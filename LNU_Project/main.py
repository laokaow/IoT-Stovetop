import time
import sensors
import actuators as a
from mqtt_client import MQTTClient
import config
import wifiConnection as w
from status_leds import update_leds

# Constants
NO_MOTION_THRESHOLD = 300  # 5 minutes
TEMP_THRESHOLD = 40 # Temperature treshold might need to be tampered with depending on the environment
PRESS_THRESHOLD = 2
MANUAL_OVERRIDE_DURATION = 1800
TEMP_SEND_INTERVAL = 15
NO_MOTION_SEND_INTERVAL = 60

# Global Variables
mqtt_connected = False
system_on = False
override_active = False
alarm_active = False
override_end_time = 0
button_pressed_time = 0
button_was_pressed = False
button_pressed = False
motion_timer = 0
current_temp = None
motion_last_detected = time.time()
last_temp_sent = 0
last_motion_sent = 0 # Updates when sending motion data
last_no_motion_sent = 0 # Updates when publishing no movement

# MQTT Setup
CLIENT_ID = config.ADAFRUIT_IO_USERNAME + "_sensor01"
MQTT_SERVER = "io.adafruit.com"
MQTT_PORT = 1883

# MWTT Topics
TOPIC_TEMP_CURRENT = f"{config.ADAFRUIT_IO_USERNAME}/feeds/{config.AIO_FEED_CURRENTTEMP}"
TOPIC_TEMP_GRAPH = f"{config.ADAFRUIT_IO_USERNAME}/feeds/{config.AIO_FEED_TEMPGRAPH}"
TOPIC_MOTION = f"{config.ADAFRUIT_IO_USERNAME}/feeds/{config.AIO_FEED_MOTION}"
TOPIC_ALARM = f"{config.ADAFRUIT_IO_USERNAME}/feeds/{config.AIO_FEED_ALARM}"
TOPIC_STATUS = f"{config.ADAFRUIT_IO_USERNAME}/feeds/{config.AIO_FEED_STATUS}"


mqtt_client = MQTTClient(
    client_id=CLIENT_ID,
    server=MQTT_SERVER,
    user=config.ADAFRUIT_IO_USERNAME,
    password=config.ADAFRUIT_IO_KEY,
    keepalive=60 
)

mqtt_client.set_last_will(TOPIC_STATUS, "OFFLINE", retain=False, qos=1) # LWT. Sends from the MQTT Broker in case of power outage etc. Currently not working

# Callback-function for if wanting to subsribe
def mqtt_callback(topic, msg):
    print("Message Recieved:", topic, msg)

mqtt_client.set_callback(mqtt_callback)

# Function for connecting to mqtt
def connect_mqtt():
    global mqtt_connected
    try:
        mqtt_client.connect()
        mqtt_connected = True
        print("MQTT connected.")
        mqtt_client.publish(TOPIC_STATUS, "ONLINE")
    except Exception as e:
        mqtt_connected = False
        print("MQTT connection failed:", e)

# A function which both checks wifi connection and mqtt connection
# Important for a system which is security critical and needs to maintain or at least notify when connection fails
def check_and_reconnect():
    global mqtt_connected
    if not w.is_connected():
        print("WiFi lost. Reconnecting...")
        try:
            w.connect_wifi()
            print("WiFi reconnected.")
        except Exception as e:
            print("WiFi reconnection failed:", e)

    if not mqtt_connected:
        print("MQTT lost. Reconnecting...")
        connect_mqtt()

# Buzzer and TOPIC_ALARM are active at the same time
def activate_alarm():
    global alarm_active
    a.buzzer.on()
    mqtt_client.publish(TOPIC_ALARM, "1")
    alarm_active = True
    print("Alarm ON")

def deactivate_alarm():
    global alarm_active
    a.buzzer.off()
    mqtt_client.publish(TOPIC_ALARM, "0")
    alarm_active = False
    print("Alarm OFF")


def reset_measurements():
    global current_temp, motion_last_detected, last_temp_sent, last_motion_sent, last_no_motion_sent
    current_temp = None
    motion_last_detected = time.time()
    last_temp_sent = 0
    last_motion_sent = 0
    last_no_motion_sent = 0
    print("Measurements reset")

def wait_for_start():
    print("System OFF. Waiting for button hold to start System.")
    if mqtt_connected:
        mqtt_client.publish(TOPIC_STATUS, "STANDBY") # Waiting after this for button press
    while True:
        button_pressed = sensors.read_button()
        update_leds(time.time(), False, False, False, button_pressed) # Sets the correct LED
        if button_pressed:
            press_start = time.time()
            while sensors.read_button():
                time.sleep(0.1)
            if time.time() - press_start >= PRESS_THRESHOLD:
                print("System ON")
                mqtt_client.publish(TOPIC_STATUS, "ONLINE")
                return  # Back to the main loop
        time.sleep(0.1)

connect_mqtt()
print("System has power and is " + ("connected" if w.is_connected() else "not connected") + " to Wifi")

while True: # Main Loop which executes the main functions
    now = time.time()

    if not system_on:
        wait_for_start() #Waiting until button press
        system_on = True
        check_and_reconnect()
        override_active = False
        reset_measurements() 
        deactivate_alarm()
        time.sleep(0.1)

    else:
        check_and_reconnect()
        button_pressed = sensors.read_button()
        update_leds(now, system_on, override_active, alarm_active, button_pressed) #Checks which LED logic to follow

        if button_pressed:
            press_start = now
            while sensors.read_button():
                time.sleep(0.01) # Enables it to sense button holds for 10 ms
            press_duration = time.time() - press_start # Separation between time.time() and now might be important. It works like this at least

            if press_duration >= PRESS_THRESHOLD: # Turns the System off
                system_on = False
                override_active = False
                deactivate_alarm()
                mqtt_client.publish(TOPIC_STATUS, "STANDBY")
                print("System OFF. Standby mode.")
                continue
            else:
                override_active = not override_active # Switches between override from ON to OFF and vice versa. Toggle Logic
                if override_active: # If not override active this if statement turns on and starts the override
                    override_end_time = now + MANUAL_OVERRIDE_DURATION
                    mqtt_client.publish(TOPIC_STATUS, "OVERRIDE")
                    deactivate_alarm()
                    print("Manual override started and alarm stopped. System back to normal in 30 minutes or when button is pressed again.")
                else:
                    print("Manual override stopped.")
                    motion_last_detected = now # Simple solution codewise to make a reasonable pause for the alarm
                    check_and_reconnect()
                    mqtt_client.publish(TOPIC_STATUS, "ONLINE")
        if override_active and now >= override_end_time: # If the override time runs out
            override_active = False
            print("Manual overrides 30 minute timer ended.")
            check_and_reconnect()
            mqtt_client.publish(TOPIC_STATUS, "ONLINE")

        # Iteration which senses temperatures, sends to Adafruit and prints in terminal
        if now - last_temp_sent >= TEMP_SEND_INTERVAL:
            current_temp = sensors.read_temperature() 
            if current_temp is not None:
                mqtt_client.publish(TOPIC_TEMP_CURRENT, str(current_temp))
                mqtt_client.publish(TOPIC_TEMP_GRAPH, str(current_temp))
                print(f"Current temperature: {current_temp:.2f} degrees Celsius")
            last_temp_sent = now
        # Iteration which senses when motion is detected, sends to Adafruit and prints in terminal
        if now - last_motion_sent >= NO_MOTION_SEND_INTERVAL:
            motion = sensors.detect_motion()
            if motion:
                motion_last_detected = now
                mqtt_client.publish(TOPIC_MOTION, "Just Now")
                print("Movement Detected!")
                last_no_motion_sent = now
            last_motion_sent = now
        # Iteration that calculates how long since motion was detected, sends to Adafruit and prints in terminal
        seconds_since_motion = int(now - motion_last_detected)
        if seconds_since_motion >= 60 and now - last_no_motion_sent > NO_MOTION_SEND_INTERVAL:
            minutes = seconds_since_motion // 60
            mqtt_client.publish(TOPIC_MOTION, f"{minutes} min ago")
            print(f"No Movement for {minutes} minutes")
            last_no_motion_sent = now

        # Variable for less code repetition
        alarm_should_be_on = (system_on and not override_active and 
                              current_temp is not None and current_temp > TEMP_THRESHOLD and
                              (now - motion_last_detected) > NO_MOTION_THRESHOLD)

        if alarm_should_be_on and not alarm_active:
           activate_alarm()
        elif not alarm_should_be_on and alarm_active:
           deactivate_alarm()

        mqtt_client.check_msg() #Not yet subscribing to a topic
        time.sleep(0.2)
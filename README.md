# IoT-Stovetop

A "smart" warning system which tracks temperature above the stovetop. In conjunction with a motion detector the system knows whether the stove/oven is on and if no one is there using it. Connected to wifi and sending messages with the mqtt protocol to be able to monitor remotely
---

This is my project report for the summer course Applied IoT 1DT305 @ Linnaeus University.
 
Author: Edwin Bylander  
Student Credentials: ed225bu

### Estimated time:  
Putting hardware together(Following the diagram): 1-3 hours. Note: this is without trimming cables, soldering etc  
Writing the code: I put around 20-30 hours (including wifi connection, mqtt etc)  
Adafruit and MQTT (Setting up feeds, dashboards): 1-2 hours  
Fixing the Back/Frontend: Entirely dependent on the level of the system and the developer 


### Objective
This stovetop monitor serves as warning system for a stovetop. It tracks temperature above the stovetop - in my case the stove and oven are combined in one unit and they emit heat upwards.

It is perfect if you have small rascals (toddlers) running around whom might accidentally (or on purpose, but unkowing of the potential consequences) turn on any or all of the dials for the stovetop. The buzzer will then serve its purpose and warn you if no movement has been detected for an appropiate amount of time(5 minutes in my case).

It is also perfect for the classic "Did I really turn the stove off?" when you just locked the door, or arrived somewhere. Perhaps someone accidentally turned a dial on after you last checked, or you simply just forgot. Then you can check in the app/website for the temperature and feel a sense of calm.

This project teaches how to use a microcontroller, connect sensors and actuators, write code, connect with wifi and communicate using the mqtt protocol. It's quite encompassing.

### Material
| IoT-Thing | Purpose  | Product Code|
|-----------|----------|-----------|
| Raspberry Pi Pico WH  | MCU, The actual "brain"  |  41019114  |
| Breadboard with 840 connections     | Easier to connect and structure everything     |  10160840 |
|PIR motion detector HC-SR501 |Detecting movement|41015509|
|Temperature sensor DS18B20|Collecting temperature|41015731|
|Active Piezo Speaker|To make a sound and alert people|41015713|
|Push Button Momentan|To be able to press a button|41015723|
|Red LED|For red light|40307020|
|Yellow LED|For yellow light|40307021|
|Green LED|For green light|40307023|


Additionally microUSB to USB-A cable, Male-Male cables, Male-Female cables are also needed.  
3x Resistors at 0.25 W 330 ohm each was used for the leds. Product Code at Electrokit: 40810233

I chose the Raspberry Pi Pico WH because of it's versatility, price and ease of use. It is a microcontroller (mcu), which in this project is programmed in micropython. WH indicates that it is presoldered - which for someone who doesnt own soldering equipment is a huge bonus. Its layout is readily available online and also in my repository.

###### Picture of the pico
![image](https://github.com/user-attachments/assets/1419cce2-51e1-4fd8-94a7-0718a2ece3e9)


I used the breadboard to easier connect everything.
###### Picture of the breadboard
![image](https://github.com/user-attachments/assets/ff791d0e-5182-4493-8750-4b4cf0390718)


I used an active buzzer as it just plays one alarm sound and when the stove is on with no one there it is a suitable tone.
###### Picture of the buzzer
![image](https://github.com/user-attachments/assets/48dadf5f-2b9d-4413-8fa2-ee7fe877c5a6)


The DS18B20 Temparature sensor which has a range from -55°C to +125°C. A longer cable could be used for more accurate measurements, but this sensor measures the surrounding temperature/warm air over the stove. It works, but directly adding a temperature cable which can resist and measure 100s of °C will be quicker and more accurate.
###### Picture of the temperature sensor
![image](https://github.com/user-attachments/assets/cf6619a9-c003-4d7c-84ca-8816119533a1)

The PIR motion detector works by detecting temperature + movement together. Placement is of importance and it should not be placed so it senses the stoves heat. It is also very adaptable, it has two potentio meters. You can easily set its detection range between 3-7 meters for your specific environment. The time delay can be set between 5 to 200 seconds.
###### Picture of the motion sensor
![image](https://github.com/user-attachments/assets/870e65c9-24a8-4dfb-aad3-59ffae71f688)

The Push Button Momentan seemed simple enough. When pushed down output is low and when not pushed down the output is high
###### Picture of the push button
![image](https://github.com/user-attachments/assets/87f7ac1f-9497-46bd-be3b-78d82f8e3681)

LEDs for different lights. The green one could have been stronger. The same ohm was used for each respective LEDs resistor. I will omit the picture.

The materials were sourced solely from electrokit.com.
A Start Kit containing the mcu, breadboard, cables etc which was bought for SEK 279.20.
A Sensor Kit containing 24 different modules which was bought for SEK 239.20.
The PIR motion detector was bought for SEK 44.00.


### Computer Setup
The chosen IDE for this project is VS code.
The setup differs between operating systems but this project was created using windows.
To setup the environment for windows the steps below were followed.
1. Download and install Node.js https://nodejs.org/en/
2. Download and install VS code https://code.visualstudio.com/download
3. In VS code press the extensions tab or press ctrl+shift+x
4. Search for PyMakr and install the PyMakr plugin

Now the programming environment should be up and running. The next step is to update the Raspberry pi pico to make sure its running the latest version. To do this the following steps were followed.
###### Flashing the Pico
1. Remove the black ESD sponge from the pico
2. Download the micropython firmware - important that you identify the correct version of your pico. Most likely you have a Raspberry Pi Pico W or a Raspberry Pi Pico 2 W. For the Raspberry Pi Pico W you download this .uf2 file: https://micropython.org/resources/firmware/RPI_PICO_W-20250415-v1.25.0.uf2
3. Connect the cable with the microUSB side to your pico
4. Press and hold the bootsel button on your pico whilst inserting the USB type A to your computer. The bootsel makes your pico act like a USB drive. Release the bootsel after it has connected to the computer.
5. Open up the new drive named RPI-RP2 and paste the .uf2 file into its storage
6. Once the drive dissapears, then you can take the usb cable out of the computer
7. Insert again (without the pressing bootsel) to make sure it worked

###### Testing your newly updated Pico
1. Open VS code and press the PyMakr extension
2. Plug your pico in(again not pressing bootsel). The new device that pops up is your pico
3. Press the lightning button to connect
4. Hower over the device again, press on the terminal button
5. In the terminal write a simple print("Hello World")
6. If everything is up and running you should be welcomed to Micropython with its version number, the name of your mcu and the text you just typed in

This should cover everything you need to start, as long as you use windows and have this specific version of Raspberry Pi Pico W.

Now for writing code and loading it to your Pico you simply insert the Pico to your PC, open PyMakr, press the connect button, and then press start development mode. This makes it very easy to just write code, press ctrl+s and it automatically uploads it and runs on your Pico. 

Note: It can be a bit finicky at times. But disconnecting and unplugging your device, then plug in and connect again usually does the trick!


### Putting everything together

Below is the wiring of this project.
- Black cables represent ground (gnd).
- Red cables represent power 3v3
- Orange, yellow, cyan represent the connection between the GPIO pins on the mcu and the components Signal (S) DQ pins

The components are not a perfect match to their real life counterparts. But some simple deduction will help differentiate between the DS18B20 temperature sensor, PIR motion detector, Active Piezo Buzzer and the Press Button.

The LEDs coudln't (or I didn't figure out how to) rotate. The long legs are next to the GPIO-Pins. They use the same 330 ohm resistors. This can, and probably should be changed to manually control their light output.  
Note: The components used for the real IoT Device already has built-in resistors. Hence they are not represented.

![Electrical Wiring](https://github.com/user-attachments/assets/88360df7-9c4e-4b78-8583-1a0cad7a23ff)


### Platform
The hosting platform used for this project is Adafruit IO which is cloud based. It offers MQTT-based data management and visualization for IoT-devices.  
Currently the free tier is used. That means its history and feed storage is limited.

For a larger, more sophisticated project you could either go for something like Google Cloud IoT which offers large storage and more advanced analytics. Or depending on the product designing a database from scratch and creating your own frontend.

However for a smaller project like this, or a quick prototype, it is very good. The feeds were up and running quickly, the data was clear and it was easy to customize for your need.

You can also easily integrate with Discord via webhooks to send you notifications or live updates. You can even interact with your IoT-device throgh Actions - For example making a button in your dashboard turn on or off a light.


### The Code

Code Structure
| File               | Description               |
|--------------------|---------------------------|
| `main.py`          | Main program entry point  |
| `boot.py`          | Runs when program gets power|
| `config.py`        | Configuration settings    |
| `keys.py`          | Variables for Wifi        |
| `sensors.py`       | Declaring the Sensors     |
| `actuators.py`     | Declaring the Actuators   |
|`status_leds.py`    | LED logic                 |
| `wifiConnection.py`| Functions for connecting to wifi|
|`mqtt_client.py`    |Functions for connecting to mqtt and Adafruit|

You can fin the full code [here](https://github.com/laokaow/IoT-Stovetop/tree/main/LNU_Project)  
Some help code for connecting to mqtt and wifi.  
[MQTT Code](https://github.com/iot-lnu/pico-w/blob/main/network-examples/N2_WiFi_MQTT_Webhook_Adafruit/lib/wifiConnection.py)  
[Wifi Code](https://github.com/iot-lnu/pico-w/blob/main/network-examples/N2_WiFi_MQTT_Webhook_Adafruit/lib/wifiConnection.py)  

###### High Level explanation with some pseudocode
- boot.py initializes the wifi connection when the system gets power
- before main loop the device connects to mqtt
- if system not on then red LED blinks slowly and the wait_for_start() function waits for button press AND updates status to STANDBY - no data is sent
- hold the button 2+ seconds to set system on
- if system on then green LED ALWAYS on AND data sends continually to Adafruit AND status is set ONLINE
- if temperature over a certain threshold and no movement for a certain amount of time then alarm blaring AND dashboard shows a red circle AND red LED blinking
- if button press under 2 seconds then override disables the alarm and puts the system on hold for 30 minutes or until button pressed again under 2 seconds AND updates status to OVERRIDE
- when override active then yellow LED and green LED are active
- if system on then hold the button 2 seconds - Goes back to the beginning of the wait_for_start() - wifi+mqtt still active

###### Start function
```python
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
  ```

###### Controlling internet and mqtt connection - Function used throughout the code to make sure wifi and mqtt are connected
```python
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
```
###### Example function. The mqtt alarm topic and physical buzzer logic lives together
```python
def activate_alarm():
    global alarm_active
    a.buzzer.on()
    mqtt_client.publish(TOPIC_ALARM, "1")
    alarm_active = True
    print("Alarm ON")
```
###### LED logic
```python
def update_leds(now, system_on, override_active, alarm_active, button_pressed):
    update_green_led(system_on)
    update_yellow_led(now, override_active, button_pressed)
    update_red_led(now, alarm_active, system_on)

# Green led always on when system is on
def update_green_led(system_on):
    if system_on:
        a.green_on()
    else:
        a.green_off()

def update_yellow_led(now, override_active, button_pressed):
    global yellow_led_on, last_yellow_blink_time
    if button_pressed:
        # Yellow led blinking quickly when button pressed
        if now - last_yellow_blink_time >= 0.05:
            yellow_led_on = not yellow_led_on
            if yellow_led_on:
                a.yellow_on()
            else:
                a.yellow_off()
            last_yellow_blink_time = now
    else:
        # Yellow led on during override
        if override_active:
            a.yellow_on()
            yellow_led_on = True
        else:
            a.yellow_off()
            yellow_led_on = False

def update_red_led(now, alarm_active, system_on):
    global red_led_on, last_red_blink_time
    if alarm_active:
        # Red blinking quickly when alarm active
        if now - last_red_blink_time >= 0.5:
            red_led_on = not red_led_on
            if red_led_on:
                a.red_on()
            else:
                a.red_off()
            last_red_blink_time = now
    elif not system_on:
          if red_led_on:
            if now - last_red_blink_time >= 0.1: #Slow blink when in standby mode
                a.red_off()
                red_led_on = False
          else:
            if now - last_red_blink_time >= 9.8:
                a.red_on()
                red_led_on = True
                last_red_blink_time = now
    else:
        a.red_off()
        red_led_on = False
```
###### Main loop with explanations
```python
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
```




### Data and Connectivity
I chose to connect my mcu with wifi as my IoT device will just be inside my house and my router is closeby and very stable.

When connecting with wifi it is important to separate sensitive data from main code that you push publicly.  
To do this you can create variables such as:  
  WIFI_SSID = 'Your_SSID'  
  WIFI_PASS = 'Your_Password'  
Then you can reference these variables in your main code without risking others connecting to your wifi. Of course replacing with the actual values. Then you add it to .gitignore so you don't accidentally push it publicly.

The same holds true for your Adafruit credentials  
ADAFRUIT_IO_USERNAME = "username"  
ADAFRUIT_IO_KEY = "key"  

Temperature Data is sent every 15 seconds. This might be too often for a free tier service, but I enjoy having a lot of data.  
Motion Data is sent every minute
- If no detected movement it increments 1 minute each time it sends
- If movement detected it resets the motion counter to zero and presents "Just Now" in the dashboard
System Status Data is sent every time the system status changes - which shouldn't be too often for an active in use system. When testing it sends whenever you turn the system on/off or when you override  
Alarm Status is sent everytime the alarm is on and when it turns off

All this Data is sent using the mqtt_client method publish(). Each of these datapoints have their own defined topics and values which are sent at the above explained times and intervals.

In the program several checks are performed, and also try methods, to ensure that the program always has a connection to both wifi and mqtt.  
As I commented in the code this is security critical for a real system which has critical use cases.

Here is an example of how mqtt messages are sent.  
```python TOPIC_TEMP_CURRENT = f"{config.ADAFRUIT_IO_USERNAME}/feeds/{config.AIO_FEED_CURRENTTEMP}" ```
ADAFRUIT_IO_USERNAME and AIO_FEED_CURRENTTEMP are both hidden constants in another file. Writing the code this way makes it more secure.  
This sends the data to the currect URL for that specific feed.
```python mqtt_client.publish(TOPIC_TEMP_CURRENT, str(current_temp))```
I even implemented the kill switch method for mqtt. However at this point in time it doesn't work. The goal is for the dashboard to show OFFLINE when the power is off or when something unexpected happens to the supply or wifi.  


### Data Presentation
Adafruit IO is used to visualize the data.
Creating a dashboard is quite straight forward
- You create feeds, name them and give them a description. Then you can choose between a URL, API URL or mqtt key.
- Then to create the dashboard you place feeds and match them with a suiting icon which displays different types of data.
- After this is done you can send data from your IoT device directly to Adafruit. In my case I used mqtt.
- Below in the code section you can see some examples of this.

For my project I both wanted a temperature graph (to see whether the temperature is rising or getting lower).
There is a simple box that shows the current temperature.
A box thats shows, in minutes the last time movement was detected. It also shows if movement was recently detected also.
A circle which is red when the alarm(buzzer) is blaring. It is green when the alarm is off.
There is also a status bar that displays which mode the system currently is in (ONLINE, OFFLINE, STANDBY, OVERRIDE)

As in this project I use the free version of Adafruit. They store 1kb of data when history is turned on. Hence the only database used is Adafruits storage. As my IoT Devices main purpose is a warning system for the home kitchen the need for structured and long term data is not needed.  
If this device were to have more sophisticated sensors, like for example high precision and high limit temperature sensors for each cooking plate and for the oven. Then you could store really interesting cooking data.  
- Individual cooking data for each plate
- Each plates efficiency (warm up time and cool down time)
- Combined with measuring which heat setting, 1-6, see max temperature of each setting etc.
- Also a more precise (more precise code) motion detector could see how many times the kitchen is entered, how long time is spent there etc.
The possibilities are endless!
My system serves as a warning system however and do not need this level of sophistication just yet. It would definitely be the next step in my Stovetop Monitors evolution however.

###### Picture of the dashboard
![Active measurements](https://github.com/user-attachments/assets/58cf02a3-8b2c-4376-a564-901f43b727c7)

![Override mode](https://github.com/user-attachments/assets/7042bd4d-0e9b-444e-899e-51a5e7b03f99)

![Standby Mode](https://github.com/user-attachments/assets/8cf1235d-cb25-4866-a4ef-c79cf1cfec8f)

![Movement Detected](https://github.com/user-attachments/assets/cf534827-d813-46a8-bda3-f2194be6b9fc)



### Final Design
All in all I am happy with my project.![IoT-Device](https://github.com/user-attachments/assets/63613c56-0e75-44bf-bfcb-59573516a9e2)
![IoT-Device](https://github.com/user-attachments/assets/86ced9b4-c9f8-4cde-bc34-e4b21b92838d)


**What to change?**

- Getting a stronger and more consumer grade temperature sensor. Trimming the cables. Then it can be mounted
- Creating my own frontend and backend for more freedom when visualizing the data.
- Have more color coded dupont cables. Easier when one color means one thing. Red = power for example.

**Extras to buy**

A 3D printer. To make my own case would be really awesome. While it is cool to see all the wires and components connected, it would be even cooler to have it all encased and hanging on the wall. It would then maybe look like a consumer grade item.  
Soldering equipment, cutters, good tape etc. To easier shorten cables and make pins stick better. It makes it much more reliable and customizable.


### Final thoughts
This project, and in extension course, has been very interesting. It bridges the gap between software and hardware and it teaches you how everything is connected.  
One revelation I had was how "simple" many common household items can be. Take for example a smoke detector/fire alarm. Before this course I couldn't tell you how it really worked and if I were to just start building one I wouldnt even know where to start. To illustrate my point, I will do a high level list of what is needed, just from the top of my head.
- MCU. The brain controlling the device
- Wires and cables to connect everything
- Other electrical components such as resistors or transistors if needed
- Battery
- Sensors
  - Smoke detection sensors, heat detection sensors
- Actuators
  - buzzers, led lights
- Casing. 3D print it to your liking and leave a spot for the led light to stick out
- Code for the hardware. Can be anything from simple to complex. Pseudocode examples:
  - if battery level < 20% then buzzer make sound.beep
  - if heat over 50 Celsius OR smoke detected then buzzer make sound.max AND send.alarm to application

Then for connecting it with the internet
- Connect the mcu to wifi(or other technologies of your choice)
- Make an app or website, self hosted or through services
- Make a notification or alarm sound on your device/s of choice if a fire is breaking out

Sure, making a consumer grade item which NEEDS to work brings more complexity and responsibility than just building one together for a project. You need certifications, testing your code, making backups, soldering the components etc etc. Disclaimer: Don't make one and use it as your only source of fire alarm and don't sell it to other people, you need to check with the local laws and regulations first.
Why I brought this example up was to show that the technology behind such items neccessarily isn't that complex and that you could learn to make a working prototype of a fire alarm just by following this course.


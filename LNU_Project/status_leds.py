import actuators as a
import time

# LED-status
red_led_on = False
yellow_led_on = False

last_red_blink_time = 0
last_yellow_blink_time = 0
last_yellow_fast_blink_time = 0

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
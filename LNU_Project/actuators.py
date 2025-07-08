import machine
import time

BUZZER_PIN = 26
RED_LED_PIN = 13
YELLOW_LED_PIN = 14
GREEN_LED_PIN = 15

buzzer = machine.Pin(BUZZER_PIN, machine.Pin.OUT)

red_led = machine.Pin(RED_LED_PIN, machine.Pin.OUT)
yellow_led = machine.Pin(YELLOW_LED_PIN, machine.Pin.OUT)
green_led = machine.Pin(GREEN_LED_PIN, machine.Pin.OUT)

def alarm_on():
    buzzer.on()

def alarm_off():
    buzzer.off()

def red_on():
    red_led.value(1)

def red_off():
    red_led.value(0)

def yellow_on():
    yellow_led.value(1)

def yellow_off():
    yellow_led.value(0)

def green_on():
    green_led.value(1)

def green_off():
    green_led.value(0)
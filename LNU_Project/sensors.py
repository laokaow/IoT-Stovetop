import machine
import onewire
import ds18x20
import time

TEMP_PIN = 27
PIR_PIN = 17
BUTTON_PIN = 3

pir = machine.Pin(PIR_PIN, machine.Pin.IN)
ds_pin = machine.Pin(TEMP_PIN)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
roms = ds_sensor.scan()

def detect_motion():
    return pir.value()

def read_temperature():
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        return ds_sensor.read_temp(rom)
    return None
def read_button():
    return button.value() == 0
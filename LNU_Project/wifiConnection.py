import keys
import network
from time import sleep

wlan = network.WLAN(network.STA_IF)  

def connect_wifi():
    if not wlan.isconnected():             
        print('Connecting to network...')
        wlan.active(True)                       
        wlan.config(pm = 0xa11140)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  
        print('Waiting for connection...', end='')
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip

def disconnect_wifi():     
    wlan.disconnect()

def test_wifi_connection():
    ip = connect_wifi()
    if ip:
        print("Wi-Fi is connected")
        return True
    else:
        print("Wi-Fi is not connected")
        return False

def is_connected():
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()
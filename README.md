# IoT-Stovetop

This is my project report for the summer course Applied IoT 1DT305 @ Linnaeus University.

A "smart" warning system which tracks temperature above the stovetop. In conjunction with a motion detector the system knows whether the stove/oven is on and no one is there using it.

Author: Edwin Bylander
Student Credentials: ed225bu

Estimated time: 
Putting hardware together: 2 hours. Note: this is without trimming cables, soldering etc
Writing the code: I put around 20-30 hours (including wifi connection, mqtt etc)
Adafruit and MQTT (Setting up feeds, dashboards): Under 1 hour
Fixing the Back/Frontend: ---


### Objective
This stovetop monitor serves as warning system for a stovetop. It tracks temperature above the stovetop - in my case the stove and oven are combined in one unit and they emit heat upwards.

It is perfect if you have small rascals (toddlers) running around whom might accidentally (or on purpose, but unkowing of the potential consequences) turn on any or all of the dials for the stovetop. The buzzer will then serve its purpose and warn you if no movement has been detected for an appropiate amount of time(5 minutes in my case).

It is also perfect for the classic "Did I really turn the stove off?" when you just locked the door, or arrived somewhere. Perhaps someone accidentally turned a dial on after you last checked, or you simply just forgot. Then you can check in the app/website for the temperature and feel a sense of calm.

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

I chose the Raspberry Pi Pico WH because of it's versatility, price and ease of use. It is a microcontroller (mcu), which in this project is programmed in micropython. WH indicates that it is presoldered - which for someone who doesnt own soldering equipment is a huge bonus. Its layout is readily available online and the m
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

Using smart names for your .py files is recommended to easier work with the code.


### Putting everything together

Here I will update with the circuits

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


Some help code for connecting to mqtt and wifi.
[MQTT Code](https://github.com/iot-lnu/pico-w/blob/main/network-examples/N2_WiFi_MQTT_Webhook_Adafruit/lib/wifiConnection.py)
[Wifi Code](https://github.com/iot-lnu/pico-w/blob/main/network-examples/N2_WiFi_MQTT_Webhook_Adafruit/lib/wifiConnection.py)

###### Connecting to wifi
<pre markdown="1">
  import wifiConnection


def http_get(url = 'http://detectportal.firefox.com/'):
    import socket                           # Used by HTML get request
    import time                             # Used for delay
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialise the socket
    s.connect(addr)                         # Try connecting to host address
    # Send HTTP request to the host with specific path
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receve response
    print(rec_bytes)                        # Print the response
    s.close()                               # Close connection

#First thing that should run
print("Booting Stovetop Monitoring Device")

# Connecting to wifi when giving the system power
try:
    ip = wifiConnection.connect_wifi()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Gets information about the network connection
try:
    http_get()
except (Exception, KeyboardInterrupt) as err:
    print("No Internet", err)
</pre>

<pre markdown="1">
  
</pre>




### Data and Connectivity
I chose to connect my mcu with wifi as my gadget will just be inside my house and my router is closeby and very stable.

When connecting with wifi it is important to separate sensitive data from main code that you push publicly.
To do this you can create variables such as
  WIFI_SSID = 'Your_SSID'
  WIFI_PASS = 'Your_Password'
Then you can reference these variables in your main code without risking others connecting to your wifi. Of course replacing with the actual values. Then you add it to .gitignore so you don't accidentally push it publicly.

The same holds true for your Adafruit credentials
ADAFRUIT_IO_USERNAME = "username"
ADAFRUIT_IO_KEY = "key"




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

As in this project I use the free version of Adafruit. They store 1kb of data when history is turned on. 1

###### Picture of the dashboard



### Final Design
All in all I am happy with my project.


**What to change?**

Getting a stronger and more consumer grade temperature sensor. For this project some DIY and taping needed to be done, and the reliability isnt 100%.
Creating my own frontend and backend for more freedom when visualizing the data.

**Extras to buy**

A 3D printer. To make my own case would be really awesome. While it is cool to see all the wires and components connected, it would be even cooler to have it all encased and hanging on the wall. It would then maybe look like a consumer grade item.
Soldering equipment, cutters, good tape etc. To easier shorten cables and make pins stick better. It makes it much more reliable and customizable.

Pictures:

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


# IoT-Stovetop

This is my project report for the summer course Applied IoT 1DT305 @ Linnaeus University.

A "smart" warning system which tracks temperature above the stovetop. In conjunction with a motion detector the system knows whether the stove/oven is on and no one is there using it.

Author: Edwin Bylander
Student Credentials: ed225bu

Estimated time to replicate:
Putting hardware together: 2 hours (if everything is unpacked, structured and you know how to do it)
Writing the code: 
Fixing the Back/Frontend:


### Objective
This stovetop monitor serves as warning system for a stovetop. It tracks temperature above the stovetop - in my case the stove and oven are combined in one unit and they emit heat upwards.

It is perfect if you have small rascals (toddlers) running around whom might accidentally (or on purpose, but unkowing of the potential consequences) turn on any or all of the dials for the stovetop. The buzzer will then serve its purpose and warn you if no movement has been detected for an appropiate amount of time.

It is also perfect for the classic "Did I really turn the stove off?" when you just locked the door, or arrived somewhere. Perhaps someone accidentally turned a dial on after you checked, or you simply just forgot. Then you can check in the app/website for the temperature and feel a sense of calm.

### Material
| IoT-Thing | Purpose  | Product Code|
|-----------|----------|-----------|
| Raspberry Pi Pico WH  | MCU, The actual "brain"  |  41019114  |
| Breadboard with 840 connections     | Easier to connect and structure everything     |  10160840 |
|PIR motion detector HC-SR501 |Detecting movement|41015509|
|Temperature sensor DS18B20|Collecting temperature|41015731|
|Active Piezo Speaker|To make a sound and alert people|41015713|

Additionally microUSB to USB-A cable. Male-Male cables, Male-Female cables are also needed.

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

This should cover everything you need to start, as long as you use windows and have this specific version of Raspberry Pi Pico W


### Putting everything together

### Platform
The hosting platform used is Adafruit IO. This service makes it easy to get your project quickly up and running. It makes data transfer, visualization of data, and controlling units very easy. It can easily integrate with Discord via webhooks to send you notifications or live updates. You can even interact with your device.



For further development on this project I would very much like to design my own database and frontend. There are plenty of alternative ways of doing this. For lightweight projects SQLite could be used and for more advanced projects 
### The Code

### Data and Connectivity
To connect with wifi it is important to separate sensitive data from main code that you push publicly.
To do this you can create variables such as
  WIFI_SSID = 'Your_SSID'
  WIFI_PASS = 'Your_Password'
Then you can reference these variables in your main code without risking others connecting to your wifi.

### Data Presentation
Adafruit IO is used to visualize the data.

#This is to be updated a bit more
For my project I both wanted a temperature graph (to see whether the temperature is rising or getting lower).
I also wanted a simple box that shows the current temperature.
I also want a box thats shows, in minutes or seconds, the last time movement was detected.

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


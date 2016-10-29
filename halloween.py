# 1. connect the PIR
#    - VCC with 5V
#    - GND with GND
#    - OUT with GPIO PIN 4
# 2. connect an LED
#    - GND with GND
#    - positiv to GPIO PIN 17
# 3. install mpg123
#    - sudo apt-get install mpg123

from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep
from subprocess import call

mp3_file = "13201"

pir = MotionSensor(4)
led = LED(17)
while True:
    if pir.motion_detected:
        print("Motion detected!")
        led.on()
        call(["mpg123",mp3_file])
        led.off()

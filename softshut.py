# Import the modules to send commands to the system and access GPIO pins
import RPi.GPIO as gpio
from time import sleep
from os import system
 
# Define a function to keep script running
def loop():
    while True:
        sleep(600)
 
# Define a function to run when an interrupt is called
def shutdown(pin):
    print("Interrupt detected... Halting the system!")
    system('shutdown -h now')

print("Setting GPIO...") 
gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering
gpio.setup(7, gpio.IN) # Set up pin 7 as an input
print("Setting interrupt...")
gpio.add_event_detect(7, gpio.RISING, callback=shutdown, bouncetime=200) # Set up an interrupt to look for button presses
 
loop() # Run the loop function to keep script running

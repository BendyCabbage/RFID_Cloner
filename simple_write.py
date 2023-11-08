import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

writer = SimpleMFRC522()

try:
    text = input("New data: ")
    print("Place your tag to write")
    writer.write(text)
    print("Successfully written")

finally:
    GPIO.cleanup()

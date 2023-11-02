import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input("New data: ")
    print("Place your tag to write")
    reader.write(text)
    print("Successfully written")

finally:
    GPIO.cleanup()
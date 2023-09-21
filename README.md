# RFID_Cloner
A simple RFID cloner built using a Raspberry Pi Zero W and the RC522 module

**Design decisions:**

Raspberry Pi Zero W:
 - Initial debate between Raspberry Pi and Arduino, went with Raspberry Pi as I have prior experience with them
   and they are slightly easier to setup.
 - Zero W version of the Raspberry Pi as I need something that is small, uses very little power and can still
   send messages using Bluetooth. This helps with the overall mobility of the project as the battery required is
   very small. 

RC522:
- Simple, low cost RFID module, almost every example found online uses this module.

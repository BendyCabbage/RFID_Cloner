# RFID Cloner
A simple RFID cloner built using a Raspberry Pi Zero W and the RC522 module

### Design decisions:

**Raspberry Pi Zero WH:**
 - Initial debate between Raspberry Pi and Arduino, went with Raspberry Pi as I have prior experience with them
	and they are slightly easier to setup.
 - Zero W version of the Raspberry Pi as I need something that is small, uses very little power and can still
	send messages using Bluetooth. This helps with the overall mobility of the project as only one battery is required.
 - H version as it comes with headers already soldered on, saving the time and hassle.

**RC522:**
- Simple, low cost RFID module, almost every example found online uses this module.

**UPS HAT (Uninterruptible Power Supply):**
Needed a way for the Raspberry Pi to be portable. Input to the Pi needs to be 5V DC and ~2.5A. Typical Batteries
do not have enough voltage, so a DC/DC converter would be required. Instead of creating all of this myself (which is
definitely doable), I decided to use a prebuilt component to save the time and hassle.

Additionally if the Raspberry Pi loses power unexpectedly it can corrupt the operating system. This is why a UPS was
chosen as this minimises the risk of that happening. 

**Things required:**
- Raspberry Pi Zero W
- Raspberry Pi power source (needs to output 5-5.5V and ~2.5A). Initially I used the official Raspberry Pi power supply,
	and then when I was making the build portable I switched to a Raspberry Pi UPS HAT that enabled the use of batteries.
- RC522 Module
- RFID tag
- SD/Micro SD card reader
- Micro SD card
- Method

**Setting up the Raspberry Pi:**

Setup via SSH: https://www.youtube.com/watch?v=63yw7b0NuWc
1. Install the Raspberry Pi OS on the micro SD card using the official raspberry pi installer.


**Possible extensions for the project:**
- Design and 3D print a case for the build
- Attach longer wires to the RFID reader so that the main device can be kept inside of a pocket or similar while the reader is contained in a sleeve pocket
- Use different readers for NFC, different frequencies of RFID etc.
- Implement wider support for varying RFID cards
- Instead of only guessing default keys, implement code to exploit the flaws in some RFID cards to discover the keys, for example the "offline nested" exploit on Mifare Classic cards (https://github.com/nfc-tools/mfoc)

**References:**
- https://pimylifeup.com/raspberry-pi-rfid-rc522/#:~:text=Wiring%20your%20RFID%20RC522%20to,SDA%20connects%20to%20Pin%2024
- https://github.com/mxgxw/MFRC522-python
- https://raspi.tv/2017/how-much-power-does-pi-zero-w-use
- https://github.com/nfc-tools/mfoc

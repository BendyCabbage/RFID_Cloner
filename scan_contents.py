import sys
import time
import signal

import RPi.GPIO as GPIO
from mfrc522 import MFRC522


reader = MFRC522()
key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
continue_reading = True

#Exits the main read_card loop and cleans up the GPIO pins
def end_read():
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

#Hook ctrl+c to end_read function
signal.signal(signal.SIGINT, end_read)

#Print the data in hexadecimal format
def format_hex(data):
    if data is None:
        return None
    return ''.join(['{:02X}'.format(byte) for byte in data])

#Reads a block of data from the card
def read_block(block_num: int, key, uid):
    status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, block_num, key, uid)
    if status != reader.MI_OK:
        print(f"Cannot authenticate block {block_num}", file=sys.stderr)
        return None
    
    data = reader.MFRC522_Read(block_num)
    return format_hex(data)

#Reads a sector of data from the card
def read_sector(sector_num: int, key, uid):
    block_data = []
    for block_num in range(4):
        block_data.append(read_block(sector_num * 4 + block_num, key, uid))

    return block_data

def print_sector_data(sector_data):
    for sector_num, sector_data in enumerate(sector_data):
        print(f"Sector {sector_num}: {sector_data}")

def write_data_to_file(uid, tag_type, sector_data):
    file = open("output.dmp", "a")

    file.write(f"UID: {format_hex(uid)}\n")
    file.write(f"Tag Type: {tag_type}\n")

    for sector_num, sector_data in enumerate(sector_data):
        file.write(f"Sector {sector_num}: {sector_data}\n")

#Reads the card and prints the data
def read_card():
    while continue_reading:
        (status, tag_type) = reader.MFRC522_Request(reader.PICC_REQIDL)
        if status != reader.MI_OK:
            continue

        (status, uid) = reader.MFRC522_Anticoll()
        if status != reader.MI_OK:
            continue

        print(f"UID: {format_hex(uid)}")
        print(f"Tag Type: {tag_type}")

        reader.MFRC522_SelectTag(uid)

        sector_data = []
        for sector_num in range(16):
            sector_data.append(read_sector(sector_num, key, uid))

        reader.MFRC522_StopCrypto1()

        print_sector_data(sector_data)
        write_data_to_file(uid, tag_type, sector_data)
        time.sleep(2)
    end_read()
    return 0

if __name__ == "__main__":
    read_card()
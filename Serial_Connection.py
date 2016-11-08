#! /usr/bin/env python3

import serial

port_name = input("Enter the name of the port\n")

ser = serial.Serial(port_name)

def costant_write():
    msg = input("Input the message")
    while 1 > 0:
        ser.write(int(msg+'\n'))

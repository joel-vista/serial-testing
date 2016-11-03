#! /usr/bin/env python3

import serial

port_name = input("Enter the name of the port\n")

ser = serial.Serial(port_name)
while(1 > 0):
    print(ser.read())

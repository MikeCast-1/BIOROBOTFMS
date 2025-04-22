#!/usr/bin/python3
#https://github.com/raspberrypi/picamera2/blob/main/examples/capture_jpeg.py

# Capture a full resolution image to memory rather than to a file.

import os
import time

command_0 = "rpicam-still -n -o /home/biorobot/Desktop/BIOROBOTFMS/test"
img_indx = 0
command_1 = ".jpg"


for i in range(5):
    img_indx = i
    os_command = f"{command_0}{img_indx}{command_1}"
    XD = os.system(os_command)
    
    print(os_command)
    print("\n")
    print(XD)
    print("\n")

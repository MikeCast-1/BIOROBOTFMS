#!/usr/bin/python3
#https://github.com/raspberrypi/picamera2/blob/main/examples/capture_jpeg.py

# Capture a full resolution image to memory rather than to a file.

import os
import time

command_0 = "rpicam-still -o /home/biorobot/Desktop/test"
img_indx = 0
command_1 = ".jpg"

os_command = f"{command_0}{img_indx}{command_1}"

for i in range(5):
    img_indx = i
    os_command = f"{command_0}{img_indx}{command_1}"
    XD = os.system(os_command)
    print(XD)

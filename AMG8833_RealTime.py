import serial
import time

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys


#Array to store data from the serial port 
Arr = []

#Array to store data corresponding to the heatmap 
heatmap = [[40 for _ in range(8)] for _ in range(8)] #Fill the array as 8x8 with values of 50 in each sector of the array
heatmap.pop()   #Remove the last sector in the array
heatmap.append([0 for _ in range(8)])   #Fill the last sector of the array with zeros

# Create a figure and axis
fig, ax = plt.subplots()

# Display the initial image
im = ax.imshow(heatmap, cmap='jet', animated=True,resample=True)
plt.colorbar(im) #Adding colorbar to the figure

# COM Port used to communicate with the 
com_port = 'COM6'
baud_rate = 115200  # Set the baud rate according to your device's specifications

# Open the serial port
ser = serial.Serial(com_port, baud_rate)

# Function to send data to the UART device
def send_data(data):
    ser.write(data.encode())

# Function to read data from the UART device
def read_data():
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        return data
    return None

def Scanner_debug(frame):
    
    ser.flush()
    ser.reset_input_buffer() 
    send_data('XD\n') # Send a command to the UART device
    time.sleep(0.1)
    
    
    # Read the response from the UART device
    response = read_data()
    while(response):
        Arr.append(response)
        response =read_data()

    xline = [0]*len(Arr) #2D X array containing Arr values

    #Filling xline with Arr values
    for i in range(0,len(Arr)-1):
        xline[i] = int(Arr[i])   #Convert data into Integer and store it

    Arr.clear()
    
    counter = 0
    rows, cols = 8,8
    heatmap.clear()

    #Filling the 2D array
    for i in range(0,cols-1):
        cols = []
        for j in range(0,rows-1):
            cols.append(xline[counter])
            counter += 1
        heatmap.append(cols)
    
    #Returning the heatmap data to plot it with the animation function
    new_data = heatmap
    im.set_array(new_data)
    return [im]



# Create an animation
ani = animation.FuncAnimation(fig, Scanner_debug, frames=range(1),interval=500, blit=True)

plt.title("Temperaturas del cultivo de Hongos (AMG8833)")
# Show the plot
plt.show()

import serial
import time

import numpy as np 
import matplotlib.pyplot as plt 


# Replace 'COM3' with your actual COM port
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


Arr = []

def Scanner_debug():
    # Send a command to the UART device
    send_data('Hello UART\n')
    time.sleep(0.001)
    
    
    # Read the response from the UART device
    response = read_data()
    while(response):
        Arr.append(response)
        print(f"Received: {response}")
        response =read_data()

    ser.close()

    xline = [0]*len(Arr) #2D X array containing x_line values

    #Filling xline with x_line values
    for i in range(0,len(Arr)-1):
        xline[i] = int(Arr[i])   #De-normalizing data

    heatmap =[]
    counter = 0
    rows, cols = 56,40

    #Filling the 2D array
    for i in range(0,cols-1):
        cols = []
        for j in range(0,rows-1):
            cols.append(xline[counter])
            counter += 1
        heatmap.append(cols)


    img = plt.imshow(heatmap,cmap='jet') #img figure creation with arr values and colormap = jet
    plt.colorbar(img) #Adding colorbar to the figure
    
    plt.title("Temperaturas del cultivo de Hongos") #Adding colorbar to the figure 
    plt.show() #Plotting the figure

    print("Exiting...")
    return 0

if __name__ == "__main__":
    Scanner_debug()
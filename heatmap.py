
# Program to plot 2-D Heat map 
# using matplotlib.pyplot.imshow() method 
import numpy as np 
import matplotlib.pyplot as plt 


x_line = np.random.random(2240) #Linear X vector containing random numbers

xline = [0]*len(x_line) #2D X array containing x_line values

#Filling xline with x_line values
for i in range(0,len(x_line)-1):
    xline[i] = int(100*x_line[i])   #De-normalizing data

#2D X array containing xline values
arr = []

counter = 0

rows, cols = 56,40

#Filling the 2D array
for i in range(0,cols-1):
    cols = []
    for j in range(0,rows-1):
        cols.append(xline[counter])
        counter += 1
    arr.append(cols)


img = plt.imshow(arr,cmap='jet') #img figure creation with arr values and colormap = jet
plt.colorbar(img) #Adding colorbar to the figure
  
plt.title("Temperaturas del cultivo de Hongos") #Adding title to the figure 
plt.show() #Plotting the figure
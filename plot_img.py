import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the image data
image_data = np.random.rand(40, 56) *100

# Display the initial image
im = ax.imshow(image_data, cmap='jet', animated=True)
plt.colorbar(im) #Adding colorbar to the figure

# Update the image with new data
def update(frame):
    new_data = np.random.rand(40, 56) *100
    im.set_array(new_data)
    return [im]

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(1),interval=500, blit=True)

plt.title("Temperaturas del cultivo de Hongos (Experimental)")
# Show the plot
plt.show()
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create a figure and axis
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'b-', animated=True)

# Initialize the plot
def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 10)
    return ln,

# Update the plot with new data
def update(frame):
    xdata.append(frame)
    ydata.append(random.uniform(0, 10))
    ln.set_data(xdata, ydata)
    return ln,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

# Show the plot
plt.show()
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Function to update the graph
def update_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.clear()
    ax.plot(x, y)
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("GUI with Buttons and Graph")

# Create a frame for the buttons
frame = ttk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.X)

# Add buttons to the frame
btn_update = ttk.Button(frame, text="Update Graph", command=update_graph)
btn_update.pack(side=tk.LEFT, padx=5, pady=5)

btn_quit = ttk.Button(frame, text="Quit", command=root.quit)
btn_quit.pack(side=tk.LEFT, padx=5, pady=5)

# Create a figure and axis for the graph
fig, ax = plt.subplots()

# Create a canvas to display the graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the Tkinter event loop
root.mainloop()
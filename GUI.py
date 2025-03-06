import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main window
root = tk.Tk()
root.title("Sample GUI")

# Create a frame for the canvas and scrollbar
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Add a canvas in that frame
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a scrollbar to the frame
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create another frame inside the canvas
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Add buttons to the inner frame
for i in range(5):
    button = tk.Button(inner_frame, text=f"Button {i+1}")
    button.pack(pady=10)

# Add a text input field
text_input = tk.Entry(inner_frame)
text_input.pack(pady=10)

# Function to print text from the text input field
def print_text():
    text = text_input.get()
    output_label.config(text=text)

# Add a button to trigger the print_text function
print_button = tk.Button(inner_frame, text="Print Text", command=print_text)
print_button.pack(pady=10)

# Add a label to display the printed text
output_label = tk.Label(inner_frame, text="")
output_label.pack(pady=10)

# Create a sample graph using matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Sample Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Add the graph to the GUI
canvas_graph = FigureCanvasTkAgg(fig, master=inner_frame)
canvas_graph.draw()
canvas_graph.get_tk_widget().pack(pady=10)

# Run the application
root.mainloop()
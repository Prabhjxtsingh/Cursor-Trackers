import tkinter as tk

def update_position(event):
    # Update the position of the point based on the cursor position
    canvas.coords(point, event.x - POINT_SIZE/2, event.y - POINT_SIZE/2,
                  event.x + POINT_SIZE/2, event.y + POINT_SIZE/2)

# Constants
POINT_SIZE = 30

# Create the main window
root = tk.Tk()
root.title("Cursor Tracker")
root.configure(background='black')

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create a canvas to draw on
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black")
canvas.pack(fill=tk.BOTH, expand=tk.YES)

# Draw a point
point = canvas.create_oval(0, 0, POINT_SIZE, POINT_SIZE, fill="red")

# Bind the mouse movement to update the point position
canvas.bind("<Motion>", update_position)

# Function to close the window and end the program
def close_window():
    root.destroy()

# Button to close the window
close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()

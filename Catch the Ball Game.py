import tkinter as tk
import random

# Set up the main window
root = tk.Tk()
root.title("Catch the Ball Game")
root.resizable(False, False)

# Canvas dimensions
canvas_width = 400
canvas_height = 600

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightblue")
canvas.pack()

# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_color = "darkblue"
paddle_x = (canvas_width - paddle_width) // 2
paddle_y = canvas_height - 30
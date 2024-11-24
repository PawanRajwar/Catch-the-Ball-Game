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

# Ball properties
ball_radius = 10
ball_color = "red"
ball_speed = 5
ball_x = random.randint(10, canvas_width - 10)
ball_y = 0

# Score and level
score = 0
level = 1
 
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

# Draw paddle and ball
paddle = canvas.create_rectangle(paddle_x, paddle_y, paddle_x + paddle_width, paddle_y + paddle_height, fill=paddle_color)
ball = canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius, fill=ball_color)

# Display score and level
score_text = canvas.create_text(50, 20, text=f"Score: {score}", font=("Arial", 16), fill="black")
level_text = canvas.create_text(350, 20, text=f"Level: {level}", font=("Arial", 16), fill="black")

# Global variable to track the restart button
restart_button = None

# Move paddle function
def move_paddle(event):
    x = event.x
    if x < paddle_width // 2:
        x = paddle_width // 2
    elif x > canvas_width - paddle_width // 2:
        x = canvas_width - paddle_width // 2
    canvas.coords(paddle, x - paddle_width // 2, paddle_y, x + paddle_width // 2, paddle_y + paddle_height)

canvas.bind("<Motion>", move_paddle)

# Restart the game
def restart_game():
    global ball_x, ball_y, ball_speed, score, level, restart_button

     # Reset game state
    ball_x = random.randint(10, canvas_width - 10)
    ball_y = 0
    ball_speed = 5
    score = 0
    level = 1

    # Update UI elements
    canvas.itemconfig(score_text, text=f"Score: {score}")
    canvas.itemconfig(level_text, text=f"Level: {level}")
    canvas.delete("game_over")

    # Remove restart button
    if restart_button:
        restart_button.destroy()
        restart_button = None

    # Restart ball movement
    update_ball()
    
    
# Update ball position and check for collisions
def update_ball():
    global ball_x, ball_y, score, level, ball_speed, restart_button

    ball_y += ball_speed

    if ball_y + ball_radius > canvas_height:  # Ball missed
        canvas.create_text(canvas_width // 2, canvas_height // 2, text="Game Over!", font=("Arial", 24), fill="red", tags="game_over")

        # Create restart button
        restart_button = tk.Button(root, text="Restart", command=restart_game, bg="darkblue", fg="white", font=("Arial", 12, "bold"))
        restart_button.place(x=canvas_width // 2 - 50, y=canvas_height // 2 + 40)

        return
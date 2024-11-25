# Catch the Ball Game

## Overview
Catch the Ball is an engaging and fun game created using Python and the Tkinter library. The objective is to control a paddle using the mouse to catch a falling ball. The game includes increasing difficulty levels as you score higher and provides a "Game Over" screen with a restart option for replayability.

## Features
- Mouse-Controlled Paddle: Move the paddle left or right using the mouse to catch the falling ball.

- Levels with Increasing Difficulty: The ball's speed increases as you progress to higher levels.

- Game Over Screen: Displays a message when you miss the ball.

- Restart Option: A themed restart button allows players to restart the game seamlessly.

- Dynamic Score Display: Tracks and displays the player's score and current level on the screen.

# How It Works

## Game Components

### 1. Canvas:
- The canvas serves as the playing area where all game elements are displayed.

- It has a width of 400px and a height of 600px with a light blue background.

### 2. Paddle:
- The paddle is a horizontal rectangle at the bottom of the canvas.

- It is controlled by the mouse and moves left or right while staying within the canvas boundaries.

- Dimensions:
Width: 100px
Height: 20px
Color: Dark Blue

### 3. Ball:
- The ball is a circular object that falls from the top of the canvas.

- The player's goal is to catch the ball using the paddle.

- Dimensions:
Radius: 10px
Color: Red

- Behavior: The ball falls at a speed that increases with higher levels. Each catch resets the ball to a new random position at the top.

### 4. Score and Level:
- The score increments by 1 for every successful catch.

- Every 5 points, the level increases, and the ball's falling speed accelerates.

- The score and level are displayed at the top-left and top-right corners of the canvas, respectively.

### 5. Game Over Screen:
- When the ball reaches the bottom of the canvas without being caught, the game ends.

- A "Game Over!" message appears in the center of the canvas, along with a restart button.

### 6. Restart Button:
- The restart button allows the player to replay the game without restarting the program.

- When clicked, it resets the score, level, ball speed, and positions of game elements.

- The button is styled to match the game's blue-themed design.

## Functionalities Explained

### 1. Paddle Movement
- The paddle follows the horizontal movement of the mouse.

- The bind method tracks the <Motion> event, allowing the paddle's position to update dynamically.

- Boundary conditions ensure that the paddle does not move outside the canvas.

### 2. Ball Movement
- The ball moves downward continuously, using the after() method to update its position at regular intervals.

- After a successful catch :
   - The ball resets to a random x-coordinate at the top of the canvas.

   - The score increments by 1.

   - Every 5 points, the level increases, and the ball's speed accelerates.


### 3. Collision Detection
- The game detects whether the ball's position overlaps with the paddle's position.

- A collision results in a successful catch, updating the score and resetting the ball.

- If the ball reaches the bottom without being caught, the game ends.

### 4. Game Over Screen and Restart
- When the game ends:
  - A "Game Over!" message is displayed in the center of the canvas.

  - A restart button appears below the message.

- Clicking the restart button:
  - Resets the score, level, ball speed, and positions.

  - Removes the "Game Over!" message and the restart button.

  - Starts a new game.



## Prerequisites

- Python: Ensure Python (version 3.6 or later) is installed on your system.

- Tkinter: Tkinter is included with Python by default. No additional installation is required.

## Steps to Run
- Clone the repository or copy the source code into a Python file named catch the ball Game.py

- Open your terminal or command prompt.

- Navigate to the directory containing the file.

- Run the script:
  python Catch the Ball Game.py
  

## Screenshots 

![Game Screenshot](<Screenshot 2024-11-25 122251-1.png>)

![Restart Functionality](<Screenshot 2024-11-25 122305-1.png>)



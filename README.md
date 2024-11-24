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



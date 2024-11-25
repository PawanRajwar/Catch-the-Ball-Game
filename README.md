# **🎮 Catch the Ball Game**

---

## **👨‍🏫 Submitted To**  
**Dr. Prateek Raj Gautam**

---

## **👨‍🎓 Submitted By**  
- **Name**: Pawan Singh Rajwar  
- **SAP ID**: 590017545  

---

## **📄 Project Title**  
**Catch the Ball Game**

---

## **📖 Description**  
**Catch the Ball** is an exciting and interactive game built using Python's **Tkinter library**. The goal is to control a paddle with the mouse to catch a falling ball. The game progressively becomes more challenging as players advance, with increasing ball speed and levels. A restart option is available to enhance replayability, providing endless fun!

---

## **✨ Features**
### 🕹️ **Interactive Gameplay**:
- Control the paddle using mouse movements for intuitive gameplay.
  
### 📈 **Progressive Difficulty**:
- Ball speed increases as you score more, making the game challenging with each level.

### 🎯 **Dynamic Score and Levels**:
- Tracks and displays the player's score and current level on the screen.

### ❌ **Game Over Screen**:
- Displays a clear **Game Over!** message when the player misses the ball.

### 🔄 **Restart Functionality**:
- A themed **Restart** button allows players to replay seamlessly after a game ends.

---

## **🎮 Game Components**

### 🖼️ **Canvas**:
- The main playing area for the game, with dimensions **400x600 px** and a light blue background.

### 🏓 **Paddle**:
- A horizontal rectangle controlled by the mouse to catch the ball.  
  - **Width**: 100px  
  - **Height**: 20px  
  - **Color**: Dark Blue  

### ⚽ **Ball**:
- A circular object that falls from the top of the canvas.  
  - **Radius**: 10px  
  - **Color**: Red  
  - Behavior: Resets position upon a successful catch and increases speed with levels.

### 🏆 **Score and Levels**:
- **Score**: Incremented by 1 with every catch.  
- **Level**: Increases every 5 points, accelerating ball speed for added difficulty.

### ❌ **Game Over Screen**:
- Shows a "Game Over!" message when the ball is missed, accompanied by a **Restart** button.

### 🔄 **Restart Button**:
- Resets game variables like score, level, and ball speed, and starts a new game session.

---

## **🔧 Functionalities Explained**

### 🖱️ **Paddle Movement**:
- Tracks mouse movements (`<Motion>` event) to update the paddle's horizontal position dynamically.  
- Boundary conditions ensure the paddle stays within the canvas.

### ⚡ **Ball Movement**:
- The ball moves downward continuously, with speed increasing based on the level.  
- After a successful catch:
  - Ball resets to a random x-coordinate at the top.  
  - Score and level are updated.  

### 🔍 **Collision Detection**:
- Detects overlaps between the ball and paddle to determine a catch.  
- If the ball touches the bottom without a catch, the game ends.

### ❌ **Game Over and Restart**:
- On game over:
  - Displays a "Game Over!" message and the **Restart** button.  
- On restart:
  - Resets score, level, and ball speed.  
  - Removes game over message and starts a new session.

---

## **🔧 Prerequisites**
- **Python**: Ensure Python (version 3.6 or later) is installed.  
- **Tkinter**: Included by default with Python; no additional setup required.  

---

## **📂 Installation**

### Clone the repository or download the script:
```bash
git clone https://github.com/PawanRajwar/Catch-the-Ball-Game.git
cd catch-the-ball-game
```

### Run the game:
```bash
python Catch_the_Ball_Game.py
```

---

## **📚 Usage**

1. **Launch the game**:  
   Run the script to start the game. The ball will start falling from the top of the canvas.  

2. **Control the paddle**:  
   Move the mouse horizontally to position the paddle and catch the ball.  

3. **Progress through levels**:  
   Score increases with successful catches. Every 5 points advances the level, and the ball speeds up.  

4. **Restart after Game Over**:  
   If you miss the ball, click the **Restart** button to begin a new session.

---

## **📸 Screenshots**

### 🎮 **Main Gameplay**:
![Game Screenshot](<Screenshot 2024-11-25 122251-1.png>)

### 🔄 **Restart Functionality**:
![Restart Functionality](<Screenshot 2024-11-25 122305-1.png>)


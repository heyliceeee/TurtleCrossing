# 🐢 Turtle Crossing

A mini‑game developed in **Python** using the **Turtle Graphics** module.  
The goal is simple: **help the turtle cross the road** while avoiding cars that move at increasingly higher speeds.

---

## 🎯 Game Objective  
Guide the turtle to the finish line while avoiding collisions with cars.  
With each successful crossing:

- The **level increases**
- The **car speed grows**
- The difficulty becomes higher

---

## 🧠 Main Features  

- **Player movement** using the **Up** key  
- **Random car generation** with varied colors and positions  
- **Progressive speed increase**  
- **Level system** with visual updates  
- **Collision detection**  
- **Game Over message**  
- Modular structure with separate classes:
  - **CarManager**  
  - **Player**  
  - **Scoreboard**  

---

## 🧩 Component Description  

### 🚗 CarManager  
Responsible for:
- Creating random cars  
- Controlling horizontal movement  
- Increasing speed each level  

---

### 🐢 Player  
The turtle controlled by the user:
- Always starts at the initial position  
- Moves upward with the **Up** key  
- Checks if it reached the finish line  
- Returns to the start after each level  

---

### 🧮 Scoreboard  
Displays:
- The current level  
- The **Game Over** message  
- Updated text whenever the level changes  

---

## 📚 Concepts Practiced  

- Object‑oriented programming (OOP)  
- Animation with `screen.tracer()`  
- Collision detection  
- Random generation  
- Code modularization  
- Keyboard events with `onkey()`  

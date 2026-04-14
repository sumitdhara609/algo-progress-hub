# 🚀 Algo Progress Hub

A powerful CLI-based system to **track, organize, and improve your Data Structures & Algorithms journey** through consistent problem solving.

> 💡 Built during high school to develop strong problem-solving discipline and consistency early.

---

## 🌍 Overview

Mastering Data Structures & Algorithms isn’t about solving random problems — it’s about **structured practice and consistency over time**.

**Algo Progress Hub** is designed to act as your personal DSA companion by helping you:

- Track solved problems efficiently  
- Organize them by difficulty, topic, and pattern  
- Maintain a consistent daily practice habit  
- Monitor your growth with meaningful insights  

---

## 🎯 Key Objectives

- 📈 Build long-term consistency in DSA practice  
- 🧠 Strengthen problem-solving and pattern recognition  
- 🗂️ Maintain a structured and organized learning path  
- 🔥 Develop a strong daily coding habit  

---

## ⚙️ Features

- 📌 Add problems with:
  - Difficulty (Easy / Medium / Hard)  
  - Topic (Array, String, etc.)  
  - Pattern (Two Pointer, DP, Hashing, etc.)  
  - Status (Solved / Revision / Unsolved)  
  - Problem link  

- 📋 View problems in a clean **DSA Progress Dashboard**  
- 🔍 Search problems instantly  
- 🗑️ Delete unwanted or incorrect entries  
- 📊 Track progress with detailed statistics  
- 🎯 Set and monitor progress goals (e.g., 100 problems) 
- 🔥 Daily streak tracking system for habit building
- 🎯 Daily goal tracking system
- 💾 JSON-based structured storage  
- ⚡ Fast and minimal CLI experience  

---

## 🧠 How It Works

1. Solve a problem from any platform (e.g., LeetCode)  
2. Add it to the tracker with details  
3. Track your progress and patterns  
4. Stay consistent and improve daily  

👉 This system helps you **learn smarter, not just harder**

---

## 🛠️ Tech Stack

- **Python 🐍**  
- JSON-based storage
- Command Line Interface (CLI) 

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/sumitdhara609/algo-progress-hub.git
```
### 2. Navigate into the project folder
```bash
cd algo-progress-hub
```
### 3. Run the program
```bash
python main.py
```

---

## 💻 CLI Usage
```bash
Enter choice: 1  → Add Problem
Enter choice: 2  → View Dashboard
Enter choice: 3  → Search Problem
Enter choice: 4  → Delete Problem
Enter choice: 5  → View Stats
Enter choice: 6 → Set Daily Goal
Enter choice: 7 → Exit
```

---

# 📂 Additional Information
## 📄 Data Format

Each problem is stored in structured JSON format:
```json
{
"name": "string",
"difficulty": "Easy | Medium | Hard",
"topic": "string",
"pattern": "string",
"status": "Solved | Revision | Unsolved",
"link": "string"
}
```
Example:
```json
{
"name": "Trapping Rain Water",
"difficulty": "Hard",
"topic": "Array",
"pattern": "Two Pointer",
"status": "Unsolved",
"link": "https://leetcode.com/problems/trapping-rain-water/"
}
```
## 🌟 Why This Project?

Most students solve problems randomly and lose track of their progress.

### Algo Progress Hub solves that by turning practice into a structured system, helping you:

- Stay organized
- Stay consistent
- See real improvement over time

## 📌 Future Improvements

- ⚡ CLI commands using argparse
- 🌐 Web dashboard (Flask / React)
- 📊 Graph-based analytics
- 🔗 LeetCode API integration

## 👤 Author & License

**Author:** Sumit Dhara

This project is open-source under the  **MIT License.**

#### © 2026 Sumit Dhara. All rights reserved.

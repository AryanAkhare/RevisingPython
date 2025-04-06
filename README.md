# Revising Python 🐍

A structured and practical Python repository by [Aryan Akhare](https://github.com/AryanAkhare) that covers:

- ✅ Core fundamentals 
- 🧠 Problem-solving scripts
- 🎮 Small projects
- 🌦 A deployed **Flask-based Weather App**

---

## 📁 Folder Structure

```
RevisingPython/
│
├── Fundamentals/
│   ├── FileOperations/
│   ├── Less21/
│   ├── Basics.py
│   ├── classes.py
│   ├── Closure.py
│   ├── dictionaries.py
│   ├── exceptions.py
│   ├── fstrings.py
│   ├── Functions.py
│   ├── Lambda.py
│   ├── ListandTuples.py
│   ├── Loops.py
│   ├── modules.py
│   ├── Recursion.py
│   ├── scope.py
│   ├── script.py
│   └── Strings.py
│
├── Problem Solving/
│
├── SmallProjects/
│   ├── Arcade/
│   ├── BankAccOops/
│   ├── GuessingNumber/
│   ├── RockPaperScissors/
│   └── WeatherApp/
│       ├── app.py
│       ├── requirements.txt
│       └── templates/
│
└── README.md
```

---

## 🌦 Weather App — Built with Flask

This project fetches weather data for any city using an API and displays it in a clean, user-friendly interface.

🔗 **Live Demo**: [weather-app-va3q.onrender.com](https://weather-app-va3q.onrender.com)

### 🚀 Deploy & Run Instructions

1. **Fork the repo**

   [https://github.com/AryanAkhare/RevisingPython](https://github.com/AryanAkhare/RevisingPython)


2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # Windows: venv\Scripts\activate
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```
4. **Navigate to the Weather App directory**

   ```bash
   cd RevisingPython/SmallProjects/WeatherApp
   ```

5. **Run the app locally**

   ```bash
   python app.py
   ```

6. **To deploy on Render:**
   - Add the repo
   - Set **Start Command** to `python app.py`
   - Add **Build Command**: `pip install -r requirements.txt`
   - Set environment to Python and expose the correct port

---

## 📚 Learning Reference

This repo was revised with help from [freeCodeCamp](https://www.youtube.com/c/Freecodecamp)'s Python crash courses and project ideas.

---

## 🙌 Author

Made with ❤️ by Aryan Akhare  
🔗 [GitHub](https://github.com/AryanAkhare)

---
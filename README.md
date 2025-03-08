# Password Strength Checker 

This repository contains a **Password Strength Checker** tool that assesses the strength of passwords entered by users. The tool analyzes various factors such as **length**, **complexity**, and **uniqueness** to provide feedback on password strength.

---

## About the Project

This is the second task of my internship project, where I built a **Password Strength Checker**. The tool evaluates the strength of passwords by checking:
- **Length** of the password
- **Character diversity** (uppercase, lowercase, numbers, special characters)
- **Uniqueness** (whether the password contains common or easily guessable patterns)

It provides feedback to help users improve weak passwords and create more secure ones.

---

## Technologies Used

- **Python**: The script is written in Python 3.x.
- **Regular Expressions (regex)**: Used to match character patterns for complexity checks.
- **String Module**: Used for special characters in complexity checks.

---

## Features

- **Length check**: Ensures the password is between 8 and 20 characters long.
- **Complexity check**: Verifies if the password contains:
  - At least one **uppercase letter**
  - At least one **lowercase letter**
  - At least one **number**
  - At least one **special character**
- **Uniqueness check**: Detects common and easily guessable patterns (e.g., "1234", "password", "sagar123").
- **Concise feedback**: Provides short and actionable feedback about the strength of the password.

---

## How to Run the Code

### Prerequisites:
1. Python 3.x should be installed on your machine.
   - If Python is not installed, download and install it from [Python's official website](https://www.python.org/downloads/).



num1 = int(input("Enter the first value = "))
num2 = int(input("Enter the second value = "))
operation = input("Give operation (+, -, *, /): ")

if operation == "+":
    print(f"Addition of two values is {num1 + num2}")
elif operation == "-":
    print(f"Subtraction of two values is {num1 - num2}")
elif operation == "*":
    print(f"Multiplication of two values is {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Division of two values is {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Error: Invalid operation.")

print("That's your answer.")


readme ='''# calculator.py
# Python Calculator

A simple Python program that performs basic arithmetic operations: **Addition, Subtraction, Multiplication, and Division**.

---

## Features
- Takes two numbers as input from the user
- Supports operations: `+`, `-`, `*`, `/`
- Handles division by zero with an error message

---

## How to Run
1. Make sure you have Python installed (Python 3 recommended).
2. Open a terminal or command prompt.
3. Run the program:
   ```bash
   python calculator.py'''

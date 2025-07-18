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
# End of calculator.py

# Calculator.py

'''A simple command-line calculator written in Python.

## Features
- Addition, Subtraction, Multiplication, Division
- Handles division by zero with an error message
- User-friendly input prompts

## How to Run
1. Make sure you have Python 3 installed.
2. Open a terminal and navigate to the project folder.
3. Run the calculator with:
   ```bash
   python calculator.py
   ```

## Example Usage
```
Enter the first value = 10
Enter the second value = 5
Give operation (+, -, *, /): /
Division of two values is 2.0
That's your answer.'''


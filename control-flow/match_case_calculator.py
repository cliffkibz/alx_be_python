#!/usr/bin/env python3
"""
match_case_calculator.py
Simple calculator using Python's match‑case (requires Python 3.10+).
"""


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
      
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
       
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
	else:
            result = num1 / num2
          
    case _:
        print(Invalid operation!")

print(f"The result is {result}")

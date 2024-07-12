import math


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not possible!")
    else:
        return num1 / num2


def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
#!/usr/bin/env python3

def admin_login(username, password):
    if username == ("admin")or("ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
    pass
admin_login("ADMIN", "12345")
def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    
    pass
hows_the_weather(50)


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
    pass

fizzbuzz(15)
def calculator(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    pass

calculator("add", 5, 3)

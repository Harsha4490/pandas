import math

# Function Definitions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        return "Error! Square root of negative number is not possible."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error! Factorial of negative number is not possible."
    return math.factorial(int(a))


# Main Program
while True:
    print("\n******** CALCULATOR ********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 10:
        print("Thank You!")
        break

    elif choice in [1, 2, 3, 4, 5, 6]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(a, b))
        elif choice == 2:
            print("Result =", subtract(a, b))
        elif choice == 3:
            print("Result =", multiply(a, b))
        elif choice == 4:
            print("Result =", divide(a, b))
        elif choice == 5:
            print("Result =", modulus(a, b))
        elif choice == 6:
            print("Result =", power(a, b))

    elif choice == 7:
        a = float(input("Enter number: "))
        print("Result =", square(a))

    elif choice == 8:
        a = float(input("Enter number: "))
        print("Result =", square_root(a))

    elif choice == 9:
        a = int(input("Enter number: "))
        print("Result =", factorial(a))

    else:
        print("Invalid Choice!")

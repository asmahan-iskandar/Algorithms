# FUNCTIONS 

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def linear_search(numbers, target):
    for num in numbers:
        if num == target:
            return True
    return False


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def login():
    username = "Salem"
    password = "12345"
    user = input("Enter username: ")
    pw = input("Enter password: ")

    if user == username and pw == password:
        print("Login successful!\n")
        return True
    else:
        print("Access denied. Please try again.\n")
        return False


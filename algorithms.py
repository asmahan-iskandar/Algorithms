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


# MAIN PROGRAM 
logged_in = False

while True:
    print("\nChoose an option:")
    print("1. Factorial")
    print("2. Find Max")
    print("3. Linear Search")
    print("4. Fibonacci")
    print("5. Login")
    print("6. Exit")

    choice = input("Enter your option: ")

    if choice == "1":
        if not logged_in:
            print("Please login first.")
            continue
        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))

    elif choice == "2":
        if not logged_in:
            print("Please login first.")
            continue
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        print("Max number:", find_max(nums))

    elif choice == "3":
        if not logged_in:
            print("Please login first.")
            continue
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        target = int(input("Enter number to search: "))
        print("Found:", linear_search(nums, target))

    elif choice == "4":
        if not logged_in:
            print("Please login first.")
            continue
        n = int(input("Enter n for Fibonacci: "))
        print("Fibonacci number:", fibonacci_iterative(n))

    elif choice == "5":
        logged_in = login()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")
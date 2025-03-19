def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error: The second number must be greater than or equal to the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'X':
            print("Exiting program.")
            break
        
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid integers.")
            continue
        
        if choice == 'D':
            result = divide(a, b)
        elif choice == 'E':
            result = exponentiation(a, b)
        elif choice == 'R':
            result = remainder(a, b)
        elif choice == 'F':
            result = summation(a, b)
        else:
            print("Invalid choice. Please select a valid operation.")
            continue
        
        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()

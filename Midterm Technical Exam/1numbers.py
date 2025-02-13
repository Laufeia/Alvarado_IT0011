import os

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "numbers.txt")

with open(file_path, "r") as file:
    line_number = 1
    for line in file:
        line = line.strip()
        if not line:
            continue
        try:
            numbers = [int(x.strip()) for x in line.split(",") if x.strip()]
        except ValueError:
            print(f"Line {line_number}: {line} - Invalid number found!")
            line_number += 1
            continue
        total = sum(numbers)
        result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
        print(f"Line {line_number}: {line} (sum {total}) - {result}")
        line_number += 1

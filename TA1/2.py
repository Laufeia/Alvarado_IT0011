text = input("Enter a string with numbers: ")
total = 0 

for char in text:
    if char.isdigit():
        total += int(char)

print("Sum of digits:", total)
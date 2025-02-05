n = 5 

for i in range(1, n + 1):
    spaces = " " * (n - i)
    numbers = "" 

    for num in range(1, i + 1):
        numbers += str(num)

    print(spaces + numbers)
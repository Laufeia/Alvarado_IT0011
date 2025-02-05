x=4
while x >= 1:
    if x % 4 == 0:
        print("party")
    elif x - 2 < 0:
        print("cake")
    elif x / 3 == 0:
        print("greeting")
    else:
        print("birthday")
        x=x-1
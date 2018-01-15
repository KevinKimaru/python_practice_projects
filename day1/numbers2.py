x = 0
while x <= 100:
    if x % 7 == 0 and x % 11 == 0:
        print("Kenya yetu")
    elif x % 11 == 0:
        print("Kenya")
    elif x % 7 == 0:
        print("Kevin")

    else:
        print(x)
    x += 1
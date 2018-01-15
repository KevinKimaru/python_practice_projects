# x = 1
# while x <= 10:
#     print(x)
#     x += 2
#
# x = 0
# while x <= 10:
#     print(x)
#     x += 2
#
#
#
# x = 0
# while x <= 10:
#     if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
#         print(x)
 #   x +=1




while True:
    no3 = input("Enter a number: ")
    no3 = int(no3)
    count = 0
    test = 1
    while test <= no3:
        if no3 % test == 0:
            count += 1
        test += 1

    if count < 3:
        print(str(no3) + " is a prime number")
    else:
        print(str(no3) + " is not a prime number")

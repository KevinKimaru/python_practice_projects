# while True:
#     age = input("Enter your age: ")
#     if age == 'DONE' :
#         break
#     age = int(age)
#
#
#     if age < 5:
#         print ("This is a toddler: " + str(age))
#     elif age >= 6 and age <= 12:
#         print("This is a kid: " + str(age))
#     elif age >= 13 and age <= 20:
#         print("This is a teenager: " + str(age))
#     elif age >= 21 and age <= 35:
#         print("This is a youth: " + str(age))
#     elif age >= 36 and age <= 55:
#         print("This is middle age: " + str(age))
#     else:
#         print("This is a senior citizen: " + str(age))

count = 0
sum = 0
while True:
    marks = input("Enter your marks: ")
    if marks == "AVG":
        break
    marks = int(marks)
    sum += marks
    count += 1
avg = sum/count
print( "Your total score is: " + str(sum))
print( "Your average is: " + str(avg))











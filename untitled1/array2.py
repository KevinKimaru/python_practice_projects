scores = [34, 56, 56, 78, 74, 23, 45, 12, 25, 12, 90, 12, 47, 90]

total = 0
for mark in scores:
   # print(mark)
    total += mark

count = len(scores)
avg = total/count

print("Average is " + str(avg))

print("The average is {0} of this total {1}".format(avg, total))

count = 0
for mark in scores:
    if mark % 2 == 0:
        print(mark)


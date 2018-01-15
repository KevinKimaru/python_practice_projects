import math
#from math import sqrt, pow, cos
from classes_account import Account as BankAccount



def largest (num1, num2, num3, num4):
    numbers = [num1, num2, num3, num4]
    numbers.sort()
    return numbers[3]

def area_equilateral(side):
    area = math.sqrt(3) / 2 * math.pow(side, 2)
    return area

#optionals
def sayMyNames(firstname, secondName = "Joe", thirdName = "Kim"):
    print(firstname + " " + secondName + " " + thirdName)

acc1 = BankAccount("Kevin Chege", 25326, 600000)
acc1.printDetails()
acc1.deposit(500)
acc1.withdraw(70000000)
acc1.withdraw(2300)


# sayMyNames("Kevin")
# sayMyNames("John", secondName="Mark")
# sayMyNames("Mary", thirdName="Hellen")
# sayMyNames("Gregory", secondName="Isaac", thirdName="Jean")

#print(area_equilateral(17))

# num = largest(23, 786, 78, 10)
# print(num)
# print(num**2)





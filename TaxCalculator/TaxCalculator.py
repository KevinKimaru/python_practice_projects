salary = input("Enter your salary: ")
#print(type(salary))
salary=int(salary)
if salary <= 11180:
    taxCharged = 0.1 * salary
elif salary <= 21714:
    taxCharged = 0.15 * salary
elif salary <= 32248:
    taxCharged = 0.2 * salary
elif salary <= 42782:
    taxCharged = 0.25 * salary
else:
    taxCharged = 0.3 * salary

print ("Tax charged:")
print(taxCharged)
netIncome = salary - taxCharged
print ("netIncome:")
print(netIncome)


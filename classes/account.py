class Account:

    name =  ""
    accNumber = 0
    balance = 0
    def __init__(self, name, accNumber, balance):
        print("Account was Created")
        self.name = name
        self.accNumber = accNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print( "Deposited KES {0}. New balance is {1}".format(amount, self.balance) )

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance . %s" %(self.balance))
        else:
            self.balance-=amount
            print( "Withdrawn KES {0}. New balance is {1}".format(amount, self.balance) )

    def printDetails(self):
        print("Name: {0} Account Number: {1} Balance: {2}".format(self.name, self.accNumber, self.balance))

maryAc = Account("Mary Joe", 3134, 26478)
janeAc = Account("Jane Njogu", 7789, 67524)

maryAc.withdraw(700)
maryAc.printDetails()
maryAc.deposit(976)

print("==================================================\n\n\n")
peris = Account("Peris Wangari", 67898009, 0);
peris.printDetails()

peris.deposit(100)
peris.deposit(200)
peris.withdraw(500)
peris.withdraw(250)
peris.printDetails()


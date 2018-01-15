def add(a, b):
    result = a + b
    print(result)

def multiply(a, b):
    result = a * b
    print(result)

def converter(amount, currency):
    if currency == "USD":
        dollars = amount/104
        print("{0} KES is {1} Dollars".format(amount, dollars))
    elif currency == "GBP":
        pounds = amount / 130
        print("{0} KES is {1} Pounds".format(amount, pounds))
    elif currency == "EUR":
        euro = amount / 115
        print("{0} KES is {1} Euros".format(amount, euro))
    elif currency == "TSH":
        tz_sh = amount * 25
        print("{0} KES is {1} Tanzanian Shillings".format(amount, tz_sh))
    elif currency == "USH":
        ug_sh = amount / 104
        print("{0} KES is {1} Uganda Shillings".format(amount, ug_sh))
    else:
        print("Unknown Currency " + currency)

converter(10000, "USD")
converter(34670, "USH")
converter(9577, "GH")
converter(34267, "EUR")
converter(1000000000, "GBP")
converter(65293333387, "TSH")


# add(23, 45)
# add(11, 45)
# add(23, 400)
# multiply(56, 90)
# multiply(5, 80)
# multiply(6, 45)
# multiply(67, 56)
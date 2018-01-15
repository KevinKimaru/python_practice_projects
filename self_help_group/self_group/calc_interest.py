
def calculate_interest(amount):
    result = amount * 10//100
    if (result % 5) != 0:
        stringResult = str(result)

        if stringResult[-1] == '1':
            result = int(stringResult) - 1
        elif stringResult[-1] == '2':
            result = int(stringResult) - 2
        elif stringResult[-1] == '3':
            result = int(stringResult) - 3
        elif stringResult[-1] == '4':
            result = int(stringResult) - 4
        elif stringResult[-1] == '6':
            result = int(stringResult)  -1
        elif stringResult[-1] == '7':
            result = int(stringResult) - 2
        elif stringResult[-1] == '8':
            result = int(stringResult) - 3
        elif stringResult[-1] == '9':
            result = int(stringResult) - 4
        elif stringResult[-1] == '10':
            result = int(stringResult) - 5

    return result

print(calculate_interest(235474))
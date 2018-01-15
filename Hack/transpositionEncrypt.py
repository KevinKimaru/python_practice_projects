#======================
mList = []
for i in range(10):
    mList = mList + [i]
print(mList)
print("\n")

mList = list(range(10))
print(mList)
print("\n")

mList = list("Hello World")
print(mList)
print("\n")

mString = "Hello world"
mString = mString[:6] + 'x' + mString[7:]
print(mString)
print("\n")

mString = "hello world"
print('o' in mString)
print("\n")

mList = list(range(10))
print(1 in mList)
print("\n")
#======================

def main():
    message = 'Common Sense is not so common. '
    key = 8

    cipherText = encryptMessage(key, message)
    # Print the encrypted string in ciphertext to the screen, with a | (called "pipe" character)
    #  after it in case there are spaces at 14.  the end of the encrypted message.
    print(cipherText + '|')

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    cipherText = [''] * key

    # Loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the current column in the ciphertext list.
            cipherText[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(cipherText)

 # If transpositionEncrypt.py is run (instead of imported as a module) call the main() function.
if __name__ == '__main__':
    main()
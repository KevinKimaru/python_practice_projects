import pyperclip

#message to be encripted
message = 'This is my secret message 12345'

#encryption/decryption key
key = 13

# tells the program to encrypt or decrypt
mode = 'encrypt'

#Every possible symbol that can be encrypted
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`a bcdefghijklmnopqrstuvwxyz{|}~'

#Stores the encrypted /decrypted form of the message
translated = ''

#capitalize the string in message
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)#get the number of the symbol
        if mode == 'encrypt':
            num = num + key
            # if num is larger than the length of letters
            if num >= len(LETTERS):
                num = num - len(LETTERS)
        elif mode == 'decrypt':
            num = num - key
            #if less than 0
            if num < 0:
                num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)
def translate():
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    return translated
message = input('Enter Message: ')
encrypt = translate()
print(encrypt)
print ("\n encrypted to: \n")
message = encrypt
decrypt = translate()
print(decrypt)
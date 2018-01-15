alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = 9
def encrypt (message):
    encrypted = ''
    for symbol in message:
        if symbol in alphabet:
            num = alphabet.find(symbol)
            num = (num + key) % len(alphabet)
            encrypted = encrypted + alphabet[num]
        else:
            encrypted = encrypted + symbol
    return encrypted

message = input("Enter your message:")
print("Encryption is: %s" %(encrypt(message)))


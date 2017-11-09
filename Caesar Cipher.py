#U means the upper case aplhabets
#L means the lower case aplhabets
key = 'abcdefghijklmnopqrstuvwxyz'
key1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext = str(input("Enter a message:"))
n = int(input("Enter a num:"))

def encryptL(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''
    
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decryptL(n,ciphertextL):
    """Decrypt the Cipher text and return the Plaintext"""
    
    result = ''

    for l in ciphertextL.lower():
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def encryptU(n, plaintext):
    """Encrypt the string and return the ciphertext all in the uppercase letters"""
    result = ''
    
    for l in plaintext.upper():
        try:
            i = (key1.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.upper()

def decryptU(n,ciphertextU):
    """Decrypt the Cipher text and return the Plaintext all in the uppercase letters"""
    
    result = ''

    for l in ciphertextU.upper():
        try:
            i = (key1.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.upper()

ciphertextL = encryptL(n,plaintext)
ciphertextU = encryptU(n,plaintext)
print("Encrypted Text in Lower Case:",encryptL(n,plaintext))
print("Decrypted Text in Lower Case:",decryptL(n,ciphertextL))
print("Encrypted Text in Upper Case:",encryptU(n,plaintext))
print("Decrypted Text in Upper Case:",decryptU(n,ciphertextU))

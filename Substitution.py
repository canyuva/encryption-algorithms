alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
my_alphabet = "/*-+?*$#%&/()[]'!.,@;~<>|´`^éX"

def existsDigit(msg):
    for i in msg:
        if i.isdigit():
            return True
    return False

def getMessage():
    msg = input('Enter the message :')
    if existsDigit(msg):
        return 'err'
    else:
        return msg

def encrypt(msg):
    msg = str.lower(msg)
    encrypted = ''
    for letter in msg:
        index = alphabet.index(letter)
        encrypted+=my_alphabet[index]
    return encrypted

def decrypt(encrypted):
    decrypted = ''
    for letter in encrypted:
        index = my_alphabet.index(letter)
        decrypted+=alphabet[index]
    return decrypted

def main():
    print('163301015 - Bekir Can YUVA\nSubstitution\n\nEncryption or Decryption ?\n1- Encryption\n2- Decryption')
    selection = input('Selection : ')
    if selection == '1':
        msg = getMessage()
        encrypted = encrypt(msg)
        print(encrypted)
    elif selection == '2':
        msg = getMessage()
        decrypted = decrypt(msg)
        print(decrypted)
    else:
        print('Please enter a valid value')

main()


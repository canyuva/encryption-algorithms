MAX_KEY = 29
alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY):
            return key

def existsDigit(msg):
    for i in msg:
        if i.isdigit():
            return True
    return False

def getMessage():
    msg = input('Enter the message :')
    if existsDigit(msg):
        return 'Please do not type digits'
    else:
        return msg

def encrypt(msg,key):
    msg = str.lower(msg)
    encrypted = ''
    for letter in msg:
        index = msg.index(letter)
        encrypted+=alphabet[(index+int(key))%len(alphabet)]
    return encrypted

def decrypt(encrypted,key):
    decrypted = ''
    for letter in encrypted:
        index = encrypted.index(letter)
        decrypted+=alphabet[(index-key)%len(alphabet)]
    return decrypted
        
def main():
    print('163301015 - Bekir Can YUVA\nCaesar\n\nEncryption or Decryption ?\n1- Encryption\n2- Decryption')
    selection = input('Selection : ')
    if selection == '1':
        msg = getMessage()
        key = getKey()
        encrypted = encrypt(msg,key)
        print(encrypted)
    elif selection == '2':
        msg = getMessage()
        key = getKey()
        decrypted = decrypt(msg,key)
        print(decrypted)
    else:
        print('Please enter a valid value')

main()
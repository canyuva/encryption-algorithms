alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
ALPHABET_SIZE = len(alphabet)

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

def encrypt(msg,a,b):
    msg = str.lower(msg)
    encrypted = ''
    for letter in msg:
        index = alphabet.index(letter)
        new_index = (int(a) * index + int(b))%ALPHABET_SIZE
        encrypted+=alphabet[new_index]
    return encrypted

def decrypt(msg,a,b):
    msg = str.lower(msg)
    decrypted = ''
    for letter in msg:
        z = int((ALPHABET_SIZE+1)/a)
        index = (alphabet.index(letter))
        new_index = ((index-5)*z)%ALPHABET_SIZE
        decrypted+=alphabet[int(new_index-1)]
    return decrypted

def main():
    print('163301015 - Bekir Can YUVA\nAffine\n\nEncryption or Decryption ?\n1- Encryption\n2- Decryption')
    selection = input('Selection : ')
    if selection == '1':
        msg = getMessage()
        a = input('Enter a valid a value')
        b = input('Enter b valid a value')
        encrypted = encrypt(msg,a,b)
        print(encrypted)
    elif selection == '2':
        msg = getMessage()
        a = input('Enter a valid a value')
        b = input('Enter b valid a value')
        decrypted = decrypt(msg,a,b)
        print(decrypted)
    else:
        print('Please enter a valid value')

main()
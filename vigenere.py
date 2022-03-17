# Vigenere Cipher
import re

# initialize everything to empty strings
plaintext = ""
key = ""
keystream = ""
encryptedMessage = ""
decryptedMessage = ""

# the cipher will not be case sensitive and it will not accept numbers or special characters
alphabet = 'abcdefghijklmnopqrstuvwxyz'
special_char = re.compile("[@_!#$%^&*()<>?/\|}{~:`']")

# change color of the text in terminal for aesthetic purposes
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   LIGHTPURPLE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# checks if numbers exist in the plaintext or key
def numExists(text):
    return any(i.isdigit() for i in text)

# gets input from user and initializes the plaintext and key used for encryption
def initializeTerms(term):
    while True:
        # initialize current term and conditions to test for
        current = ""
        noSpecialChar = True
        noNums = True

        print()
        if term == 1:
            current = input(color.LIGHTPURPLE + color.BOLD + "Enter the plaintext: " + color.END)
        elif term == 2:
            current = input(color.LIGHTPURPLE + color.BOLD + "Enter the key: " + color.END)

        # checks for special characters
        if(special_char.search(current) != None):
            noSpecialChar = False
        # checks for numbers
        if(numExists(current) != False):
            noNums = False
        if current and noSpecialChar and noNums:
            break
    # not case sensitive therefore everything is converted to lowercase
    return current.lower()

# generate keystream using plaintext and key
def generateKeystream(plaintext, key):
    if len(plaintext) == len(key):
        return key
    else:
        keystreamList = []
        x = 0
        # key is appended to keystream in a circular manner if the plaintext length != key length
        for i in range(len(plaintext)):
            if plaintext[i] != " ":
                keystreamList.append(key[x])
                x += 1
                # reached the end of the key so reset x to 0 and start at the beginning
                if x == len(key):
                    x = 0
            else:
                # whitespaces are allowed
                keystreamList.append(" ")

        return ("".join(keystreamList))

# encrypt the plaintext
def encrypt(plaintext, keystream):
    encrypted_text = ""
    # formula for encryption is E[i] = (P[i] + K[i]) % 26
    for i in range(0, len(plaintext)):
        if plaintext[i] == " ":
            encrypted_text += " "
        else:
            value = ((alphabet.find(plaintext[i]) + alphabet.find(keystream[i])) % 26)
            encrypted_text += alphabet[value]

    return encrypted_text

# decrypt the encrypted message
def decrypt(encrypted_text, keystream):
    decrypted_text = ""
    # formula for decryption is D[i] = (E[i] - K[i]) % 26
    for i in range(0, len(encrypted_text)):
        if encrypted_text[i] == " ":
            decrypted_text += " "
        else:
            value = ((alphabet.find(encrypted_text[i]) - alphabet.find(keystream[i])) % 26)
            decrypted_text += alphabet[value]

    return decrypted_text

# prompts user for a yes or no answer based on the question
def promptAnswer(question):
    answer = ""
    while True:
        if question == "write":
            answer = input(color.CYAN + color.BOLD + "\nWrite the encrypted message to a file? [Y]es / [N]o : " + color.END)
        elif question == "open":
            answer = input(color.CYAN + color.BOLD + "\nOpen and read the file? [Y]es / [N]o : " + color.END)
        elif question == "decrypt":
            answer = input(color.LIGHTPURPLE + color.BOLD + "\nDecrypt the message? [Y]es / [N]o : " + color.END)
        elif question == "new":
            answer = input(color.LIGHTPURPLE + color.BOLD + "\nEncrypt another message? [Y]es / [N]o : " + color.END)

        # break only if a valid answer is given
        if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
            break
    return answer

# performs the cipher by initializing, encrypting, and decrypting the text
# includes the option to write the encrypted text to a file
def cipher():
    while True:
        # prompt user for plaintext and key to form the keystream
        ptext = 1
        ktext = 2
        plaintext = initializeTerms(ptext)
        key = initializeTerms(ktext)
        keystream = generateKeystream(plaintext, key)
        # encrypt and decrypt the message using the keystream
        encryptedMessage = encrypt(plaintext, keystream)
        decryptedMessage = decrypt(encryptedMessage, keystream)

        # writes encrypted message to a file
        writeAnswer = promptAnswer("write")
        if writeAnswer ==  'Y' or writeAnswer == 'y':
            # create file and append encrypted text to file
            f = open("encryptedMessage.txt", "w")
            f = open("encryptedMessage.txt", "a")
            f.write("ENCRYPTED TEXT: " + encryptedMessage)
            f.write("\nKEY: " + key)
            f.close()
            print()
            print(color.YELLOW + color.BOLD + "ENCRYPTED TEXT WRITTEN TO encryptedMessage.txt" + color.END)

            # open and read file contents
            readFile = promptAnswer("open")
            if readFile == 'Y' or readFile == 'y':
                print()
                f = open("encryptedMessage.txt", "r")
                print(f.read())
        else:
            # print encrypted text if user does not want it written to a file
            print(color.YELLOW + color.BOLD + "\nENCRYPTED TEXT: " + color.END, encryptedMessage)
    
        # prints the decrypted message 
        decryptMsg = promptAnswer("decrypt")
        if decryptMsg ==  'Y' or decryptMsg == 'y':
            print(color.YELLOW + color.BOLD + "\nDECRYPTED TEXT: " + color.END, decryptedMessage)

        # continue to encrypt messages or quit
        encryptAgain = promptAnswer("new")
        if encryptAgain ==  'Y' or encryptAgain == 'y':
            cipher()
        elif encryptAgain ==  'N' or encryptAgain == 'n':
            quit()

print(color.DARKCYAN + "---------------------------------" + color.END)
print(color.LIGHTPURPLE + color.BOLD +"         V I G E N È R E        " + color.END)
print(color.LIGHTPURPLE + color.BOLD +"           C I P H E R          " + color.END)
print(color.DARKCYAN + "---------------------------------" + color.END)
cipher()
# Vigenère Cipher

### A mini program written in Python to learn more about Cryptography and encryption methods.
The Vigenère Cipher is a substitution cipher used for data encryption. The goal of the cipher is to avoid being susceptible to brute force and letter frequency analysis. To do this, the Vigenère Cipher consists of several Caesar Ciphers in sequence with different shift values based on a keyword, instead of just one key.

### Visual example of how the cipher works by RealPython 
![](https://files.realpython.com/media/vigerene-cipher-steps.66057bb0979f.gif)

### Running the program
Download ```vigenere.py``` and open a command-line. To run the program, type in the following: ``` python3 vigenere.py ``` 

### Implementing the cipher
This program takes in input for the plaintext and key, allowing whitespaces, but rejecting any input that contains special characters or numbers. A keystream is created by appending the characters of the key to a string in a circular manner until it is the same length as the plaintext. To encrypt the plaintext, the formula ```Encrypted[i] = (Plaintext[i] + Keystream[i]) % 26``` is used. The formula to decrypt the encrypted text is ```Decrypted[i] = (Encrypted[i] - Keystream[i]) % 26```. Users have the option to write the encrypted text to a file called ```encryptedMessage.txt``` which will be saved to their local machine. This file includes both the encrypted text and the key.

### Example of the program running
![](https://i.imgur.com/JVJsAfi.gif)

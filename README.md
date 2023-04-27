# Os-labproject
Ransomware using multithreading


Theory of the project

File encryption using AES CBC (Advanced Encryption Standard - Cipher Block Chaining) mode encryption is a widely used method for securing sensitive data. AES is a symmetric encryption algorithm, meaning that the same key is used for both encryption and decryption. CBC mode is a block cipher mode of operation that adds a level of security by chaining the encrypted blocks together. 

Multithreading is a programming technique that allows a single program to execute multiple threads concurrently. In the context of file encryption, multithreading can be used to improve performance by allowing multiple threads to encrypt different parts of the file simultaneously. This can significantly reduce the overall time required to encrypt a large file.

To implement file encryption using AES CBC mode encryption and multithreading, the following steps can be taken:

1. Divide the file into smaller blocks: The file to be encrypted is divided into smaller blocks of a fixed size. The size of the blocks should be chosen based on the available memory and the processing power of the system.

2. Generate a random initialization vector (IV): An initialization vector is a random value that is used to initialize the encryption algorithm. The IV is XORed with the first block of plaintext before encryption, adding an additional level of randomness and security to the encryption process.

3. Generate a random encryption key: A random encryption key is generated using a secure random number generator. This key is used to encrypt and decrypt the file.

4. Encrypt the file using AES CBC mode encryption: Each block of the file is encrypted using the AES CBC mode encryption algorithm with the encryption key and IV. The encrypted blocks are then chained together in the order they were encrypted to form the ciphertext.

5. Implement multithreading: The encryption process can be divided into multiple threads, with each thread responsible for encrypting a separate block of the file. The number of threads should be chosen based on the available hardware resources.

6. Save the encrypted file: The encrypted file is saved along with the IV and the encryption key. These values will be needed to decrypt the file later.

To decrypt the file, the following steps can be taken:

1. Read the encrypted file: The encrypted file, along with the IV and encryption key, is read from disk.

2. Decrypt the file using AES CBC mode decryption: Each block of the encrypted file is decrypted using the AES CBC mode decryption algorithm with the encryption key and IV. The decrypted blocks are then chained together in the order they were decrypted to form the plaintext.

3. Save the decrypted file: The decrypted file is saved to disk.

In conclusion, file encryption using AES CBC mode encryption and multithreading is an effective way to secure sensitive data. By dividing the encryption process into multiple threads, the performance can be significantly improved, allowing for faster encryption and decryption of large files.


Features:

➢ File encryption with custom extension a multi-threaded(and decryption when the key is supplied)
➢ Obfuscation
➢ Keylogger



Implementation:
 •  	Firstly, I start with key generation, listing files, encrypting files with a key, and sending key to the server.   
•  	Warning Screen containing timer payment details and takes decryption key input using Tkinter.
•  	Add a keylogger using pynput, which sends log packets to the attacker’s server.
•  obfuscation.
 
TechStack:
     Ransomware:
1)   Python
2)   Tkinter
3)   Pyarmor, threading
4)   pynput, pycryptodome
5)   pyinstaller
	Web Server:
		1)   HTML,CSS,JAVASCRIPT
    2)   Flask

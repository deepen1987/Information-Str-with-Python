# Implementation of Encryption and Decryption of data using Synchronous cryptography. 
Description - The project is about the encryption or decryption of a message or a file using an 8-character alpha numeric key. I have implemented the concept of Synchronous cryptography using bit wise manipulation of data. The program takes in a message or a file and based on key provided, does bit wise manipulation to transform the data in non-human readable form. To decrypt the message or the file user needs to provide the same key which was used to encrypt them. This way only those users can decrypt the data who have the key. As part of this project I have implemented support only for .txt files.

*The Project has 5 options.*

### Options
* Encrypt a Message.
  * Enter a key to encrypt message.
  * Enter the message to be encrypted.
  * Provide the file name to save the encrypted data.
* Encrypt a File.
  * Enter a key to encrypt message.
  * Enter the file name to encrypt
  * Provide the file name to save the encrypted data.
* Decrypt a Message. 
  * Enter a key to decrypt message. They should be same as the one used to encrypt it.
  * Enter the message to be decrypted.
  * Provide the file name to save the decrypted data.
* Decrypt a File.
  * Enter a key to decrypt message. They should be same as the one used to encrypt it.
  * Enter the file name which has encrypted data.
  * Provide the file name to save the decrypted data.
* Exit

### Technology
* Python 3.9

### Instructions to run the program:  
  1. Download the project folder.  
  2. Using the command prompt, go to project directory.  
  3. Run python crypto.py 
  4. Only Supports .txt file format.

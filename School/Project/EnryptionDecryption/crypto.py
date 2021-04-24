import os


class Crypto:
    def __init__(self, passcode):
        self.passcode = 0
        for i in passcode:
            self.passcode = self.passcode + ord(i)

    def encrypt(self, msg):

        new_message = ""
        for i in range(len(msg)):
            new_message += str(ord(msg[i]) << self.passcode)
            if i != (len(msg) - 1):
                new_message += "@"
        return new_message

    def decrypt(self, msg):

        new_message = ""
        array_message = msg.split("@")

        for i in array_message:
            if i.isdigit():
                new_message += chr(int(i) >> self.passcode)
            else:
                print(
                    "No Encryption found for the message or file please enter a valid message or file to be decrypted.")
                return None
        return new_message


def file_name_verify(name):
    if name[-1:-5:-1] == "txt.":
        return True
    else:
        return False


def menu(user_input):
    k = input("Enter a 8 character key: ")
    while len(k) != 8:
        k = input("Please Enter a 8 character key only: ")

    encrypt_decrypt = Crypto(k)

    if user_input == 1:
        message = input("Please enter the message to be encrypted: ")
        message = encrypt_decrypt.encrypt(message)

        f_name = True
        while f_name:
            file_name = input("Enter a filename to save the message: ")
            if file_name_verify(file_name):
                if os.path.isfile(file_name):
                    with open(file_name, 'w') as f:
                        f.write("")
                        f.write(message)
                        f_name = False
                else:
                    if file_name_verify(file_name):
                        with open(file_name, 'w') as f:
                            f.write("")
                            f.write(message)
                            f_name = False

    if user_input == 2:

        f_name = True
        while f_name:
            input_file_name = input("Enter a filename with extension: ")
            if file_name_verify(input_file_name):
                if os.path.isfile(input_file_name):
                    with open(input_file_name, 'r') as f:
                        file = f.read()
                        f_name = False
        file = encrypt_decrypt.encrypt(file)

        f_name = True
        while f_name:
            file_name = input("Enter a filename to save the encrypted file: ")
            if file_name_verify(file_name):
                if os.path.isfile(file_name):
                    with open(file_name, 'w') as f:
                        f.write("")
                        f.write(file)
                        f_name = False
                else:
                    if file_name_verify(file_name):
                        with open(file_name, 'w') as f:
                            f.write("")
                            f.write(file)
                            f_name = False

    if user_input == 3:
        f_name = False
        message = input("Please enter a message to be decrypted: ")
        message = encrypt_decrypt.decrypt(message)
        if message:
            f_name = True

        while f_name:
            file_name = input("Enter a filename to save the message: ")
            if file_name_verify(file_name):
                if os.path.isfile(file_name):
                    with open(file_name, 'w') as f:
                        f.write("")
                        f.write(message)
                        f_name = False
                else:
                    if file_name_verify(file_name):
                        with open(file_name, 'w') as f:
                            f.write("")
                            f.write(message)
                            f_name = False

    if user_input == 4:

        f_name = True
        while f_name:
            input_file_name = input("Enter a filename with extension: ")
            if file_name_verify(input_file_name):
                if os.path.isfile(input_file_name):
                    with open(input_file_name, 'r') as f:
                        file = f.read()
                        f_name = False
        file = encrypt_decrypt.decrypt(file)
        if file:
            f_name = True

        while f_name:
            file_name = input("Enter a filename to save the decrypted file: ")
            if file_name_verify(file_name):
                if os.path.isfile(file_name):
                    with open(file_name, 'w') as f:
                        f.write("")
                        f.write(file)
                        f_name = False
                else:
                    if file_name_verify(file_name):
                        with open(file_name, 'w') as f:
                            f.write("")
                            f.write(file)
                            f_name = False


inputVerify = True
userInput = ""
key = ""

while inputVerify:
    print("\nOnly .txt file type or a plain message are supported. Please be mindful...")
    userInput = input("""Please select one of the following menu options:
    1. Encrypt a Message
    2. Encrypt a File
    3. Decrypt a Message
    4. Decrypt a File
    5: Exit
    Make Your selection: 
    """)

    if userInput.isdigit():
        userInput = int(userInput)
        if userInput in [1, 2, 3, 4]:
            menu(userInput)
            print("Process Complete.")
        if userInput == 5:
            inputVerify = False

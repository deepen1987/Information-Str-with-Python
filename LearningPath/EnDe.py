key = input("Enter a 8 character key ")
while len(key) != 8:
    key = input("Enter a 8 character key ")
system_Key = 0
for i in key:
    system_Key = system_Key + ord(i)

message = input("Please Enter message to be encrypted: ")

print(message)
new_Message = ""
for i in range(len(message)):
    new_Message += str(ord(message[i]) << system_Key)
    print(ord(message[i]) << system_Key)
    if i != (len(message) - 1):
        new_Message += "@"


arrayMessage = new_Message.split("@")


for i in arrayMessage:
    print(chr(int(i) >> system_Key))

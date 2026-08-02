from cryptography.fernet import Fernet

# def generateKey():
#   key = Fernet.generate_key()
#   with open("keys.key", "wb") as keysFile:
#     print(keysFile.write(key))

def loadKey():
  file = open('keys.key', 'rb')
  key = file.read()
  file.close
  return key

password = input("Type your master password: ")

key = loadKey() + password.encode()
fer = Fernet(key)

def viewPwd():
  with open("password.txt", "r") as n:
    for line in n.readlines():
      userData = line.strip()
      user, passw = userData.split("|")
      print(f'Username: {user} | Password: {fer.encrypt(passw.encode())}')

def changePwd():
  userAccount = input("Type your account name: ")
  userPassword = input("Type your account passwords: ")

  with open("password.txt", "a") as file:
    file.write(f"{userAccount} | {str(fer.encrypt(userPassword.decode()))}" + "\n")
  

while True:
  userResponse = input("Would you like to change your existing password or want to view it (view / change) or Press Q to quit: ").lower()
  if userResponse == 'q':
    break

  if userResponse == 'change':
    changePwd()
  elif userResponse == 'view':
    viewPwd()
  else: print("Enter a valid response")


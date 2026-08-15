userInput = input("Enter Your Age: ")

if userInput.isdigit():
  userInput = int(userInput)

  if userInput >= 0:
    if userInput < 13:
      print(f"Since your age is {userInput}, you belong to Child group")
    elif 13 <= userInput <= 19:
      print(f"Since your age is {userInput}, you belong to Teenager group")
    elif 20 <= userInput <= 59:
      print(f"Since your age is {userInput}, you belong to Adult group")
    elif userInput >= 60:
      print(f"Since your age is {userInput}, you belong to Senior group")

  else:
    print("Enter a integer greater than 0, NOOB!")

else:
  print("Enter a integer value! DUMBASS!")
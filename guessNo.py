import random
userInput = input("Type Your Guessed Number: ")

if userInput.isdigit():
  userInput = int(userInput)
  if userInput <= 0:
    print("Guess a number larger than 0")
else:
  print("Please! Type a integer value")

randomNumber = random.randint(1, userInput)
guesses = 0

while True:
  guesses += 1
  userGuess = input("Guess Number: ")
  if userGuess.isdigit():
    userGuess = int(userGuess)
  else:
    print("Please! type a integer value")  

  if userGuess > randomNumber:
    print('You were above the number')
  elif userGuess < randomNumber:
    print('You were below the number')  

  if userGuess == randomNumber:
    print("You got it!")
    break
  else:
    print("You got it Wrong!")
    continue    

print(f"Your Total Guesses: {guesses}")
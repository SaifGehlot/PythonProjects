import random
userScore = 0
userStart = input("Press S to start the game or Press Q to quit the game: ").lower()

if userStart == 'q':
  print("Game Over!")
elif userStart == 's':
  while True:
    randomDiceNum = random.randint(1, 10)
    enterToRoll = input("Enter to roll the dice: ")
    print(randomDiceNum)

    if randomDiceNum == 1:
      userScore = 0
      print(f"You rolled {randomDiceNum} !")
      break
    else:
      userScore += randomDiceNum
      print(f"You Score is {userScore}")  

    if userScore >= 50:
      print("You Won!")
      break

print(f"Your Final Score Is: {userScore}")


  




import random
userScore = 0
chooseMode = input("Press S to play in SinglePlayer Mode, Press M to play in MultiPlayer Mode: ").lower()

def randomRoll():
  minNumber = 1
  maxNumber = 6
  roll = random.randint(minNumber, maxNumber)

  return roll

def singlePlayer(userScore):
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
        print(f"You rolled {randomDiceNum}")
        break
      else:
        userScore += randomDiceNum
        print(f"You Score is {userScore}")  

      if enterToRoll == 'q':
        break  

      if userScore >= 50:
        print("You Won!")
        break
  print(f"Your Final Score Is: {userScore}")

def multiPlayer(userScore, userMax = 50):
  while True:
    playersCount = input("Enter the number of players (2 - 4): ")

    if playersCount.isdigit():
      playersCount = int(playersCount)
    
      if 2 <= playersCount and playersCount <= 4:
        playerScoresInArr = [0 for _ in range(playersCount)]
        print(playerScoresInArr)
      else:
        print("Enter the number between the given range")
        break

    else:
      print("Enter a integer value")

    while max(userScore) < userMax:
      userRoll = input("Would you like to roll press (y): ").lower()
      diceRollValue = randomRoll()

      if userRoll != 'y':
        print("Your turns over!")
        break

      if diceRollValue == 1:
        userScore = 0
        print(f"You rolled {userScore}")
        break
      else:
        userScore += diceRollValue
        print(f"You rolled: {userScore}")  


if chooseMode == 's':
  singlePlayer(userScore)
elif chooseMode == 'm':
  multiPlayer(userScore)
else:
  print('You Pressed Invalid Key')  
  




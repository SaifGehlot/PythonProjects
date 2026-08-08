import random
userScore = 0
chooseMode = input("Press S to play in SinglePlayer Mode, Press M to play in MultiPlayer Mode: ").lower()

def randomRoll():
  minNumber = 1
  maxNumber = 6
  roll = random.randint(minNumber, maxNumber)

  return roll

def singlePlayer(userScore):
  diceRollValue = randomRoll()
  userStart = input("Press S to start the game or Press Q to quit the game: ").lower()
  if userStart == 'q':
    print("Game Over!")
  elif userStart == 's':
    while True:
      enterToRoll = input("Enter to roll the dice: ")
      print(diceRollValue)

      if diceRollValue == 1:
        userScore = 0
        print(f"You rolled {diceRollValue}")
        break
      else:
        userScore += diceRollValue
        print(f"You Score is {userScore}")  

      if enterToRoll == 'q':
        break  

      if userScore >= 50:
        print("You Won!")
        break
  print(f"Your Final Score Is: {userScore}")

def multiPlayer(userScore):
  maxScore = 50

  while True:
    playersCount = input("Enter the number of players (2 - 4): ")

    if playersCount.isdigit():
      playersCount = int(playersCount)
      playerScoresInArr = [0 for _ in range(playersCount)]
    
      if 2 <= playersCount <= 4:

        while max(playerScoresInArr) < maxScore:
          for playerIdx in range(playersCount):
            currentScore = 0     
            print(f"\n Player {playerIdx + 1}, Turn just started! \n")
            print(f"Your total score is {playerScoresInArr[playerIdx]}")
          
            while True:
              userRoll = input("Would you like to roll press (y): ").lower()  
              diceRollValue = randomRoll()
              print(f"You rolled: {diceRollValue}")
          
              if userRoll != 'y':
                print("Your turns over!")
                break
          
              if diceRollValue == 1:
                currentScore = 0
                print(f"Your turn done!, GG")
                break
          
              else:
                currentScore += diceRollValue
                print("Your current score is: ", currentScore)
        
          playerScoresInArr[playerIdx] += currentScore
          print(f"Your total score is: {playerScoresInArr[playerIdx]}")
      else:
        print("Enter the number between the given range!")
        break

    else:
      print("Enter a integer value!")

if chooseMode == 's':
  # singlePlayer(userScore)
  pass
elif chooseMode == 'm':
  multiPlayer(userScore)
else:
  print('You Pressed Invalid Key')  
  




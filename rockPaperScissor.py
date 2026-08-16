import random

userScore = 0
computerScore = 0
roundWon = "You Won!"
roundLoss = "You Loss!"
roundDraw = "You Draw!"


options = ["rock", "paper", "scissor"]

while True:
  userInput = input("Type Rock/Paper/Scissor or Q to quit: ").lower()

  if userInput == 'q':
    break

  if userInput not in options:
    continue

  randomNumber = random.randint(0, 2)
  # Rock: 0, Paper: 1, Scissor: 2

  computerPicks = options[randomNumber]
  print(f"Computer Picks: {computerPicks}")

  if userInput == "rock" and computerPicks == "scissor":
    print(roundWon)
    userScore += 1

  elif userInput == "paper" and computerPicks == "rock":
    print(roundWon)
    userScore += 1
  
  elif userInput == "scissor" and computerPicks == "paper":
    print(roundWon)
    userScore += 1

  elif userInput == computerPicks:
    print(roundDraw)

  else:
    print(roundLoss)
    computerScore += 1

print(f"You Won {userScore} Times.")
print(f"Computer Won {computerScore} Times.")
print("Goodbye!")


 
                 






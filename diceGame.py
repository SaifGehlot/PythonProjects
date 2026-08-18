import random

def roll():
  min_Value = 1
  max_Value = 6

  roll = random.randint(min_Value, max_Value)
  return roll

while True:
  modeSelection = input("Enter the number of player (2 - 4): ")

  if modeSelection.isdigit():
    modeSelection = int(modeSelection)
    if 2 <= modeSelection <= 4:
      break
    else:
      print('Player must be between 2 to 4')

  else:
    print("Invalid value")

player_scores = [0 for _ in range(modeSelection)]
max_score = 50

while max_score > max(player_scores):

  for currentPlayer in range(modeSelection):
    currentScore = 0
    print(f"\nPlayer number {currentPlayer + 1} turn has just started!")
    print(f"Your total score is: {player_scores[currentPlayer]}\n")

    while True:
      would_roll = input("Would you like to roll (y)? ")
      if would_roll.lower() != 'y':
        break

      rollValue = roll()
      if rollValue == 1:
        print(f"You rolled a {rollValue}! turn done")
        currentScore = 0
        break
      else:
        currentScore += rollValue
        print(f"Your rolled a: {rollValue}")

      print(f"Your total score is: {currentScore}")

    player_scores[currentPlayer] += currentScore
    print("Your total score is:", player_scores[currentPlayer])

winningPlayer = player_scores.index(max(currentScore))
print(f"Player number {winningPlayer + 1} has won the game 🥳")



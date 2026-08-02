import random

print("Welcome to the Quiz Game!")
playing = input("Do You Want to Play the game?: ")

if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :)")

setOfQuestions = [
    "Who is best football player?",
    "How much time it take to learn DSA with consistent efforts?",
    "Which team won the fifa world cup 2026?",
    "How many years are their in 1 decade?",
    "Who won the fifa world cup 2023?"
]

setOfAnswers = [
    "Cristiano Ronaldo",
    "6 months",
    "Spain",
    "10 years",
    "Argentina"
]

randomQuestionSelector = random.randint(0, 4)
userInput = input(f"Here's Your Question: {setOfQuestions[randomQuestionSelector]}: ").lower()

correctAnswer = setOfAnswers[randomQuestionSelector]
if userInput == correctAnswer:
    print(f"{correctAnswer} is Correct")

else:
    print(f"{userInput} is Wrong Answer Unfortunately")



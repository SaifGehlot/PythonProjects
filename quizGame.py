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
    "cristiano ronaldo",
    "6 months",
    "spain",
    "10 years",
    "argentina"
]

randomQuestionSelector = random.randint(0, len(setOfQuestions))
userInput = input(f"Here's Your Question: {setOfQuestions[randomQuestionSelector]}: ").lower()

correctAnswer = setOfAnswers[randomQuestionSelector]

if userInput == correctAnswer:
    print(f"{correctAnswer} is Correct")

else:
    print(f"{userInput} is Wrong Answer Unfortunately")



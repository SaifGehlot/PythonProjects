import datetime

name = input("What is your name ?").strip()
age = input("How old are you ?").strip()
city = input("Which city do you live in ?").strip()
profession = input("What is your profession ?").strip()
hobby = input("What is your favourite hobby ?").strip()

introMessage = (
  f"Hello! my name is {name}, i'm {age} years old and live in {city}"
  f"I work as a {profession} and i absolutely enjoy {hobby} in my free time"
  f"Nice to meet you \n"
)

currentDate = datetime.date.today().isoformat()
introMessage += f"\n Logged on: {currentDate}"

starBorder = "*" * 80
finalIntroMsg = f"{starBorder}\n{introMessage}\n{starBorder}"

print("\n" + finalIntroMsg )
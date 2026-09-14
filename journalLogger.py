import datetime

userEntry = input("Enter what you've learned today?: ").strip()
userRating = input("Enter your productivity rating? (1-5)⭐️: ").strip()

currentDate = datetime.datetime.now()
decodedCurrentDate = currentDate.strftime("%Y-%M-%d - %I:%M %p")

fileEntry = f"🗓️ {decodedCurrentDate}\n{userEntry}\nProductivity Rating: {userRating} Stars"
fileEntry += f"\n{'-' * 50}"

with open("journalEntry", "a") as f:
  f.write(fileEntry)


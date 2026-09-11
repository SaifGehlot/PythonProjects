# def calculateLeft(ageYears):
#   DAYS_IN_YEARS = 365.25
#   HOURSE_IN_DAYS = 24
#   MINUTES_IN_HOUR = 60

#   totalDays = ageYears * DAYS_IN_YEARS
#   totalHourse = totalDays * HOURSE_IN_DAYS
#   totalMinutes = totalHourse * MINUTES_IN_HOUR

#   return round(totalDays), round(totalHourse), round(totalMinutes)

# while True:
#   try:
#     age = float(input("Enter your age: "))
#     days, hours, minutes = calculateLeft(age)
#     print("\n You are approx:")
#     print(f" - {days} days old.")
#     print(f" - {hours} hourse old.")
#     print(f" - {minutes} minutes old \n")

#     again = input("Would you like to try again? (y/n)").strip().lower()

#     if again != 'y':
#       print("Good Bye!")
#       break

#   except ValueError:
#     print("Invalid Input Try Again")

# My code

def aliveLeftCal(ageInput):
  DAYS_IN_YEAR = 365.25
  HOURS_IN_DAY = 24
  MINUTES_IN_HOUR = 60

  totalDays = ageInput * DAYS_IN_YEAR
  totalHourse = totalDays * HOURS_IN_DAY
  totalMinutes = totalHourse * MINUTES_IN_HOUR

  return round(totalDays), round(totalHourse), round(totalMinutes)

while True:
  try:
    userAge = float(input("Enter your age: ").strip())
    days, hours, minutes = aliveLeftCal(userAge)

    print("You age approx: \n")
    print(f" - {days} days.")
    print(f" - {hours} hours.")
    print(f" - {minutes} minutes. \n")
  except ValueError:
    print("Enter a valid age in number ❌")


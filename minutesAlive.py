userAgeInput = int(input("Enter your age in years: ").strip())

def minutesAlive(userAgeInput):
  DAYS_IN_YEARS = 365.25
  HOURS_IN_DAYS = 24
  MINUTES_IN_HOUR = 60

  daysAlive = userAgeInput * DAYS_IN_YEARS
  hoursAlive = daysAlive * HOURS_IN_DAYS
  minutesAlive = hoursAlive * MINUTES_IN_HOUR

  return round(daysAlive), round(hoursAlive), round(minutesAlive)

days, hours, minutes = minutesAlive(userAgeInput)

print("\n You are approx: ")
print(f" - {days} days.")
print(f" - {hours} hours.")
print(f" - {minutes} minutes. \n")





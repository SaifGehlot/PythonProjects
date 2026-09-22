# import time

# while True:
#   try:
#     seconds = int(input("⏰ Enter the time in seconds: "))
#     if seconds < 1:
#       print("Please enter a number greater than 0")
#       continue
#     break
#   except ValueError:
#     print("Invalid input, please enter a whole number")

# print("\n 🔔 Timer Started...")
# for remaining in range(seconds, 0, -1):
#   minutes, secs = divmod(remaining, 60)
#   time_format = f"{minutes:02}:{secs:02}"
#   print(f"🕰️ Time left: {time_format} ", end="\r")
#   time.sleep(1)

# print("\n Time's up! Take a break or move on to next task.")
# print("\a")

# My Code

import time

while True:
  try:
    time_input = int(input("⌛️ Enter time in seconds: "))
    if time_input < 1:
      print("Time should be greater than 0")
      continue
    break
  except ValueError:
    print("❌ Invalid input, enter the time in seconds.")

print("\n Time Started...")
for digit in range(time_input, 0, -1):
  mins, secs = divmod(digit, 60)
  time_format = f'{mins:02}:{secs:02}'
  print(f"⏰ Time Left: {time_format}", end="\r")
  time.sleep(1)

print("Time's up! Better luck next time")

  
## Bill splitter

print("\nWelcome to bill splitter\n")

def getFloat(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("❌ Please enter a valid number.")


grpCount = int(input("How many people are in the group: "))
individualNames = []

for i in range(grpCount):
  name = input(f"Enter name of person {i + 1}: ")
  individualNames.append(name)

totalBill = getFloat("Enter your overall bill in number only: ")

share = round(totalBill / grpCount, 2)

print("-" * 20 + "\n")

print(totalBill)
print(f"Each person owes: {share}")

for name in individualNames:
  print(f"{name}: {share}")

print("\n" + "-" * 20)

# Expense tracker

def getExpenseFloat(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("❌ Enter a valid number")

print("\n" + "=" * 5 + " Expense Tracker " + "=" * 5 + "\n")

countUsers = int(input("Enter how many people: "))
print("\n")

userData = dict()

for i in range(countUsers):
  userNameInput = input(f"Enter the user name #{i + 1}: ")
  userExpenseInput = getExpenseFloat("Enter user expense: ")
  userData = name = userNameInput, expense = userExpenseInput

  print("\n")

print("\n" + "-" * 25 + "\n")

print(f"Total Expense: {userExpenseInput}")

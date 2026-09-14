print("\n" + "-" * 10 + " Expense Tracker " + "-" * 10 + "\n")

peopleCount = int(input("How many people? ").strip())
individUserData = []

for user in range(peopleCount):
  indivdUserName = input("Enter name: ")
  individUserExpense = input("Enter expense: ")

  individUserData.append({indivdUserName, individUserExpense})


print(individUserData)
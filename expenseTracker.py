print("\n" + "-" * 15 + " Welcome To Expense Tracker " + 15 * "-" + "\n")

userData = []
expenses = []

def expense_tracker(userData, expenses):
  user_count_input = int(input("Enter how many users: ").strip())

  for user in range(user_count_input):
    user_name_input = input(f"Enter user name #{user + 1}: ").lower()
    user_expense_input = int(input(f"Enter user expense: "))

    userData.append({"name": user_name_input, "expense": user_expense_input})
    expenses.append(user_expense_input)

  print("Here's your expenses details: " + "\n")
  highest_user = max(userData, key=lambda user: user["expense"])
  lowest_user = min(userData, key=lambda user: user["expense"])

  for indivdUser in userData:
    print(f"{indivdUser["name"]}: ${indivdUser["expense"]}")

  print(f"{highest_user["name"]} has highest expense: ${highest_user["expense"]}")
  print(f"{lowest_user["name"]} has lowest expense: ${lowest_user["expense"]}")
  
  return userData, expenses

def bubbleSort(expenses):
  n = len(expenses)

  for i in range(n):
    for j in range(0, n-i-1):
      if expenses[j] > expenses[j+1]:
        expenses[j], expenses[j+1] = expenses[j+1], expenses[j]

  return expenses


expense_tracker(userData, expenses)



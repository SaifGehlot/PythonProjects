grpCount = int(input("How many people are there in the grp?: ").strip())
userData = []

for user in range(grpCount):
  individUserName = input(f"Enter the name of user #{user + 1}: ").strip()
  userData.append(individUserName)

overallBill = int(input("Enter the overall bill in numbers: ").strip())
share = round(overallBill / len(userData), 2)

print("\n" + "-" * 10 + " Here's Your Bill " + "-" * 10 + "\n")
print(f"Total bill: {overallBill}")
print(f"Each person owes: {share}")

for indivdUser in userData:
  print(f"{indivdUser} owes {share} rupess")

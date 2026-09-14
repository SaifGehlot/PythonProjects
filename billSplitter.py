# Bill splitter

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



  

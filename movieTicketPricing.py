age = 25
ticketPrice = 12 if age >= 18 else 8
offDay = "Thursday"

if offDay == "Wednesday":
  ticketPrice -= 2

print(f"Your ticket price is ${ticketPrice} ")
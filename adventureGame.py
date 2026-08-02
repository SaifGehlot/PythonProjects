userName = input("Please Type Here Your Name: ")
print(f"Hello! {userName} To The Adventure Game!")

answer = input("You are on a dirt road, it as come to an end and you can go left or right. which way would you like to go? left or right: ").lower()
if answer == 'right':
  swimWalk = input('You came to a river, you can walk around it or swim accross? Type walk to walk around it or swim to swim accross it: ').lower()
  if swimWalk == "swim":
    print("You swam accross and get eaten my a alligator.")
  elif swimWalk == "walk":
    print("You walked too much and ran out of water.")
  else: print("Not a valid option")  

elif answer == 'left':
  bridgeCross = input("You came accross a bridge, it looks wobbly, you want to cross it or head back, Type cross to cross over it or back to go back: ").lower()
  if bridgeCross == 'cross':
    print("You died! Don't know why")
  elif bridgeCross == 'back':
    print("Saala Fattu, Aage Jaana Piche kyun aa rha hai")
  else: print("Not a valid option")

else: print('Not a Valid option!')

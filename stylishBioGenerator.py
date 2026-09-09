import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favourite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style")
print("1. Simple Line")
print("2. Vertical Line")
print("3. Emoji Sandwitch")

style = input("Choose Your Bio Style: \n").strip()

def generateBio(style):
  if style == "1":
    return f"{emoji} | {name} --> {profession}\n💡 | {passion}\n📃 | {website}"
  elif style == "2":
    return f"{emoji} | {name}\n🔥 | {profession}\n🚀 | {passion}"
  elif style == "3":
    return f"{emoji * 3}\n {name} - {profession}\n {passion}\n {website}\n {emoji * 3}"

bio = generateBio(style)

print("\nYour Stylish Bio:")
print("-" * 50 + "\n")
print(textwrap.dedent(bio))
print("\n" + "-" * 50)

save = input("Do you want to save this Bio to a text file? (y/n): ")

if save.lower() == "y":
  fileName = f"{name.lower().replace(" ", "_")}_bio.txt"
  with open(fileName, "w", encoding="utf-8") as f:
    f.write(bio)

  print("file saved")
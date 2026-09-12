emojiMapFun = {
  "love": "❤️",
  "happy": "😀",
  "code": "💻",
  "chai": "☕️",
  "music": "🎵",
  "food": "🌭"
}

userMessage = input("Enter your message here: ").strip().lower()
updatedWord = []

for word in userMessage.split():
  cleanedWord = word.strip(".,!?#$%^&*").lower()
  emojiFound = emojiMapFun.get(cleanedWord, None)

  if emojiFound:
    updatedWord.append(f"{word} {emojiFound}")
  else:
    updatedWord.append(word)

updatedMessage = " ".join(updatedWord)
print("Enhanced Message: \n")
print(updatedMessage)
emojisContainer = {
  "love": "❤️",
  "happy": "😀",
  "code": "💻",
  "chai": "☕️",
  "music": "🎵",
  "food": "🌭"
}

userMessage = input("Enter your message: ").strip()
updateWords = []

for word in userMessage.split():
  cleanedWord = word.strip("!@#$%^&*.,?").lower()
  emojiFound = emojisContainer.get(cleanedWord, "")

  if emojiFound:
    updateWords.append(f"{cleanedWord} {emojiFound}")
  else:
    updateWords.append(word)

finalMessage = " ".join(updateWords)
print("Here's is your enhanced message!")
print(finalMessage)

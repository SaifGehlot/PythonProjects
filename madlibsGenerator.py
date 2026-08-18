with open("story.txt", "r") as f:
  story = f.read()

words = set()
startOfWord = None

targetStart = "<"
targetEnd = ">"

for i, char in enumerate(story):
  if char == targetStart:
    startOfWord = i

  if char == targetEnd and startOfWord != None:
    word = story[startOfWord: i + 1]
    words.add(word)
    startOfWord = -1

answers = {}

for word in words:
  answer = input(f"Enter a word for {word}: ")
  answers[word] = answer

for word in words:
  story = story.replace(word, answers[word])

print(story)
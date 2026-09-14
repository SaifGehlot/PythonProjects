import datetime

entry = input("What did you learn today? ").strip()
rating = input("⭐️ Rate your productivity today (1-5, optional)" ).strip()

now = datetime.datetime.now()
dateStr = now.strftime("%Y-%m-%d - %I:%M %p")
print(dateStr)
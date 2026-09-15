import os

TASK_FILE = "tasks.txt"

def loadTasks():
  tasks = []
  if(os.path.exists(TASK_FILE)):
    with open(TASK_FILE, 'r', encoding='utf-8') as f:
      for line in f:
        text, status = line.strip().rsplit("||", 1)
        tasks.append({"text": text, "done": status == "done"})
  return tasks

def saveTasks(tasks):
  with open(TASK_FILE, 'w', encoding="utf-8") as f:
    for task in tasks:
      status = "done" if task["done"] else "not done"
      f.write(f"{task['text']}||{status}")

def displayTasks(tasks):
  if not tasks:
    print("No task found!")
  else:
    for i, task in enumerate(tasks, 1):
      checkbox = "✅" if task["done"] else " "
      print(f"{i}. [{checkbox}] {task["text"]}")
  print()

def taskManager():
  tasks = loadTasks()

  while True:
    print("\n ------- Task List Manager -------")
    print("1. Add task")
    print("2. View task")
    print("3. Mark Task as complete")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    match choice:
      case "1":
        text = input("Enter your task: ").strip()

        if text:
          tasks.append({"text":text, "done": False})
          saveTasks(tasks)
        else:
          print("Task connot be empty")

      case "2":
        displayTasks(tasks)

      case "3":
        displayTasks(tasks)
        try:
          num = int(input("Enter task number"))
          if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            saveTasks(tasks)
            print("task marked as DONE")
          else:
            print("Enter a valid task number")
        except ValueError:
          print("Please enter a number")

      case "4":
        displayTasks(tasks)
        try:
          num = int(input("Enter task number to delete"))
          if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            saveTasks(tasks)
            print(f"task removed {removed['text']}")
          else:
            print("Enter a valid task number")
        except ValueError:
          print("Please enter a number")

      case "5":
        print("Exciting task Manager")
        break

      case _:
        print("Please enter a valid choice.")

taskManager()

      
                

  
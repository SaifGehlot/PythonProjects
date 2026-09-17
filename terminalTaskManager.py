# import os
# TASKS_FILE = 'tasks.txt'

# def loadTasks():
#   tasks = []
#   if(os.path.exists(TASKS_FILE)):
#     with open(TASKS_FILE, "r", encoding="utf-8") as f:
#       for line in f:
#         text, status = line.strip().rsplit("-", 1)
#         tasks.append({"text": text, "done": status == "done"})

#   return tasks

# def saveTasks(tasks):
#   with open(TASKS_FILE, 'w', encoding="utf-8") as f:
#     for task in tasks:
#       status = "done" if task["done"] else "not done"
#       f.write(f"{task["text"]}-{status}")

# def displayTasks(tasks):
#   if not tasks:
#     print("No task found!")
#   else:
#     for i, task in enumerate(tasks, 1):
#       checkbox = "✅" if task["done"] else "❌"
#       print(f"{i}. [{checkbox}] {task["text"]}")
#     print()

# def taskManager():
#   tasks = loadTasks()

#   while True:
#     print("\n ------- Task List Manager -------")
#     print("1. Add task")
#     print("2. View task")
#     print("3. Mark Task as complete")
#     print("4. Delete task")
#     print("5. Exit")
#     print("\n")

#     choice = input("Enter the option (1-5): ")

#     match choice:
#       case "1":
#         text = input("Enter task here: ").strip()
#         if text:
#           tasks.append({"text": text, "done": False})
#           saveTasks(tasks)
#         else:
#           print("Task cannot be empty.")

#       case "2":
#         displayTasks(tasks)

#       case "3":
#         displayTasks(tasks)
#         try:
#           markTask = int(input("Enter the task number: ").strip())
#           if 1 <= markTask <= len(tasks):
#             tasks[markTask-1]["done"] = True
#             saveTasks(tasks)
#             print("Task marked as DONE!")
#           else:
#             print("Enter a valid task number.")
#         except ValueError:
#           print("Enter a number value, NOOB!")

#       case "4":
#         displayTasks(tasks)
#         try:
#           markTask = int(input("Enter the task number to delete: ").strip())
#           if 1 <= markTask <= len(tasks):
#             tasks.pop(markTask-1)
#             saveTasks(tasks)
#             print("Task marked as DONE!")
#           else:
#             print("Enter a valid task number.")
#         except ValueError:
#           print("Enter a number value, NOOB!")

#       case "5":
#         print("Exiting task manager")
#         break

#       case _:
#         print("Enter a valid choice!")

# taskManager()
        


import os
TASK_FILE = "tasks02.txt"

def load_task():
  tasks = []
  if(os.path.exists(TASK_FILE)):
    with open(TASK_FILE, 'r', encoding="utf-8") as f:
      for line in f:
        text, status = line.strip().rsplit("-", 1)
        tasks.append({"text": text, "done": status == 'done'})    
  return tasks

def save_task(tasks):
  with open(TASK_FILE, 'w', encoding='utf-8') as f:
    for task in tasks:
       status = "done" if task["done"] else "not done"
       f.write(f"{task["text"]}-{status}")  

def display_task(tasks):
  if not tasks:
    print("No task found!")
  else:
    for i, task in enumerate(tasks, 1):
      checkbox = "✅" if task["done"] else "❌"
      print(f"{i} [{checkbox}] {task}")
  print()


def task_manager():
  tasks = load_task()










      
                

  
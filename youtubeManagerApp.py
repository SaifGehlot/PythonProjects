import json

def load_videos():
  try:
    with open('youtube.txt', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_videos_helper(videos):
  with open("youtube.txt", "w") as file:
    json.dump(videos, file)


def list_all_videos(videos):
  if videos:
    for index, video in enumerate(videos, 1):
      print(f"{index}. {video['name']}, Duration: {video['time']} ")
  else:
    print("No videos found! Kindly add one")

def add_video(videos):
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  videos.append({"name": name, "time": time})
  save_videos_helper(videos)
  print("Video added successfully ✅")

def update_video(videos):
  list_all_videos(videos)
  video_num = int(input("Enter video num: "))
  if 1 <= video_num <= len(videos):
      print(videos[video_num-1])
      update_detail = input("Enter what detail you want to update (name or time): ").lower()
      if update_detail == "name":
        update_name = input("Enter new name: ")
        videos[video_num-1]['name'] = f"{update_name}"
      elif update_detail == "time":
        update_time = input("Enter new time: ")
        videos[video_num-1]['time'] = f"{update_time}"
      print("Detail updated successfully ✅")
  else:
      print("No video found with that number 😕")

def delete_video(videos):
  list_all_videos(videos)
  del_video = int(input("Enter video num: "))
  if 1 <= del_video <= len(videos):
    videos.pop(del_video-1)
    save_videos_helper(videos)
    print("Video deleted successfully ✅")
  else:
    print("No video found with that number 😕")


def main():
  videos = load_videos()
  while True:
    print("\n Youtube Manager | Choose an option ")
    print("1. List all youtube videos ")
    print("2. Add a youtube video ")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app ")

    choice = input("Enter your choice: ")

    match choice:
      case "1":
        list_all_videos(videos)

      case "2":
        add_video(videos)

      case "3":
        update_video(videos)

      case "4":
        delete_video(videos)

      case "5":
        break

      case _:
        print("Invalid Choice")   

if __name__ == "__main__":
  main()
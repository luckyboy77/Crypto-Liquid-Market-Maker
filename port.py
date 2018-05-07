import json

def save_book(book, name=None, file_path=None):
  if not file_path and not name:
    file_path = "./saved_book.json"
    tag = "w+"
  elif not file_path:
    file_path = name + ".json"
    tag = "w+"
  else: 
    tag = "w"

  with open(file_path, tag) as file:
    json.dump(book, file, indent=4)

def open_book(file_path):
  with open(file_path, "r") as file:
    return json.loads(file)

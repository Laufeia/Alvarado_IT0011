import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "students.txt")

with open(file_path, "r") as file:
    contents = file.read()
    print(contents)

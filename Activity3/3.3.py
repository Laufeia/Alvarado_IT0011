import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "students.txt")

last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
contact_number = input("Enter your contact number: ")
course = input("Enter your course: ")

student_info = (
    f"Last Name: {last_name}\n"
    f"First Name: {first_name}\n"
    f"Age: {age}\n"
    f"Contact Number: {contact_number}\n"
    f"Course: {course}\n\n\n"
)
with open(file_path, "a") as file:
    file.write(student_info)

print("Student information has been saved successfully.")

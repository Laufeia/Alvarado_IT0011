first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

full_name = first_name + " " + last_name
sliced_fname = first_name[:3]
greeting_message = f"Hello!, {first_name}! Welcome. You are {age} years old."

print("Full Name:", full_name)
print("Sliced First Name:", sliced_fname)
print("Greeting Message:", greeting_message)
import os
import ast

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.getcwd()
    
os.chdir(script_dir)

records = []
current_file = None

def open_file():
    global records, current_file
    filename = input("Enter filename to open (e.g., students.txt): ")
    file_path = os.path.join(script_dir, filename)
    if os.path.exists(file_path):
        current_file = file_path
        records.clear()
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    record = ast.literal_eval(line)
                    records.append(record)
        print("File opened successfully.")
    else:
        print("File not found in the script's folder.")

def save_file():
    global records, current_file
    if current_file is None:
        print("No file is currently open. Use Save As option.")
        return
    with open(current_file, "w") as file:
        for record in records:
            file.write(str(record) + "\n")
    print("File saved successfully.")

def save_as_file():
    global records, current_file
    filename = input("Enter new filename to save as: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    current_file = filename
    with open(current_file, "w") as file:
        for record in records:
            file.write(str(record) + "\n")
    print("File saved as", current_file)

def show_all_students_record():
    if not records:
        print("No records available.")
        return
    print("1. Order by last name")
    print("2. Order by grade")
    option = input("Select ordering option: ")
    if option == "1":
        sorted_records = sorted(records, key=lambda r: r[1][1].lower())
    elif option == "2":
        sorted_records = sorted(records, key=lambda r: 0.6 * r[2] + 0.4 * r[3], reverse=True)
    else:
        print("Invalid option. Showing unsorted records.")
        sorted_records = records
    for rec in sorted_records:
        student_id, name, class_standing, exam_grade = rec
        final_grade = 0.6 * class_standing + 0.4 * exam_grade
        print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class Standing: {class_standing}, Exam Grade: {exam_grade}, Final Grade: {final_grade:.2f}")

def show_student_record():
    sid = input("Enter student ID to search: ")
    found = False
    for rec in records:
        if str(rec[0]) == sid:
            student_id, name, class_standing, exam_grade = rec
            final_grade = 0.6 * class_standing + 0.4 * exam_grade
            print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class Standing: {class_standing}, Exam Grade: {exam_grade}, Final Grade: {final_grade:.2f}")
            found = True
    if not found:
        print("Student record not found.")

def add_record():
    sid = input("Enter student ID (6 digits): ")
    if len(sid) != 6 or not sid.isdigit():
        print("Invalid student ID.")
        return
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    try:
        cs = float(input("Enter class standing grade: "))
        exam = float(input("Enter major exam grade: "))
    except ValueError:
        print("Invalid grade input.")
        return
    record = (int(sid), (first, last), cs, exam)
    records.append(record)
    print("Record added.")

def edit_record():
    sid = input("Enter student ID to edit: ")
    for i, rec in enumerate(records):
        if str(rec[0]) == sid:
            print("Current record:", rec)
            first = input("Enter new first name (or press enter to keep unchanged): ")
            last = input("Enter new last name (or press enter to keep unchanged): ")
            cs_input = input("Enter new class standing grade (or press enter to keep unchanged): ")
            exam_input = input("Enter new major exam grade (or press enter to keep unchanged): ")
            new_first = first if first else rec[1][0]
            new_last = last if last else rec[1][1]
            new_cs = float(cs_input) if cs_input else rec[2]
            new_exam = float(exam_input) if exam_input else rec[3]
            records[i] = (rec[0], (new_first, new_last), new_cs, new_exam)
            print("Record updated.")
            return
    print("Record not found.")

def delete_record():
    sid = input("Enter student ID to delete: ")
    for i, rec in enumerate(records):
        if str(rec[0]) == sid:
            print("Deleting record:", rec)
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == "y":
                records.pop(i)
                print("Record deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Record not found.")

def main_menu():
    while True:
        print("\nRecord Management Menu")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Show Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            save_as_file()
        elif choice == "4":
            show_all_students_record()
        elif choice == "5":
            show_student_record()
        elif choice == "6":
            add_record()
        elif choice == "7":
            edit_record()
        elif choice == "8":
            delete_record()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

from datetime import datetime

date_input = input("Enter the date (mm/dd/yyyy): ")

try:
    date_obj = datetime.strptime(date_input, "%m/%d/%Y")
    formatted_date = f"{date_obj.strftime('%B')} {date_obj.day}, {date_obj.year}"
    print("Date Output:", formatted_date)
except ValueError:
    print("Invalid date format. Please use mm/dd/yyyy.")

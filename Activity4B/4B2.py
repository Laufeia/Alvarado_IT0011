import os
import csv

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.getcwd()

os.chdir(script_dir)
file_path = os.path.join(script_dir, "currency.csv")

exchange_rates = {}
currency_names = {}

try:
    with open(file_path, newline="", encoding="latin-1") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        print("Detected fieldnames:", reader.fieldnames)
        for row in reader:
            code = row["code"].strip()
            name = row["name"].strip()
            rate = float(row["rate"].strip())
            exchange_rates[code.upper()] = rate
            currency_names[code.upper()] = name
except FileNotFoundError:
    print("Error: currency.csv not found in the script folder.")
    exit(1)
except Exception as e:
    print("Error reading the CSV file:", e)
    exit(1)

try:
    dollar_amount = float(input("How much dollar do you have? "))
except ValueError:
    print("Invalid input for dollar amount.")
    exit(1)

target_currency = input("What currency you want to have? ").strip().upper()

if target_currency in exchange_rates:
    converted_amount = dollar_amount * exchange_rates[target_currency]
    print(f"\nDollar: {dollar_amount} USD")
    print(f"{currency_names[target_currency]}: {converted_amount}")
else:
    print("Currency code not found.")

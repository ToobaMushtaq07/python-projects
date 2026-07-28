#Employee record
import csv
import json

employees = [
    {"ID": 101, "Name": "Ali", "Salary": 55000, "Department": "IT"},
    {"ID": 102, "Name": "Sara", "Salary": 45000, "Department": "HR"},
    {"ID": 103, "Name": "Ahmed", "Salary": 60000, "Department": "Finance"},
    {"ID": 104, "Name": "Ayesha", "Salary": 35000, "Department": "Marketing"}
]

# Write data to CSV
with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(employees)

# Write data to JSON
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

# Read CSV file
print("Employee Data from CSV:")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Read JSON file
print("\nEmployee Data from JSON:")
with open("employees.json", "r") as file:
    data = json.load(file)
    for employee in data:
        print(employee)

print("\nEmployees with Salary > 50000:")
for employee in data:
    if employee["Salary"] > 50000:
        print(employee)
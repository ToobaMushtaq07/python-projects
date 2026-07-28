import csv
import json
students = [
    {"ID": 1, "Name": "Ali", "Age": 20, "Marks": 85},
    {"ID": 2, "Name": "Sara", "Age": 21, "Marks": 72},
    {"ID": 3, "Name": "Ahmed", "Age": 19, "Marks": 90},
    {"ID": 4, "Name": "Ayesha", "Age": 22, "Marks": 65}
]
# Write data to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

# Write data to JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Read CSV file
print("Reading CSV File:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Read JSON file
print("\nReading JSON File:")
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data:
        print(student)

print("\nStudents with Marks >= 80:")
for student in data:
    if student["Marks"] >= 80:
        print(student)
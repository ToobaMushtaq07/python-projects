# project : grade calculator
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def get_marks():
    while True:
        try:
            marks = float(input("Enter student marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Error: Marks must be between 0 and 100.")
            else:
                return marks

        except ValueError:
            print("Error: Please enter a valid numeric value.")
def main():
    print("=" * 40)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)

    marks = get_marks()
    grade = calculate_grade(marks)

    print("\n--------- RESULT ---------")
    print(f"Student Marks : {marks}")
    print(f"Student Grade : {grade}")
    print("--------------------------")

if __name__ == "_main_":u
main()
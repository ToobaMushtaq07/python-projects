# reverse a string
text = input("Enter a string: ")
reverse = ""
for i in text:
    reverse = i + reverse
print("Reversed string:",reverse)


#two strings are anagrams
str1 = input("enter first string:")
str2 = input("enter second string:")
if sorted(str1) == sorted(str2):
    print("anagrams")
else:
    print("not anagrams")


# second largest number in list
numb = [20 ,46 ,76 ,14 ,37]
numb.sort()
print("second largest number:",numb[-2])


#student class with grades
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 80:
            return "A"
         elif 
        self.marks >= 60:
        return "B"
         elif
        self.marks >= 40:
            return "C"
         else:
  return " Fail"
s = Student("ali",90)
print("Name:",s.name)
print("Marks:",s.marks)
print("Grade:",s.grade())

#to-do list task
tasks = []
def add_task():
    task = input("Enter task: ")
    tasks.append(task)

def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found.")

def view_tasks():
    print("Tasks:")
    for task in tasks:
        print(task)

add_task()
add_task()
view_tasks()
remove_task()
view_tasks()


# handle division safely
try:
    x = int(input("enter first numb:"))
    y = int(input("enter second numb:"))
    print("result:", x/y)
except ZeroDevisionError:
        print("cannot divide by zero.")
except ValueError:
        print("invalid input.")



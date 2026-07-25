#valid input integer
while True:
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")


#addition of two number
while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)
        break
    except ValueError:
        print("Please enter valid integers only.")
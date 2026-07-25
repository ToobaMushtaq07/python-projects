while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)
        break
    except ValueError:
        print("Please enter valid integers only.")
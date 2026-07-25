#exception safe 
while True:
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
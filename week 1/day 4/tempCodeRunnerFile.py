try:
    x = int(input("enter first numb:"))
    y = int(input("enter second numb:"))
    print("result:", x/y)
    except ZeroDevisionError:
        print("cannot divide by zero.")
    except ValueError:
        print("invalid input.")


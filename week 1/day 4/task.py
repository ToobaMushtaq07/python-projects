def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
                              #temp converter
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
                             #calculate area
def circle_area(radius):
    return 3.14 * radius * radius

def rectangle_area(length, width):
    return length * width

print(" Celsius to Fahrenheit")
print(" Fahrenheit to Celsius")
print(" Area of Circle")
print(" Area of Rectangle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(f))

elif choice == 3:
    r = float(input("Enter radius: "))
    print("Area of Circle:", circle_area(r))

elif choice == 4:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", rectangle_area(l, w))

else:
    print("Invalid choice!")
n = int(input("Enter the numbs of terms"))
a = 1
b = 5
print("fibnocci series using loop")
for i in range(n):
    print(a, end="")
    c=a + b
    a = b
    b = c

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fib(i), end=" ")

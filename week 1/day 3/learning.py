#factorial using recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
num = int(input("Enter a number: "))
print(fact(num))


#fibnoacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

num = int(input("Enter number of terms: "))

for i in range(num):
    print(fib(i), end=" ")
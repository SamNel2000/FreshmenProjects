name = input("Enter 'A' for Fibonacci Sequence and 'B' for Lucas Sequence: ")

def fib(a, b):
    n = int(input("Enter the ordinal value of the term you want: ")) - 1
    for x in range(n):
        a = a + b
        b = a - b
    print("The " + str(n + 2) + "th term of the fibonacci sequence is:", a, "\nThe approximation of the golden ratio is:", a/b)

def lucas(a, b, c):
    n = int(input("Enter the ordinal value of the term you want: ")) - 1
    if n == -1:
        c = 2
    for x in range(n):
        a = b + c
        b = c
        c = a
    print("The " + str(n + 2) + "th term of the lucas sequence is:", c,  "\nThe approximation of the golden ratio is:", c/b)

if name == 'A':
    fib(1, 1)
    
if name == 'B':
    lucas(0, 2, 1)
    

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
print(Fibonacci(9))


def factorial_recursive(number):
    if number == 1:
        return number
    return number * factorial_recursive(number-1)

print(factorial_recursive(5))
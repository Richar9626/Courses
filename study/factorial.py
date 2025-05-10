def factorial_iterative(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = 5
print(f"Factorial de {n} es {factorial_iterative(n)}")
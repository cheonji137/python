def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
    
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = eval(input("Enter a number: "))
print(n, "! =", factorial(n))
print(n, "! =", fact(n))
#loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# user input
a = int(input("Enter a number : "))

# print the result
result = factorial(a)
print(f"The factorial of {a} is: {result}")
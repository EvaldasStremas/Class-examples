def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    print(x)

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 1000
print("The factorial of", num, "is", factorial(num))
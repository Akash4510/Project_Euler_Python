from functools import reduce


def factorial(n):
    result = 1
    for x in range(n, 0, -1):
        result *= x
    return result


s = int(input("Enter the number: "))
num = factorial(s)
op = list(str(num))
print(reduce(lambda x, y: int(x)+int(y), op))

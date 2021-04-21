def sum_even_fibonacci(num):
    fibonacci_list = [0, 1]
    temp = 0
    num1 = 0
    num2 = 1
    while temp in range(0, num):
        temp = num1 + num2
        fibonacci_list.append(temp)
        num1, num2 = num2, temp

    for x in fibonacci_list:
        if x > num:
            fibonacci_list.pop(fibonacci_list.index(x))
            print(f"Fibonacci series for nos. not greater than {num}: ", fibonacci_list)

    even_fibonacci_list = []
    for x in fibonacci_list:
        if x % 2 == 0:
            even_fibonacci_list.append(x)
    print("Even Fibonacci list: ", even_fibonacci_list)
    print("The Sum of all the numbers in even fibonacci list: ", sum(even_fibonacci_list))
    return sum(even_fibonacci_list)

def my_func():

    my_list = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            my_list.append(str(product))

    palindrome = []
    for num in my_list:
        if len(num) == 5:
            if num[0] == num[4] and num[1] == num[3]:
                palindrome.append(int(num))
        elif len(num) == 6:
            if num[0] == num[5] and num[1] == num[4] and num[2] == num[3]:
                palindrome.append(int(num))

    print("Palindromes: ", palindrome)
    print("Maximum Palindrome number: ", max(palindrome))
    return max(palindrome)


my_func()

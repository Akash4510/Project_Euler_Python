def prime_list(num):

    x = 2
    my_list = []
    while len(my_list) <= num:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            my_list.append(x)
        x += 1

    print(my_list)
    print(f"{num}st prime number = {my_list[num-1]}")


prime_list(10001)

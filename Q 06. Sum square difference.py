def sum_square_difference():

    my_list = list(range(0, 101))
    x = list(map(lambda num: num**2, my_list))
    square_sum = sum(x)

    y = sum(my_list)
    sum_square = y ** 2

    print("All numbers: ", my_list)
    print("Sum of all numbers: ", y)
    print("Square of sum: ", sum_square)
    print("Square list: ", x)
    print("Sum of squares: ", square_sum)
    print(sum_square - square_sum)


sum_square_difference()

def largest_prime_factor(num):

    all_factors_list = []
    for i in range(1, num+1):
        if num % i == 0:
            all_factors_list.append(i)

    odd_factors_list = []
    for x in range(1, num+1, 2):
        if num % x == 0:
            odd_factors_list.append(x)

    prime_factors_list = []
    for y in odd_factors_list:
        for z in range(3, y):
            if y % z == 0:
                break
        else:
            prime_factors_list.append(y)

    print("All Factors: ", all_factors_list)
    print("Odd Factors: ", odd_factors_list)
    print("Prime Factors: ", prime_factors_list)
    print("Largest Prime Factor: ", max(prime_factors_list))
    return max(prime_factors_list)


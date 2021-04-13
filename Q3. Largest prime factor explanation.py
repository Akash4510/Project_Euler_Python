def largest_prime_factor(num):

    # First we will create a list of all the factors of the given number.
    # This is completely OPTIONAL.

    all_factors_list = []
    for i in range(1, num+1):
        if num % i == 0:
            all_factors_list.append(i)

    # Then we will create a list of all odd factors for the given number.

    odd_factors_list = []
    for x in range(1, num+1, 2):  # Here we selected step size of 2 to skip all the even no.s.
        if num % x == 0:
            odd_factors_list.append(x)

    # The reason we created the odd factors list because even numbers cannot be prime numbers.
    # So when we list out all the prime no.s from this list, it will be quicker than all_factors_list.
    # Because in this list we don't have to check for even no.s.

    # After getting all the odd factors we will check for the prime numbers in the list.
    # Then make a list of all the prime numbers present in the odd_factors_list.

    prime_factors_list = []
    for y in odd_factors_list:
        for z in range(3, y):
            if y % z == 0:
                break
        else:
            prime_factors_list.append(y)

    # In the above for loop we used an for, else statement inside the loop to determine the prime no.s.
    # If the number is prime then num % z != 0, therefore we added that no. to the prime_factors_list.

    print("All Factors: ", all_factors_list)
    print("Odd Factors: ", odd_factors_list)
    print("Prime Factors: ", prime_factors_list)
    print("Largest Prime Factor: ", max(prime_factors_list))
    return max(prime_factors_list)


largest_prime_factor(435378)

def get_number():
    while True:
        n = input("Enter the number: ")
        if n.isdigit():
            return int(n)
        else:
            print("Whoops! that's not a number.")
            continue


def collatz(num):
    my_list = []
    while True:
        if num == 1:
            my_list.append(num)
            break
        elif num % 2 == 0:
            my_list.append(num)
            num = int(num / 2)
        elif num % 2 != 0:
            my_list.append(num)
            num = (3*num) + 1
        else:
            print("Unexpected Problem!")
    return len(my_list)


value = get_number()
max_len = 0
max_num = 0
for s in range(1, value+1):
    op = collatz(s)
    if op > max_len:
        max_len = op
        max_num = s
print(f"The number is {max_num} with {max_len} terms in the collatz sequence.")

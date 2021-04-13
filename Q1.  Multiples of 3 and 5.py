my_list = []
for x in range(0, 1000):
    if x % 3 == 0 or x % 5 == 0:
        my_list.append(x)
print(sum(my_list))
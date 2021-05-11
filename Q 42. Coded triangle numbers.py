import string

my_list = list(string.ascii_lowercase)
my_dict = {}
for num, alp in enumerate(my_list, start=1):
    my_dict[alp] = num

tri_count = 0
with open("p042_words.txt") as f:
    for lines in f.readlines():
        for items in lines.split(','):
            word = items.replace('"', '')
            value = 0
            for i in word:
                value += my_dict[i.lower()]
            for y in range(0, value+1):
                if value == (y/2)*(y+1):
                    tri_count += 1
                    print(f"'{word}' is a triangle Word ({value})")
                    break
    print(f"Total triangle words: {tri_count}")

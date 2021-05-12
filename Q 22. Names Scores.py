import string

letters = list(string.ascii_lowercase)
alpha_dict = {}
for num, alpha in enumerate(letters, start=1):
    alpha_dict[alpha] = num


def word_value(word):
    value = 0
    word_list = list(word)
    for s in word_list:
        value += alpha_dict[s.lower()]
    return value


def name_score(w, li):
    score = word_value(w)*(li.index(w)+1)
    return score


with open("p022_names.txt") as f:
    all_words = f.readlines()
    clean_words = []
    for lines in all_words:
        for words in lines.split(','):
            new_words = words.replace('"', '')
            clean_words.append(new_words)

clean_words = sorted(clean_words)
total_value = 0
for i in clean_words:
    total_value += name_score(i, clean_words)
print(f"Total value = {total_value}")

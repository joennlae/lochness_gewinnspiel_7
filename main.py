import random
import numpy as np

def get_str_value(str_: str) -> np.ndarray:
    values = np.zeros(5, np.int32)
    lower = str_.lower()
    i = 0
    for c in lower:
        values[i] = ord(c) - 96
        i += 1
    return values

def get_average(list: list[str]) -> np.ndarray:
    total = np.zeros(5, np.float64)

    for s in list:
        total += get_str_value(s)
    
    avg = total / len(list)
    return avg

def calc_error(str: str, comp: np.ndarray) -> float:
    value = get_str_value(str)
    err = np.sum(np.abs(comp - value))
    return err

words_5 = []

file1 = open('words.txt', 'r')
Lines = file1.readlines()
count = 0
for line in Lines:
    count += 1
    word = line.strip()
    word = word.lower()
    if "ä" in word:
        continue
    if "ü" in word:
        continue
    if "ö" in word:
        continue
    if "ß" in word:
        continue
    if len(word) == 5:
        words_5.append(word)

print("length", len(words_5))
print("value", get_str_value(words_5[0]), words_5[0], get_average(words_5))

avg = get_average(words_5)
errors = [(calc_error(w, avg), i, w) for i, w in enumerate(words_5)]

sorted_ = sorted(errors, key=lambda tup: tup[0])
print("words", sorted_[:10])


file1 = open('de_50k.txt', 'r')
words_freq = []
words_with_freq = []
Lines = file1.readlines()
for line in Lines:
    count += 1
    word = line.split(" ")[0]
    freq = int(line.split(" ")[1].strip())
    word = word.strip()
    word = word.lower()
    if "ä" in word:
        continue
    if "ü" in word:
        continue
    if "ö" in word:
        continue
    if "ß" in word:
        continue
    if len(word) == 5:
        words_freq.append(word)
        words_with_freq.append((word, freq))

print(len(words_with_freq), words_with_freq[:100])

runs = 15
picks_per_run = 80

for i in range(runs):
    random_avg = np.zeros(5, np.float64)
    for p in range(picks_per_run):
        random_avg += get_str_value(words_freq[random.randint(0, 999)])

    random_avg /= picks_per_run
    errors = [(calc_error(w, random_avg), k, w) for k, w in enumerate(words_5)]
    sorted_ = sorted(errors, key=lambda tup: tup[0])
    print("TRY ", i)
    print(random_avg)
    for k in range(2):
        print(sorted_[k])

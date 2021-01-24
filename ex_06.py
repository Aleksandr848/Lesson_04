from itertools import count
from itertools import cycle

for i in count(3):
    if i >= 10:
        break
    else:
        print(i, end = "  ")
print()

number_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

k = 1
for el in cycle(number_list):
    if k > len(number_list):
        break
    print(el, end = "  ")
    k += 1

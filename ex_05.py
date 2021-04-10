from functools import reduce
number_list = [el for el in range(100, 1001) if el % 2 == 0]
multiplication = reduce(lambda x, y: x * y, number_list)
print(number_list)
print(multiplication)
#
import random

list_1 = []
list_2 = []
common_list = []

for i in range(0, 10):
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    list_1.append(x)
    list_2.append(y)

for index in list_1:
    if index in list_2:
        if index not in common_list:
            common_list.append(index)

print(common_list)

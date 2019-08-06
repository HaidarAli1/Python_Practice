'''
number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for index in number_list:
    if int(index) < 5:
        new_list.append(index)
        print(str(index))

print(new_list)
'''

number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_input = int(input("Provide a number: " ))

for index in number_list:
    if int(index) < int(user_input):
        print(str(index))


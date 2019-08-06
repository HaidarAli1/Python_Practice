
'''
number = int(input("Choose a number: "))

if number % 2 == 0:
    if number % 4 == 0:
        print(str(number) + " is even, and a multiple of 4.")
    else:
        print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
'''

number_1 = int(input("Choose a number: "))
number_2 = int(input("Choose a previous number: "))

if number_1 % number_2 == 0:
    print(str(number_1) + " divides evenly into " + str(number_2))
else:
    print(str(number_1) + " doesn't divided evenly into " + str(number_2))
name = input("What is your name: ")
age = input("What is your age: ")
repeat = int(input("Amount of repeats: "))
one_hundered_years = (2019 - int(age)) + 100

for rep in range(repeat):
    print(str(name) + ", in the year " + str(one_hundered_years) + " you will be a 100!")



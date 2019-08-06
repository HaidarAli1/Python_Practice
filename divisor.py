user_input = int(input("Pick any number: "))
x = range(2, user_input)
list_of_divisors = []

for divisor in x:

    if user_input % divisor == 0:
        list_of_divisors.append(divisor)

print(list_of_divisors)
print("They're a couple of things you can do with the following file such as:\n append\n read\n write\n")
user_input = input("What would you like to do with this file: ")

user_input.lower()

if user_input == "read" or user_input == "r" or user_input == "reading":
    journal = open("journal.txt", "r")
    escape = 1
    while escape == 1:
        escape = 2
        read_user_input = input("Would you like to read one line, or the whole thing? ")
        read_user_input.lower()

        if read_user_input == "one line":
            print(journal.readline())
        elif read_user_input == "whole thing":
            print(journal.readlines())
        else:
            print("Invalid Input, retry.\n")
            escape = 1
    journal.close()
elif user_input == "append" or user_input == "app" or user_input == "a":
    journal = open("journal.txt", "a")
    escape_phrase = "yes"

    while escape_phrase == "yes" or escape_phrase == "y" or escape_phrase == "yea":
        journal.write(input("Words written into file: "))
        escape_phrase = input("Would you like to continue writing? ")

elif user_input == "write" or user_input == "writing" or user_input == "w":
    journal = open("journal.txt", "w")
    escape_phrase = "yes"

    while escape_phrase == "yes" or escape_phrase == "y" or escape_phrase == "yea":
        journal.write(input("Words written into file: "))
        escape_phrase = input("Would you like to continue writing? ")
    journal.close()
else:
    print("Invalid/Unknown Input")
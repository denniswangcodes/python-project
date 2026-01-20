# from math import *

# print("hello world")

# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /   |")
# print("/____|")

# character_name = "John" # string
# character_age = 35      # number
# is_male = True          # boolean
# print (f"There was once a man named {character_name}")
# print (f"he is {character_age} years old")

# print("She exclaimed \"Wow!\"")
# phrase = "Goodbye World"
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase.index("G"))
# print(phrase.replace("World", "Heaven"))
# print(10 % 3)
# print(str(5))
# print(pow(2, 3))
# print(abs(-5))
# print(round(3.7))
# print(max(4, 100))
# print(floor(3.7))
# print(ceil(3.8))
# print(sqrt(36))
# name = input("Enter your name: ")
# print(f"Hello {name}")
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# result = float(num1) + float(num2)
# print(result)

# lucky_numbers = [4, 8, 15, 100, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
# # print(friends[1:4])

# friends.extend(lucky_numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Oscar")
# friends.pop()
# # friends.clear()
# print(friends)
# print(friends.index("Karen"))
# print(friends.count("Jim"))
# lucky_numbers.sort()
# lucky_numbers.reverse()
# lucky_numbers.copy()
# print(lucky_numbers)

# tuple, immutable
# coordinates = (4, 5)
# print(coordinates)

# functions
# def greet(name: str, age: int):
#     print(f"Hi {name} you are {age} years old")
# greet("Mike", 30)
# def cube(num):
#     return num*num*num
# print(cube(2))

# conditionals
# is_male = False
# is_tall = False
# if is_male and is_tall:
#     print("You are either male or tall or both")
# elif is_male and not(is_tall):
#     print("You are male but not tall")
# elif not(is_male) and is_tall:
#     print("You are not a male but tall")
# else:
#     print("You are nothing")

# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3
    
# print(f"Biggest number is {max_num(2, 5, 9)}")

# dictionary
# monthConversions = {
#     "Jan": "January",
#     "Feb": "Feburary",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May"
# }

# print(monthConversions["Jan"])
# print(monthConversions.get("Feb"))

# looping
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#         print(f"You have {guess_limit - guess_count} gusses left!")
#     else: 
#         out_of_guesses = True

# if out_of_guesses:
#     print("You are out of gusses, sucker!")
# else:
#     print("You win!")

# for i in range(1, 6, 2):
#     print(i)
# for letter in ():
#     print(letter)

# ***for loop with length index steeps

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(matrix[0][0])

# def raise_to_power(base, pow):
#     result = 1
#     for index in range(pow):
#         result = result * base
#     return result
# print(raise_to_power(3, 2))

# try excep error handling

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError as err:
#     print(err)

# read from external file
# employee_file = open("sample.txt", "r") #or w or a for append

# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# write to external file
# employee_file = open("sample.txt", "a") #or w or a for append
# employee_file.write("\nToby")
# employee_file.close()

# Classes and Objects
# from Question import Question

# question_prompts = [
#     "What color are apples?\n(a) r\n(b) b\n(c) g",
#     "What color are blueberries?\n(a) r\n(b) b\n(c) g",
#     "What color are limes?\n(a) r\n(b) b\n(c) g",
# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "b"),
#     Question(question_prompts[2], "c")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print(f"You got {score} out of {len(questions)} correct!")

# run_test(questions)

# # Inheritance
# from Chef import Chef
# from ChineseChef import ChineseChef

# myChef = Chef()
# myChef.make_special_dish()

# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()

# Recursion
# access emails within emails

email_data = {
    "subject": "Hello",
    "from": "alice@example.com",
    "reply": {
        "subject": "Re: Hello",
        "from": "bob@example.com",
        "reply": {
            "subject": "Re: Re: Hello",
            "from": "carol@example.com"
        }
    }
}

def collect_emails(email):
    # start with current email
    emails = [email]
    count = 1

    # if there is a nested email, recurse
    if "reply" in email:
        child_count, child_emails = collect_emails(email["reply"])
        count += child_count
        emails += child_emails

    return count, emails

count, all_emails = collect_emails(email_data)

print("total email count:", count)

for e in all_emails:
    print(e["subject"])
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
i = 1
while i <= 10:
    print(i)
    i += 1

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")
print("You guessed it!")
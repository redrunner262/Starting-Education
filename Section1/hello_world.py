# PART 2
# print('Hello, world!')
# print('5'+ str(3))
# print(4 + 2.5)
# print(False)

# PART 3
# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# # PART 4
# name = input('What\'s your name? ')
# print('Nice to meet you, ' + name + "!")

# PART 5
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are not an adult.")

# PART 9: MINI PROJECT

name     = input("What is your name? ")
age      = int(input("What is your age? "))
message1 = "Hello, " + name + "! "

if age < 30:
    print(message1 + "You will be 30 years old in " + str(30 - age) + " years.")
elif age == 30:
    print(message1 + "You are 30 years old.")
else:
    print(message1 + "You were 30 years old " + str(age - 30) + " years ago.")
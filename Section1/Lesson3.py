# IF STATEMENTS: MAKING DECISIONS
# PROBLEM 1

# user_number = int(input("Enter a whole number. "))
# print("Is the entered number even or odd?")
# print("Even") if user_number % 2 == 0 else print("Odd")

# PROBLEM 2

# user_number_1 = int(input("Enter a whole number. "))
# user_number_2 = int(input("Enter another whole number. "))

# if user_number_1 > user_number_2:
#     print(f"The larger number is: {user_number_1}")
# elif user_number_1 < user_number_2:
#     print(f"The larger number is: {user_number_2}")
# else:
#     print("The two numbers are equal.")

# PROBLEM 3

# user_score = int(input("Enter your test score. "))

# if user_score < 0:
#     print("Enter a positive number score.")
# elif user_score > 100:
#     print("Enter a score less than or equal to 100.")
# elif user_score >= 90:
#     print("You got an A!")
# elif user_score >= 80:
#     print("You got a B.")
# elif user_score >= 70:
#     print("You got a C.")
# elif user_score >= 60:
#     print("You got a D...")
# else:
#     print("You got an F. How disappointing.")

# PROBLEM 4

# user_age = int(input("Enter your age. "))

# if user_age >= 0 and user_age <= 12:
#     print("You are a child.")
# elif user_age >= 13 and user_age <= 19:
#     print("You are a teen.")
# elif user_age >= 20 and user_age <= 64:
#     print("You are an adult.")
# else:
#     print("You are a senior.")

# PART 2: FOR LOOPS
# PROBLEM 5

# for num in range(1, 11):
#     print(num)

# PROBLEM 6

# list_nums = [2, 4, 6, 8, 10]

# for num in list_nums:
#     print(num)
#     print(num ** 2)

# PROBLEM 7

# the_numbers = [4, 8, 15, 16, 23, 42]
# the_numbers_sum = 0
# for number in the_numbers:
#     the_numbers_sum += number

# print(the_numbers_sum)

# PROBLEM 8

# list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in list_numbers:
#     if number % 2 == 0:
#         print(number)

# PART 3: WHILE LOOPS

# PROBLEM 9

# from random import randint

# result = False

# while result == False:
#     user_num = int(input("Guess a number between 1 and 3, inclusive. "))
#     secret_num = randint(1, 3)
#     if user_num < 1 or user_num > 3:
#         print("Silly goose! Guess a number in the stated range :)")
#         result == False
#     else:
#         print(f"The secret number this time is: {secret_num}")
#         if user_num == secret_num:
#             print("You guessed correctly!")
#             result == True
#         else:
#             print("Try again.")
#             result == False

# PROBLEM 10

# user_start_num = int(input("Enter a positive whole number. "))

# if user_start_num < 0:
#     print("Enter a positive number, I said.")
# elif user_start_num > 1000:
#     print("Whoa! That's too high a number. Pick a number lower than 1,000.")
# else:
#     while user_start_num >= 0:
#         print(user_start_num)
#         user_start_num -= 1

# PART 4: LOOP CONTROL

# PROBLEM 11

# for i in range(1, 11):
#     print(i)
#     if i == 5:
#         break

# PROBLEM 12

# for i in range(1, 11):
#     if i % 2 == 1:
#         continue
#     print(i)

# PART 5: COMBINED CHALLENGE

# PROBLEM 13
# user_choice = 0

# while user_choice != 3:
#     print("Select an option:\n1. Say Hello\n2. Add Two Numbers\n3. Quit")
#     user_choice = int(input("Enter a whole number between 1 and 3, inclusive. "))
#     if user_choice == 1:
#         print("Hello!")
#     elif user_choice == 2:
#         num_choice_1 = int(input("Enter a number. "))
#         num_choice_2 = int(input("Enter another number. "))
#         print(f"The sum of your numbers is: {num_choice_1 + num_choice_2}")
#     elif user_choice == 3:
#         print("Quitting this program.")
#         break
#     else:
#         print("You disobeyed. This round is over. Harumph.")
#         break
# STRINGS
# PROBLEM 1
# message = "Python Programming"
# first_6 = message[0:6]
# print(first_6)
# spl_message = message.split()
# print(spl_message[1])

# new_list = []
# message_index = 0
# for letter in message:
#     if message_index % 2 != 0:
#         new_list.append(letter)
#     message_index += 1

# new_str = ""
# for letter in new_list:
#     new_str = new_str + letter

# print(new_str)

# reverse_message = message[::-1]
# print(reverse_message)


# PROBLEM 2
# user_text = " Hello WORLD! This is Python! "
# user_text_1 = user_text.strip().lower()
# print(user_text_1)
# user_text_2 = user_text_1.replace("!", ".")
# print(user_text_2)
# user_text_3 = user_text_2.replace(".", "").split()
# print(user_text_3)
# user_text_4 = user_text_2.count("o")
# print(user_text_4)

# PROBLEM 3
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# full_name = first_name + " " + last_name
# # I could use first the separated first and last name variables, but let's manipulate full_name for a challenge.
# names = full_name.split()
# last_first = names[1] + ", " + names[0]
# print(last_first)
# initials = names[0][0] + "." + names[1][0] + "."
# print(initials)
# name_only_chars = full_name.isascii()
# print(name_only_chars)
# names_list = full_name.split()
# len_name_chars = len(names_list[0] + names_list[1])
# print(len_name_chars)

# NUMBERS
import math
# PROBLEM 4
# item_1 = 12.99
# item_2 = 8.50
# item_3 = 15.75
# total_all_three = item_1 + item_2 + item_3
# print(total_all_three)
# discounted_total = total_all_three * 0.85
# print(discounted_total)
# taxed_total = discounted_total * 1.085
# print(taxed_total)
# rounded_total = round(round(taxed_total, 4), 3)
# rounded_total = round(rounded_total_1, 2)
# print(rounded_total)

# PROBLEM 5
# from datetime import *
# user_age = input("What is your age? ")
# # user_birth_month = input("What is the number of the month in which you were born? ")
# # user_birth_month_int = int(user_birth_month)
# user_age_str = str(user_age)
# user_age_int = int(user_age)
# print(user_age_int)
# age_int_check = str(type(user_age_int))
# print(age_int_check)
# year_now = datetime.now().year
# # month_now = datetime.now().month # I didn't finish considering the month. I know I could figure it out, but for the sake of time, I moved on.
# # ym_now = year_now + round((month_now / 12), 2)
# # user_age_ym = user_age_int + (1 - (user_birth_month_int / 12)) # End of code in progress considering the month into a person's age and birth year.
# if age_int_check == "<class 'int'>":
#     print("Conversion succeeded.")
#     birth_year = year_now - user_age_int
#     print(f"The year you were born is {birth_year}.")
# else:
#     print("Conversion failed. Please enter your age in numbers only.")
#     age_int_check = False

# PROBLEM 6
# temp_celsius_input = input("What is the current temperature in degrees Celsius? ")
# temp_celsius = int(temp_celsius_input)
# convert_to_f = ((temp_celsius * 9/5) + 32)
# print(convert_to_f)
# convert_to_k = temp_celsius + 273.15
# print(convert_to_k)
# all_temps = [round(temp_celsius, 1), round(convert_to_f, 1), round(convert_to_k, 1)]
# print(all_temps)
# if temp_celsius <= 0:
#     print("The temperature is below freezing.")
# elif temp_celsius >= 20 and temp_celsius <= 25:
#     print("The temperature is room temperature.")
# elif temp_celsius >= 30:
#     print("The temperature is hot.")
# else:
#     print("The temperature is in a non-normal zone.")

# BOOLEANS
# PROBLEM 7
# student_gpa = round(float(input("What is your GPA? ")), 2)
# student_credits = int(input("How many credit hours have you completed, rounded down to the nearest whole number? "))
# student_year = int(input("What is the number of the year you are in, from 1 to 4? "))
# eligible = False
# if student_gpa >= 3.5 and student_credits >= 60:
#     eligible = True
# elif student_gpa > 3.0 and student_year == 4:
#     eligible = True
# else:
#     eligible = False
# print(eligible)

# PROBLEM 8
# my_list = [0, "", [], None, "hello", [1, 2, 3], -1, 0.0]
# truthy_values = 0
# falsy_values = 0
# for item in my_list:
#     if bool(item) == True:
#         print(True)
#         truthy_values += 1
#     else:
#         print(False)
#         falsy_values += 1

# print("There are " + str(truthy_values) + " truthy values and " + str(falsy_values) + " falsy values.")

# PROBLEM 9
# user_password = input("Enter your password. ")
# uppers = 0
# lowers = 0
# digits = 0
# if len(user_password) >= 8:
#     for char in user_password:
#         if char.isupper():
#             uppers += 1
#         if char.islower():
#             lowers += 1
#         if char.isdigit():
#             digits += 1
#     if uppers > 0 and lowers > 0 and digits > 0:
#         print("Password is strong.")
#     elif uppers == 0:
#         print("Provide at least one uppercase letter.")
#     elif lowers == 0:
#         print("Provide at least one lowercase letter.")
#     elif digits == 0:
#         print("Provide at least one digit.")
#     else:
#         print("Password is weak. Create a stronger password.")
# else:
#     print("Password length must be 8 digits or more.")

# LISTS
# PROBLEM 10
# shopping = ["milk", "bread", "eggs", "butter", "cheese"]
# new_list_1 = shopping + ["apples", "bananas"]
# # print(new_list_1)
# new_list_2 = new_list_1
# new_list_2.insert(1, "yogurt")
# # print(new_list_2)
# new_list_3 = new_list_2
# new_list_3.remove("bread")
# # print(new_list_3)
# new_list_4 = new_list_3
# new_list_4.sort()
# # print(new_list_4)
# total_len = len(new_list_4)
# print(total_len)

# PROBLEM 11
# numbers = []
# sum_remaining_numbers = 0
# for number in range(1, 11):
#     numbers.append(number ** 2)
#     if number ** 2 > 50:
#         numbers.remove(number ** 2)
#         sum_remaining_numbers += (number ** 2)

# print(numbers)
# print(sum_remaining_numbers)
# print("The minimum value is " + str(numbers[0]) + ".\nThe maximum value is " + str(numbers[-1]) + ".")

# PROBLEM 12
# scores = [85, 92, 78, 96, 88, 76, 94, 89, 82, 90]
# total = 0
# above_avg = 0
# Ninety_or_higher = []

# for score in scores:
#     total += score
#     if score >= 90:
#         Ninety_or_higher.append(score)

# average = total / len(scores)

# for score in scores:
#     if score > average:
#         above_avg += 1

# print(average)
# print(above_avg)
# print(Ninety_or_higher)

# grade_a = [90, 100]
# grade_b = [80, 89]
# grade_c = [70, 79]
# grade_d = [60, 69]
# grade_f = [0, 59]

# scores_grades = []

# for score in scores:
#     if score >= grade_a[0] and score <= grade_a[1]:
#         scores_grades.append("A: " + str(score))
#     if score >= grade_b[0] and score <= grade_b[1]:
#         scores_grades.append("B: " + str(score))
#     if score >= grade_c[0] and score <= grade_c[1]:
#         scores_grades.append("C: " + str(score))
#     if score >= grade_d[0] and score <= grade_d[1]:
#         scores_grades.append("D: " + str(score))
#     if score >= grade_f[0] and score <= grade_f[1]:
#         scores_grades.append("F: " + str(score))

# print(scores_grades)

# DICTIONARIES
# PROBLEM 13
# student = {"name" : "Alice", "age" : 20, "major" : "Computer Science"}
# student.update({"gpa" : 3.7})
# student.update({"age" : 21})
# student["courses"] = ["Econ 101", "Sales 101", "Physics 101"]
# student_keys = student.keys()
# student_values = student.values()

# print(student)
# print(student_keys)
# print(student_values)

# PROBLEM 14
# inventory = {"apples": 50, "bananas": 30, "oranges": 25, "grapes": 40, "strawberries": 15}
# highest_qty_key = ""
# highest_qty_val = 0
# total_qty = 0
# more_than_twenty = {}

# for key, value in inventory.items():
#     print("Item: " + key + ", Quantity: " + str(value))
#     if value >= highest_qty_val:
#         highest_qty_val = value
#         highest_qty_key = key
#     total_qty += value
#     if value > 20:
#         more_than_twenty[key] = value

# print("The item with the highest quantity is: " + str(highest_qty_key))
# print("The total quantity of all fruits is: " + str(total_qty))
# print("The fruits with quantities of more than 20 are:")
# print(more_than_twenty)

# PROBLEM 15
# student_scores = {"Adam": [100, 92, 97], "Colby": [85, 79, 93], "Chris": [98, 94, 100]}
# student_scores.update({"Shannon": [100, 99, 100]})
# student_names = student_scores.keys()
# averages = {}
# highest_avg_score = 0
# highest_avg_student = ""

# for student, scores in student_scores.items():
#     average = 0
#     for score in scores:
#         average += score
#     average = round(average / len(scores), 2)
#     averages[student] = average

# print(averages)

# for student, average in averages.items():
#     if average > highest_avg_score:
#         highest_avg_score = average
#         highest_avg_student = student

# print("The student with the highest average score is: " + highest_avg_student)

# print("Here is a report of each student with his or her average score.")
# for student, average in averages.items():
#     print(f"{student} has an average score of {average}.")
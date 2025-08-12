# PART 1: DEFINING & CALLING FUNCTIONS

# PROBLEM 1

# def greet(name):
#     print(f"Hello, {name}! Welcome!")

# # PROBLEM 2

# def add_numbers(num_1, num_2):
#     print(num_1 + num_2)

# # PROBLEM 3

# def say_hello(name = "friend": str):
#     print(f"Hello, {name}!")

# # PART 2: PARAMETERS, ARGUMENTS & RETURN VALUES

# # PROBLEM 4

# def square(num: int):
#     return num ** 2

# # PROBLEM 5

# def personalized_message(name, age):
#     return f"{name} is {age} years old."

# # PROBLEM 6

# def get_min_max(lst: list):
#     return min(lst), max(lst)

# # PART 3: LOCAL AND GLOBAL VARIABLES

# # PROBLEM 7

# def show_local_var():
#     local_var = "Desert"
#     print(local_var)

# print(local_var)
# The local variable does not exist outside the function.

# PROBLEM 8 (incomplete)

counter = 0

def increment_counter():
    # new_count = counter + 1
    # return new_count
    global counter
    counter += 1

increment_counter()
print(counter)
increment_counter()
print(counter)

# PART 4: WORKING WITH DATA IN FUNCTIONS

# PROBLEM 9
# __doc__ = """Function capitalizes the first letter of each name in a list of names.
# Parameter(s): List of names
# Returns: List of names with each first letter capitalized"""

# # Define the function and provide the parameter
# def capitalize_names(lst_names: list):
#     # Create an empty list for the function to fill in each round of a loop.
#     lst_new_names = []
#     # Loop through the provided list of names.
#     for name in lst_names:
#         # Capitalize a name in the list of names.
#         cap_name = name.capitalize()
#         # Add the newly-capitalized name to the list created at the function's call as the last item in the list.
#         lst_new_names.append(cap_name)
#     # Return the resulting list of capitalized names.
#     return lst_new_names

# # print(capitalize_names(["eric", "chris"]))

# # PROBLEM 10

# def describe_person(dict_name_age: dict):
#     for name, age in dict_name_age.items():
#         return f"{name} is {str(age)} years old."

# # print(describe_person({"chris": 33}))

# # PART 5: WRITING CLEAR FUNCTIONS

# # PROBLEM 11

# # Refer to Problem 9's docstring.
# # Refer to Problem 9's comments throughout the function definition.

# # PART 6: TESTING YOUR FUNCTIONS

# # PROBLEM 12

# greet("Mainville")

# add_numbers(11, 8)

# say_hello()
# say_hello("Micah")

# print(square(5))

# print(personalized_message("Jeremy", 50))

# print(get_min_max([1, 2, 4, 8, 0, 10, 7, 4]))
# print(get_min_max(["Andrew", "Zedekiah", "Michael"]))

# show_local_var()

# # increment_counter()
# # print(counter)
# # increment_counter()
# # print(counter)

# print(capitalize_names(["rachel", "ashley", "angela"]))

# print(describe_person({"Matt Walsh": 38}))
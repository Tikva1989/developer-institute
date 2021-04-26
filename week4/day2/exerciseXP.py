# #                         Exercise 1 : Favorite Numbers
# # creat set:
# my_fav_numbers = {2, 7, 3, 36}
#
# # add two numbers to the set:
# my_fav_numbers.add(18)
# my_fav_numbers.add(83)
#
# # Remove the last number:
# my_fav_numbers.remove(83)
#
# #creat my frinds number:
# friend_fav_numbers = {8, 9, 3, 434}
#
# # concatenate both sets:
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
#
# print(our_fav_numbers)

#                Exercise 2: Tuple
# Given a tuple which value is integers,
# is it possible to add more integers to the tuple?
# tuple items are ordered, unchangeable and allow duplicate values.
# can't change, add or remove items once has been created.

#                   Exercise 3: Print A Range Of Numbers
# Use a for loop to print all numbers from 1 to 20, inclusive

# numbers = list(range(1,21))
# for number in numbers:
#     print(number)

#                   Exercise 4: Floats

# Recap – What is a float? What is the difference between an integer and a float?
# float number are numbers which are positive or negative containing one or more decimals.
# x = 2.28
# integer number is a whole number, positive or negative, with unlimited length.
# y = 598
# 2. Can you think of another way to generate a sequence of floats?
#  https://www.techbeamers.com/python-float-range/

# # 3. Create a list containing the following
# sequence = ( 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 )
# # (don’t hard-code the sequence
# sequence_1 = list(range(1.5,5.5,0.5))
# print(sequence_1)

# #                               Exercise 5: Shopping List
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # 1. Remove “Banana” from the list
# basket.pop(0)
#
# # 2. Remove “Blueberries” from the list
# basket.pop()
#
# #3. Add “Kiwi” to the end of the list.
# basket.append("Kiwi")
#
# # 4. Add “Apples” to the beginning of the list
# basket.insert(0, "Apples")
#
# #5.  Count how many apples are in the basket.
# count_Apples= basket.count("Apples")
#
# #6. Empty the basket
# basket.clear()
# print(basket)

# #                                   Exercise 6 : Loop
# # Write a while loop that will continuously ask the user for their name,
# # unless the input is equal to your name.
#
# user_name = input("What is your name?")
# my_name = "Tikva"
# while user_name != my_name:
#     user_name = input("What is your name?")
# print("We have the same name!")

#                                       Exercise 7
# Given a list, use a loop to print out every element which has an even index.
# numbers = [2, 3, 4, 6, 43, 43, 87, 23, 98]
# index = 0
# for number in numbers:
#     print(index, number)
#     index += 2
#                                      Exercise 9: Favorite Fruits

# 1. Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits
# with a single space.
# #2. Store the favorite fruit(s) in a list
# fav_fruits = input("Type your favorite fruit(s) separete with single space:")
# list_fav_fruits = fav_fruits.split()
# user_fruit = input("Enter a fruit name:").casefold()
# if user_fruit in list_fav_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")


#                        Exercise 10: Who Ordered A Pizza ?

# 1. Write a loop that asks a user to enter a series of pizza toppings,
# when the user inputs ‘quit’ stop asking for toppings.
# #
# active = True
# topping_counter =[]
# while active:
#     user_input = input("Enter pizza topping (enter 'quit' when you are finished): ")
#
#     if user_input == 'quit':
#         active = False
#         total_cost = len(topping_counter) * 2.5 + 10
#     else:
#         print(f'{user_input} added to your pizza!')
#         topping_counter.append(user_input)
# print(f' total cost is {len(topping_counter)*2.5 + 10}')



#                                               Exercise 11: Cinemax

# family_age = [12, 24, 50, 2, 1]
# for age in family_age :
#     if age < 3 :
#         age_under_3.append(age)
#         print(age_under_3)


#                                               Exercise 12 : Who Is Under 16???????????????????????????
# names = ["Benny", "Manny", "Shanty", "Donna"]
# age_list =[]
# for name in names:
#     age = int(input(f'{name} Enter your age:'))
#     age_list.append((age))
#     for age in list(age_list):
#         if age < 16:
#             names.remove(name)"pastrami"
#             print(names)

#                                                   Exercise 13:
# sandwich_orders = ["omllet", "chees", "turkey"]
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)
# print("\n")
# for sandwich in finished_sandwiches:
#     print("i made a "+sandwich + " sandwich.")

#                                                      Exercise 14??????????
#1. Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.




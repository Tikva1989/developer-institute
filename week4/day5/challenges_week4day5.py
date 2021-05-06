#           Challenges:
import math

# #1. Insert item at a defined index in a list:
# my_list = ['a', 'b', 'c']
# my_list.insert(2, 'b1')
# print(my_list)

# # 2. Write a script that counts the number of spaces in a string:
# my_str = " I L ove spaces"
# spaces = my_str.count(" ")
# print(spaces)

# # 3. Write a script that calculates the number of upper case letters and lower case letters in a string
# def test_string(str):
#     d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
#     for letter in str :
#         if letter.isupper():
#             d["UPPER_CASE"]+= 1
#         elif letter.islower():
#             d["LOWER_CASE"]+= 1
#         else:
#             pass
#     print("String to check:", str)
#     print("UPPER CASES:", d['UPPER_CASE'])
#     print("LOWER CASE:", d['LOWER_CASE'])
#
# my_str = "I loVe BanaNA"
# test_string(my_str)

# # 4. Write a function to find the sum of an array without using the built in function:
# my_array = [1, 5, 4, 2]
# def my_sum(array):
#     counter = 0
#     for i in array:
#         counter = counter + i
#
#     return counter
#
# print(my_sum(my_array))

# # 5.Write a function to find the max number in a list
# my_list = [0, 7, 3, 50]
# def find_max (list):
#     current_max = 0
#     for i in list:
#         while i > current_max:
#             current_max = i
#     return current_max
#
# print(find_max((my_list)))

# # 6. Write a function that returns factorial of a number
#
# def factorial_schem(num):
#     counter = num -1
#     factorial = num
#     while counter != 0:
#         factorial =factorial * counter
#         counter -= 1
#     return factorial
#
# print(factorial_schem(3))

# # 7 . Write a function that counts an element in a list (without using the count method):
# def list_count(lis):
#     return len(lis)
# my_list = [['a','a','t','o'],'a',[1, 5, 6]]
# print(list_count(my_list))

# # 8. Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
# def  l2_norm(list):
#     total_sum = 0
#     for i in list:
#         x = i**2
#         total_sum = total_sum + x
#     return math.sqrt(total_sum)
# list = [1, 2, 2]
# print(l2_norm(list))

# 9. Write a function to find if an array is monotonic (sorted either ascending of descending)


# #10. Write a function that prints the longest word in a list.
# def longest_word(lis):
#         longest_word = ''
#         x = len(longest_word)
#         for word in lis:
#                 if x < len(word):
#                     longest_word = word
#         return longest_word
# my_lis = ["so", "much",  "love", "sunday"]
# print(longest_word(my_lis))

# # 11. Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
# my_mix_list = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
# list_integer = []
# list_string = []
# def  is_int_or_is_string(list):
#     for  item in list:
#         if isinstance(item, int):
#             list_integer.append(item)
#         elif isinstance(item, str):
#             list_string.append(item)
#
#     print(list_integer)
#     print(list_string)
#
# is_int_or_is_string(my_mix_list)

# 12. Write a function to check if a string is a palindrome:
# def is_string_palindrome(string):
#     for i in range(0, int(len(string)/2)):
#         if string[i] != string[len(string)-i-1]:
#             return False
#     return True
#
# print(is_string_palindrome("radar"))

# # 13. Write a function that returns the amount of words in a sentence with length > k:
# def sum_over_k(sentence , k ):
#     word_in_rule = []
#     new_sentence = sentence.split(" ")
#     for word in new_sentence:
#         if len(word) > int(k):
#             word_in_rule.append(word)
#     return len(word_in_rule)
#
# print(sum_over_k( 'Do or do not there is no try', 2))

# # 14. Write a function that returns the average value in a dictionary (assume the values are numeric):
# my_dict= {
#         'a': 1,
#         'b':2,
#         'c':8,
#         'd': 1
# }
# def dict_ave(dict):
#     lis_values= dict.values()
#     lis_keys= dict.keys()
#     return sum(lis_values) // int(len(lis_keys))
#
# print(dict_ave(my_dict))

# 15. Write a function that returns common divisors of 2 numbers:
# 16.

# #17. Write a function that prints elements of a list if the index and the value are even:
my_list = [1,2,2,3,4,5]
# def weird_print(list):
#     even_list =[]
#     for index, element  in enumerate(list):
#         if index %2==0 and element%2==0:
#             even_list.append(element)
#     return even_list
#
# print(weird_print(my_list))

#         #using comprihansion:
# even_lis = [element for index,element in enumerate(my_list) if index %2==0 and element%2==0]
# print(even_lis)


# #18. Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
# # type_count(a=1,b='string',c=1.0,d=True,e=False)
# def type_count(**kwargs):
#     types_value = []
#
#     for value in kwargs.values():
#             types_value.append(type(value))
#     for item in types_value:
#          print(types_value.count({item}))
#
#         # print(type)
# type_count(a=1,b='string',c=1.0,d=True,e=False)

# 19. Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def my_split(*args):
    


# # 20. Convert a string into password format.
# password_user = input("please enter a password:")
# formated_pass = len(password_user)* '*'
# print(formated_pass)

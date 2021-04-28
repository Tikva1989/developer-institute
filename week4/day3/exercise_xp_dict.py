#  # Exercise 1
# #replace the first 20 showen with 200 :
# list = [5, 10, 15, 20, 25, 50, 20]
# print(list.index(20))
# list.insert(3, 200)
# list.pop(4)
# print(list)

# #Exercise:
# #Unpack the following tuple into 4 variables
# a_tuple = (10, 20, 30, 40)
# a, b, c, d = a_tuple
# print(a)
# print(b)
# print(c)
# print(d)
## tuple unpacking:

# for num in range(0,5):
#     print (num)
# for our_tuple in enumerate('abcde'):
#     print(our_tuple)
#
# for our_tuple in enumerate('abcde'):
#     index, letter = our_tuple
#     print(index, letter)
#
#
#
# for index, letter in enumerate('abcde'):
#     print(index,letter)
#given the list write a code to sum the items:

# numbers = [1, 2, 3, 4, 5]
# our_total = 0
# for number in numbers:
#     our_total += number
# print(our_total)

# numbers = list(range(45, 100))
#
# # find the minimum number in that range:
# current_min = numbers[0]
# for number in numbers:
#     if number < current_min:
#         current_min = number
# print(current_min)
#
# #find the maximun number in a givenlist and then print it:
# current_max = numbers:
# for number in numbers :
#     if number

# While example:
#
# password = ''
# while password != 'hello-world-123':
#   password = input('What is the top secret password? ')
#
# print('You guessed the right password!')

# # Exercise:
# x = 1
# while x <= 10:
#     print(x)
#     x += 1

# flag example:
# active = True
#
# while active:
#     user_input = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if user_input in ['quit', 'leave me alone', 'stop']:
#         active = False
#     else:
#         print("I'd love to go to", user_input)
#
# print("Goodbye !")

# numbers = list(range(0,10))
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print(number)
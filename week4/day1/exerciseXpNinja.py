# # Exercise 3 : Outputs
#
# print( 3 <= 3 < 9)  # true
# print(3 == 3 == 3)   #true
# print(bool(0))       #flase
# print(bool(5 == "5")) # false
# print(bool(4 == 4) == bool("4" == "4")) #true
# print(bool(bool(None)))   #false!!!
# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10
# print("x is", x)   # x is true
# print("y is", y)   # y is false
# print("a:", a)     # a: 5

# #Exercise 4 : How Many Characters In A Sentence ?
# my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco
#            laboris nisi ut aliquip ex ea commodo consequat.
#            Duis aute irure dolor in reprehenderit in voluptate velit
#            esse cillum dolore eu fugiat nulla pariatur.
#            Excepteur sint occaecat cupidatat non proident,
#            sunt in culpa qui officia deserunt mollit anim id est laborum."""
# print(len(my_text))

#Exercise 5: Longest Word Without A Specific Character

# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
# user_sentence = input("Type the longest word without the character 'A':")
# x = len(user_sentence)
# x=0
# while x < len(user_sentence) and "A" not in user_sentence:
#         print("congratulations ")
#         x += len(user_sentence)
# else:
#     print("Your new value isn't the longest")
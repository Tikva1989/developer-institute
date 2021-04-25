# # Exercise 1 : Hello World
# print("hello world \n " * 4)
#
# # Exercise 2 : Some Math
# # Write code that calculates the result of: (99^3) * 8
# x = (99**3)*8
# print(x)
#
# # Exercise 3 : What Is The Output ?
# print(5 < 3)      #fals
# print(3 == 3)   #true
# print(3 == "3")   #false
# print("Hello" == "hello")  #false

# #Exercise 4 : Your Computer Brand
# computer_brand = "lenevo"
# print("i have a "+ computer_brand+" computer.")

# # Exercise 5 : Your Information
# name = "tikva"
# age = "31"
# shoe_size = "37"
# info = f'my name {name} age {age} and my shoe size {shoe_size}'
#
# print(info)

# # Exercise 6 : A & B
# #
# a = 8
# b = 5
# if (a > b) :
#     print("hello world")

# # Exercise 7 : Odd Or Even
# # Write code that asks the user for a number and determines whether this number is odd or even.
# num = int(input("Enter a number:"))
# remain = num % 2
# if remain == 0:
#     print("number is even")
# else:
#     print("number is odd")

# # Exercise 8 : What’s Your Name ?
# # Write code that asks the user for their name and determines whether or not you have the same name,
# # print out a funny message based on the outcome.
# user_name = input("what is your name?").lower()
# my_name = "tikva"
# if user_name == my_name :
#     print ("Awesome!")
# else:
#     print("your name isn't like main...your loss hihihi!!")

# #Exercise 9 : Tall Enough To Ride A Roller Coaster
# # Write code that will ask the user for their height in inches.
# height = int(input("What is your height in inches?"))
# # If they are over 145cm print a message that states they are tall enough to ride.
# # If they are not tall enough print a message that says they need to grow some more to ride.
# if height > 145 :
#     print("You are tall enough to ride")
# else:
#     print("You need to grow some more to ride")
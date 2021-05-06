#                   Challenges

# 1. list.insert(i, item)

#2. count the number of spaces in a string:
string = "i Dont Get The She dfds"
# print(string.count(" "))

#3.Write a script that calculates the number of upper case letters and lower case letters in a string.

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
# string_test(string)
#
# # 4.  whrit a sum function:
# my_sum= ([1,5,4,2])
# my_sum_1 = lambda a, b, c, d : a+b+c+d
# print(my_sum_1(1,5,4,2))

# 5. Write a function to find the max number in a list:
# find_max=[0,1,3,50]
# def my_max(list):
#     highest_max =0
#     for i in find_max:
#         if i > highest_max:
#             highest_max = i
#     return highest_max
#
# print(my_max(find_max))

# 6. Write a function that returns factorial of a number:
def factorial (num):
    i = 1

    while i < num:
        factorial_res= i * num

        i += 1
        return factorial_res
print(factorial(4))

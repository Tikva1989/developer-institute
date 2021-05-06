#===================== Exercise XP # 2  =================
import datetime
# # Create a function that displays the current date.
# def current_date():
#     return  datetime.date.today()


# # Create a function that displays the amount of time left from now until January 1st.
# # (Example: the 1st of January is in 10 days and 10:34:01hours).
#
# def time_left():
#         now = datetime.datetime.now()
#         end_date =  datetime.datetime(2022, 1, 1)
#         left_time = end_date - now
#         print(f" the 1st of January is in {left_time}hours ")
##
# time_left()

#Create a function that accepts a birthdate as an argument (in the format of your choice),
# then display a message stating how many minutes the user has been alive.

# def lived_minutes(birthdate="dd/mm/yyyy"):
#         ''''info:  calculate the  minutes from birthday till now
#         write your birthdate in format  dd/mm/yyyy '''
#         birthday= datetime.datetime.strptime(birthdate, "%d/%m/%Y")
#         today =  datetime.datetime.now()
#         delta = today - birthday
#         print(f"You lived in earth for {delta.total_seconds()//60} total minutes")
#
# lived_minutes('07/09/1989')

#======================= Exercise 4===============================
# Write a function that display today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

# def next_holiday():
#         now = datetime.datetime.now()
#         shavuot = datetime.datetime(2021, 5, 16, 00, 00,  00)
#         delta = shavuot - now
#         print(f'Today is {now.strftime("%d/%m/%Y")} the next holiday Shavuot in {delta} hours ')
#
# next_holiday()

#===================== Exercise 5 : How Old Are You On Jupiter? ============


# #===================== Exercise 6 : Faker Module =========================
# from faker  import Faker
#
# fake_users = Faker()
# #creat a class for the user's details
# class User():
#     def __init__(self, name, address, language_code):
#         self.name = name
#         self.address = address
#         self.language_code = language_code
#
#     def __repr__(self):
#         return 'name: {}, address: {}, language_code: {},'.format(self.name, self.address, self.language_code)
#
# #function to creat a list of users
# users_list = []
# def create_user_list():
#     for i in range(5):
#             users_list.append(User(fake_users.name(), fake_users.address(), fake_users.language_code()))
#     for i in users_list:
#         print(i, "\n")
#
# create_user_list()
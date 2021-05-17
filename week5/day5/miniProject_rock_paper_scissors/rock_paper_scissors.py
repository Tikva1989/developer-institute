import game

#this should display a simple menu, get the user’s choice (with data validation), and return the choice
def get_user_menu_choice():
    print('''  menu
    (g) Play a new game
    (x) Show scores and exit
    ''')
    user_choice =input("Type here:  ")
    if user_choice == 'g':
            return 'g'
    elif user_choice == 'x':
            return 'x'
    else:
        try:
            user_choice = str(user_choice) and len(user_choice)==1
        except ValueError:
             print("Sorry, Typed value is not valid choose.Making an exit")
             user_choice ='x'
             return user_choice


#print the results of the games played. It should have a single parameter named results; which will be a dictionary
# of the results of the games played. It should display these results in a user-friendly way
def print_results(object):
    for k,v in object.results.items():
        print(f"{k} {v} time(s)")
    print("Thank you gor playing!")



def main():
    new_game = game.Game('results')
    game.Game.play(new_game)
    while True:
          user_choice= get_user_menu_choice()
          if user_choice == 'x':
                print_results(new_game)
                break
          if user_choice == 'g':
                game.Game.play(new_game)




main()








import random

class Game():
        def __init__(self, results):
                self.results =  {'win': 0, 'loss': 0, 'draw': 0}



        def get_player_item(self):
               item_option = ['r', 'p', 's']
               while True:
                        user_item = input("Pleas select item ( r )ock ,  ( p )aper , ( s )cissors:  ")
                        try:
                                if user_item in item_option:
                                          return user_item
                                else:
                                          print("Don't be silly! ")
                        except ValueError:
                               print("Don't be silly! Select item ( r )ock ,  ( p )aper , ( s )cissors")


        @staticmethod
        def get_computer_item():
                computer_item = random.choice(['r', 'p', 's'])
                return computer_item

        def get_game_result(self, user_item, computer_item):
                if user_item == computer_item:
                    self.results['draw']+= 1
                    return "draw"
                # win_situations = {"r " > "s", "s" > "p", "p" > "r"}
                elif (user_item== 'r' and computer_item =='s')or (user_item=='s' and computer_item=='p')or( user_item=='p' and computer_item=='r'):
                    self.results['win'] += 1
                    return 'win'
                else:
                    self.results['loss'] += 1
                    return 'loss'

        def play(self):

            user_item = self.get_player_item()
            computer_item = self.get_computer_item()
            game_results =self.get_game_result(user_item,computer_item)
            if game_results == "win":
                   print("You selected '{}'. The computer selected '{}'. You Won!".format(user_item, computer_item))
            elif game_results == "loss":
                    print("You selected {}. The computer selected '{}'. You Loss!".format(user_item, computer_item))
            elif game_results == "draw":
                print("You selected '{}'. The computer selected '{}'. You drew!".format(user_item, computer_item))
            return game_results







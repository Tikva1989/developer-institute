import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']


def get_word():
    word = random.choice(wordslist)
    return word.lower()


def play(word):
    hidden_word = list('*' * len(word))
    guessed = False
    tries = 6
    guessed_letters = []

    while not guessed and tries > 0:
        guess = input("Please guess a letter:").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(hidden_word)
                # comprihension to store the index
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                hidden_word = "".join(word_as_list)
                if '*' not in hidden_word:
                    guessed = True
        else:
            print("Not a valid guess.")
            tries -= 1
        print(display_hangman(tries))
        print(hidden_word)

    if guessed:
        print("You guessed right, you WIN!")
    else:
        print("Sorry, you ran out of tries. The word was", word)

def display_hangman(tries):
    stages  = [
        #final: head, body, left arm,right arm, right leg, left leg
        '''
        ------------
        |           |   
        |           O
        |          \\|/
        |           |
        |          / \\
        _  
        ''',
        # head, body, left arm,right arm, right leg
        '''
        ------------
        |           |   
        |           O
        |          \\|/
        |           |
        |            \\
        _  
        ''',
        #  head, body, left arm,right arm
        '''
        ------------
        |           |   
        |           O
        |          \\|/
        |           |
        |          
        _  
        ''',
        #  head, body, left arm
        '''
        ------------
        |           |   
        |           O
        |          \\|
        |           |
        |         
        _  
        ''',
         # head, body
        '''
        ------------
        |           |   
        |           O
        |           |
        |           |
        |          
        _  
        ''',
        #  head
        '''
        ------------
        |           |   
        |           O
        |       
        |           
        |        
        _  
        ''',
        # initial empty state
        '''
        ------------
        |           |   
        |          
        |        
        |          
        |       
        _  
        ''',
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)

if __name__=="__main__":
    main()
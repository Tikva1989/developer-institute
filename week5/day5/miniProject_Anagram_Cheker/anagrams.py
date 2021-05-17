from anagram_cheker import  AnagramChecker



def menu():
    while True:
        user_word = input("Please insert a word to anagram checks or 'q' for exit:  ").lower().strip()
        if  user_word.isalpha() and not user_word.isspace():
           return user_word
           break
        print("Your word id invalid. Try again")
    if user_word == 'q':
        print("Good Bye!")

def main():
    anagram = AnagramChecker()
    user_word = menu()
    if anagram.is_valid_word(user_word):
        results= anagram.get_anagrams(user_word)
        # return  results
        print("You type {}\nthis is a valid English word,\n Anagrams for your word: {}".format(user_word, results))


print(main())
# anagram = AnagramChecker()
# print(menu()
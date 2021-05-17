
class AnagramChecker():
        def __init__(self):
            with open("./sowpods.txt", 'r') as file:
               words = file.read().splitlines()
            self.words = [w.lower() for w in words]
            self.results = {'word': []}

        def is_valid_word(self, word):
                if word in self.words:
                        return True
                else:
                        return False


        def is_anagram(self,word1,word2):
             if len(word1) == len(word2):
                  return  sorted(word1.lower()) == sorted(word2.lower())


        def get_anagrams(self,word1):
                for word2 in self.words:
                    if self.is_anagram(word1,word2):
                        self.results['word'].append(word2)
                        # print(word2)
                return self.results['word']




# anagram = AnagramChecker()
# word = 'meat'
# anagram.is_valid_word(word)
# print(anagram.is_anagram(word,'mate'))
# print(anagram.get_anagrams(word))
#


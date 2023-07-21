class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        matches = []
        for word in list:
            if len(self.word) == len(word):
                if sorted(self.word.lower()) == sorted(word.lower()):
                    matches.append(word)
        return matches
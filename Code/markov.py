from dictogram import Dictogram
from utils import cleanup_source
import random

class MarkovChain(dict):

    def __init__(self, words_list=None):
        super(MarkovChain, self).__init__()
        #start and end points for chain
        if words_list is not None:
            self.create_chain(words_list)
            self['start'] = Dictogram(['the'])
            self['end'] = Dictogram()


    def create_chain(self, words_list):
        #loop through words list
        for index, word in enumerate(words_list):

            #Check if word is in histogram already
            if self.get(word) == None:
                #set value to a new dictogram object
                self[word] = Dictogram()

            #Make sure list does not go out of range
            if index + 1 < len(words_list) - 1:
                next_word = words_list[index + 1]
                #add next word to chain
                self.get(word).add_count(next_word)



    def create_sentence(self, length=10):
        #chose random word from start histogram
        sampled_word = random.choice(list(self.get('start')))
        sentence = sampled_word
        
        #select item in chain
        for item in range(length - 1):

            sampled_word = self[sampled_word].sample()
            sentence += " " + sampled_word

        return sentence


if __name__ == "__main__":
    
    words_list = cleanup_source('hist_test.txt')
    markov = MarkovChain(words_list=words_list)

    print(markov)
    print(markov.create_sentence())

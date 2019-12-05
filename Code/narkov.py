from dictogram import Dictogram
from utils import cleanup_source
import random

class NarkovChain(dict):

    def __init__(self, order, words_list=None):
        super(NarkovChain, self).__init__()
        #start and end points for chain
        self.order = order

        if words_list is not None:
            self.create_nth_chain(words_list)
            self['start'] = Dictogram(['the'])
            self['end'] = Dictogram(['.'])

        self.sentence = None

    def create_nth_chain(self, words_list):
        #Point to start slicing
        start = 0
        #point to stop slicing slice excludes the end point[]
        end = self.order

        while end <= len(words_list) :

            #take a slice
            state = ' '.join(words_list[start:end])
            #check if it is in histogram already
            if self.get(state) == None:
                #not in histogram so add it
                self[state] = Dictogram()

            #increment state
            start += 1
            end += 1

            #bounds check
            if end <= len(words_list):
                #look at next state
                next_state = ' '.join(words_list[start:end])
                #add next state to current state
                self.get(state).add_count(next_state)
  
    def create_sentence(self, length=10):
        #chose random word from start histogram
        sampled_word = random.choice(list(self.get('start')))
        sentence = sampled_word.capitalize()
        
        #select item in chain
        for item in range(length - 1):

            sampled_word = self[sampled_word].sample()
            sentence += " " + sampled_word

        sentence += random.choice(list(self.get('end')))
        self.sentence = sentence
        
        return sentence


if __name__ == "__main__":
    
    words_list = cleanup_source('hist_test.txt')
    #test orders 2 through 5
    for order in range(2,6):
        print(f"Markov Chain order: {order}")
        print(NarkovChain(order, words_list=words_list))
        print("----------------")

    #print(narkov.create_sentence())

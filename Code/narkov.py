from dictogram import Dictogram
from utils import cleanup_source
import random
import re

class NarkovChain(dict):

    def __init__(self, order, words_list=None):
        super(NarkovChain, self).__init__()
        #start and end points for chain
        self.order = order

        if words_list is not None:
            self['start'] = Dictogram()
            self.create_nth_chain(words_list)
            #self['end'] = Dictogram(['.'])

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


            #check if token should go in start state
            #checks for capitalization
            if re.match('[A-Z]', state) is not None:
                self.get('start').add_count(state)


            #increment state
            start += 1
            end += 1

            #bounds check
            if end <= len(words_list):
                #look at next state
                next_state = ' '.join(words_list[end-1:end])
                #add next state to current state
                self.get(state).add_count(next_state)



    def create_sentence(self):
        #chose random word from start dictogram
        sentence_list = list()
        sentence_list.extend(self['start'].sample().split(' ', 1))

        print(self['start'])
        print("----------------")
        print(sentence_list)

        stop_token_hit = False
        
        #loop until we hit a stop token
        while stop_token_hit is False:

            #look at current sentence
            end = len(sentence_list)

            #take n last words 
            state = ' '.join(sentence_list[end - self.order:end])
            print('-----')
            print(state)

            #sample the state and add to list
            sampled_word = self.get(state).sample()

            #check for a stop token
            if re.search('[$\.\?\!]', sampled_word) is not None:
                stop_token_hit = True

            sentence_list.append(sampled_word)

        sentence = ' '.join(sentence_list)

        return sentence



        
        # #select item in chain
        # for item in range(length - 1):

        #     sampled_word = self[sampled_word].sample()
        #     sentence += " " + sampled_word

        # sentence += random.choice(list(self.get('end')))
        # self.sentence = sentence
        
        #return sentence


if __name__ == "__main__":
    
    #words_list = cleanup_source('hist_test.txt')
    words_list = cleanup_source('civildisobedience.txt')
    #print(words_list)
    #test orders 2 through 5
    
    for order in range(2,3):
        print(f"Markov Chain order: {order}")
        narkov = NarkovChain(order, words_list=words_list)
        print(narkov)
        print("----------------")
        print(narkov['start'])
        print(narkov.create_sentence())

from dictogram import Dictogram
from utils import cleanup_source



def create_markov_chain(words_list):
    """
        Create markov chain from given words list
    """
    markov_dictonary = dict()

    #loop through words list
    for index, word in enumerate(words_list):

        #Check if word is in dictonary already
        if markov_dictonary.get(word) == None:
            #set value to a new dictogram object
            markov_dictonary[word] = Dictogram()

        #Make sure list does not go out of range
        if index + 1 < len(words_list) - 1:
            next_word = words_list[index + 1]
            #add next word to chain
            markov_dictonary.get(word).add_count(next_word)

    return markov_dictonary

if __name__ == "__main__":
    
    words_list = cleanup_source('hist_test.txt')

    print(create_markov_chain(words_list))

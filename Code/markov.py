from dictogram import Dictogram
from utils import cleanup_source
import random


def create_state_histogram(words_list):
    """
        Create markov chain from given words list
    """
    state_histogram = dict()

    #loop through words list
    for index, word in enumerate(words_list):

        #Check if word is in histogram already
        if state_histogram.get(word) == None:
            #set value to a new dictogram object
            state_histogram[word] = Dictogram()

        #Make sure list does not go out of range
        if index + 1 < len(words_list) - 1:
            next_word = words_list[index + 1]
            #add next word to chain
            state_histogram.get(word).add_count(next_word)

    return state_histogram


def create_sentence(state_histogram, length):
    #randomly choose a word to start sentence 
    sampled_word = random.choice(list(state_histogram))

    sentence = sampled_word

    for item in range(length - 1):

        sampled_word = state_histogram[sampled_word].sample()
        sentence += " " + sampled_word

    return sentence


if __name__ == "__main__":
    
    words_list = cleanup_source('hist_test.txt')

    state_histogram = create_state_histogram(words_list)

    print(create_sentence(state_histogram, 10))

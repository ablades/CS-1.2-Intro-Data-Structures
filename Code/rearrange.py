#Rearranges command line args

import sys
import random as r


def reverse_words(words_list):
    """
    Reverse every word in a list
    """
    for i, word in enumerate(words_list):
        words_list[i] = word[::-1]

    return words_list


def shuffle_list(words_list):
    """
    Shuffles order of words in a given list
    """
    for i, word in enumerate(words_list):
        random_index = r.randint(0, len(words_list) - 1)
        words_list[i] = words_list[random_index]
        words_list[random_index] = word

    return words_list


if __name__ == "__main__":
    words_list = []

    #Add args to list
    for arg in range(1, len(sys.argv)):
        words_list.append(sys.argv[arg])

    print(words_list)
    
    #Shuffles list
    shuffled_list = shuffle_list(words_list)
    print(shuffled_list)

    #Reverses list
    reversed_list = reverse_words(words_list)
    print(reversed_list)



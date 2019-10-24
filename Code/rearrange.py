#Rearranges command line args

import sys
import random as r
import math


def reverse_words(words_list):
    """
    Reverse every word in a list
    """
    for i, word in enumerate(words_list):
        words_list[i] = word[::-1]

    return words_list
"""
function shuffle(array) {
  var m = array.length, t, i;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = array[m];
    array[m] = array[i];
    array[i] = t;
  }

  return array;
}
"""
def fisher_yates_shuffle(words_list):
    """
    Shuffle algorithm adapted from https://bost.ocks.org/mike/shuffle/
    """
    m = len(words_list)
    
    while m:

        m -= 1
        i = math.floor(r.random() * m)
        temp = words_list[m]
        words_list[m] = words_list[i]
        words_list[i] = temp

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

    print(f"word list: {words_list}")
    
    #Shuffles list
    shuffled_list = shuffle_list(words_list)
    print(f"shuffled list: {shuffled_list}")

    #Fisher-yates
    fy_shuffle = fisher_yates_shuffle(words_list)
    print(f"fisher yates: {fy_shuffle}")

    #Reverses list
    reversed_list = reverse_words(words_list)
    print(f"reversed list: {reversed_list}")



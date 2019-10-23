#read in the words file
#select a random set of words from the file and store in a data type
#put the number of words requested together into a "sentence"
#output your sentence
import random as r
import sys

def read_file():
    words = list()
    count = 0
    with open('/usr/share/dict/words', 'r') as f: 
        words = f.read().split('\n')

    return words

def select_words(count, words_list):
    sentence = str()
    while count > 0:
        index = r.randint(0, len(words) - 1)
        
        if count == 1:
            sentence += words_list[index]
        else:
            sentence += words_list[index] + ' '

        count -= 1

    return sentence
        


if __name__ == "__main__":
    words = read_file()

    count = int(sys.argv[1])

    print(select_words(count, words))
import random
import sys

def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

    #Strip words of special characters
    for word in words:
        word = word.strip(".@'/").upper()

    return words

def histogram_dictonary(words):
    histogram = dict()

    #Look up and increment word
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

#create the sample list
def sample_list(histogram):
    words_list = list()

    for key, value in histogram.items():
        #add values to new list
        for i in range(value):
            words_list.append(key)

    return words_list

#choose word from list a certain count of times
def choose_words(count, words_list):
    count_list = list()
    count_histogram = dict()

    for i in range(count):
        count_list.append(random.choice(words_list))

    #add the list of word counts to dictonary
    for word in count_list:
        count_histogram[word] = count_histogram.get(word, 0) + 1

    return count_histogram

if __name__ == "__main__":

    file_name = sys.argv[1]

    words = read_file(file_name)

    hist = histogram_dictonary(words)

    words_list = sample_list(hist)

    chosen_word_counts = choose_words(100, words_list)

    print(chosen_word_counts)



    

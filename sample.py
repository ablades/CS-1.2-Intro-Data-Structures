import random
import sys

from histogram import read_file, histogram_dictonary



#create the sample list


def better_words(count, token_count, histogram):
    sentence = ""

    for i in range(count):
        random_value = random.randrange(0, token_count)
        position = 0

        for key, value in histogram.items():

            position += value

            if position > random_value:
                sentence += f" {key}"

    return sentence
   



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

    token_count = len(words)

    hist = histogram_dictonary(words)

    sentence = better_words(10, token_count, hist)

    print(sentence)


    



    

import sys


def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

    #Strip words of special characters
    for word in words:
        word = word.strip(".@'/").upper()

    return words


def histogram(words):
    histogram = dict()

    #Look up and increment word
    histogram[word] = histogram.get(word, 0) + 1

    return histogram


def histogram_list_of_lists(words):
    histogram = list()

    for word in words:
        for item in histogram:
            #Check if item already in list
            if item[0] == word:
                item[1] += 1
                break
        #add item to list if it does not exist
        else:
            histogram.append([word, 1])

    return histogram
            
            

    



def unquie_words(histogram):
    pass


def frequency(word, histogram):
    pass


if __name__ == "__main__":
    file_name = sys.argv[1]

    words = read_file(file_name)

    #Histogram using dict
    histogram(words)

    #Histogram using list of lists
    histogram_list_of_lists(words)
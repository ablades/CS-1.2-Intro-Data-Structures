import sys


def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

    #Strip words of special characters
    for word in words:
        word = word.strip(".@'/").upper()

    return words

#dictionary
def histogram_dictonary(words):
    histogram = dict()

    #Look up and increment word
    for word in words:
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
            

def histogram_of_tuples(words):
    histogram = list()

    for word in words:

        for index, item in enumerate(histogram):
            #Item is already in list
            if item[0] == word:
                histogram[index] = (word, (item[1] + 1))
                break
        #Item is not in list
        else:
            histogram.append((word, 1))

    return histogram
        

def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    #histogram is a list or tuple
    if isinstance(histogram, (list, tuple)):
        for item in histogram:
            if item[0] == word:
                return item[1]
    #Histogram is a dictonary
    elif isinstance(histogram, dict):
        return histogram.get("word", 0)

def histogram_list_of_counts(words):
    histogram = list()
    #([count], list())
    #[("count",['word', 'test', 'gdsgf'] )]

    #add words to histogram
    for word in words:
        #look at items(tuples) in histogram
        for i, tup in enumerate(histogram):
            #look at items in list in tuple is in index 1
            for j, j_item in enumerate(histogram[i][1]):
                # item already in list
                if word == j_item:
                    #get current item count
                    count = histogram[i][0]
                    #remove word from list
                    histogram[i][1].pop(j)

                    #loop through histogram
                    for k, k_item in enumerate(histogram):
                        #count is already in histogram append word to list
                        if (count + 1) == histogram[k][0]:
                            histogram[k][1].append(word)
                            break
                
                    #count does not exist in list so create it
                    else:
                        histogram.append((count + 1, [word])
                        





    #create a list
    #make a tuple where ([number], list of words with that count)

    #loop through entire words list
    #check if word is already in the list.
    #if it is move it to the next list. create that list if it doesnt exist


    pass



if __name__ == "__main__":
    file_name = sys.argv[1]

    words = read_file(file_name)

    #Histogram using dict
    print(f"Dictionary: {histogram_dictonary(words)}")

    print(f"Tuples: {histogram_of_tuples(words)}")
    #Histogram using list of lists
    print(f"List of Lists: {histogram_list_of_lists(words)}")
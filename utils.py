import sys

#app.py          # main script, uses other modules to generate sentences
#cleanup.py      # module for cleaning up source text
##tokenize.py     # module for creating lists of tokens from a text
#word_count.py   # module for generating histograms from a list of tokens
#sample.py       # module for generating a sample word from a histogram
#sentence.py     # module for generating a sentence from a histogram

def cleanup_source(file_name):
    """
        Reads in file and cleans it up
        Params: file_name path to file
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
        #words = f.read().split()
    word_list = []
    #handle small lines said by characters and spaces in files
    for i, line in enumerate(lines):
        line = line.lstrip().rstrip()

        if len(line.split(' ')) >= 4:
            for word in line.split():
                word_list.append(word)

    return word_list

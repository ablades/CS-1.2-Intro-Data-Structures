#Rearranges command line args

import sys
import random

if __name__ == "__main__":
    words_list = []
    for arg in range(1, len(sys.argv)):
        words_list.append(sys.argv[arg])

    random.shuffle(words_list)

    print(words_list)
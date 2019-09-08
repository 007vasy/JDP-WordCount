"""Word Freq CLI
Usage:
    word_freq.py
    word_freq.py <file_path>
    word_freq.py <file_path> <excluded_words>
    word_freq.py <file_path> <excluded_words> <min_count>
    word_freq.py <file_path> <min_count> 
    word_freq.py -h|--help
    word_freq.py -v|--version
Options:
    <file_path>  file_path argument to point out the file to parse and show the frequency of the words in it.
    <excluded_words> the words in this file will be excluded from the list.
    <min_count> is the threshold (Anything equal or less will be hidden).
    
    -h --help  Show this screen.
    -v --version  Show version.
"""

import os
from docopt import docopt

def filePathFeedback(file_path):
    return("{} is the choosen file path".format(file_path))

def excludedWordsFeedback(excluded_words):
    return("{} is the file containing the excluded words".format(excluded_words))

def minCountFeedback(min_count):
    return("_{}_ is the threshold (Anything equal or less will be hidden)".format(min_count))



if __name__ == '__main__':
    print("####")
    arguments = docopt(__doc__, version='1.0')
    
    if arguments['<file_path>']:
        fName = arguments['<file_path>']
        print(filePathFeedback(fName))

        stop_words_file = ""
        if arguments['<excluded_words>']:
            stop_words_file = arguments['<excluded_words>']
            print(excludedWordsFeedback(stop_words_file))

        count_threshold = None
        if arguments['<min_count>']:
            count_threshold = int(arguments['<min_count>'])
            print(minCountFeedback(count_threshold))


        try:
            f1 = open(fName, 'r')
        except IOError:
            print("Could not read file for analysis:{}".format(fName))
            sys.exit()
        text = ""    
        with f1:
            text = f1.read()
            f1.close()

        for ch in '-.,:':
            text = text.replace(ch,'')

        text = text.lower()

        list_of_words = text.split()

        freq_counter = {}

        for w in list_of_words:
            if w not in freq_counter:
                freq_counter[w] = 1;
            else:
                freq_counter[w] += 1

        freq_of_words = []

        for key,val in freq_counter.items():
            freq_of_words.append((val,key))

        freq_of_words.sort(reverse=True)

        stop_words = [] 

        if stop_words_file != "":
            try:
                f2 = open(stop_words_file, 'r')
            except IOError:
                print("Could not read file for stop words:{}".format(stop_words_file))
                sys.exit()
               
            with f2:
                stop_words = f2.read().split()
                f2.close()

        print("----")

        for (val, key) in freq_of_words:
            if val > count_threshold and key not in stop_words: 
                print('{}:{}'.format(key,val))

        print("----")

    else:
        print(arguments)
    print("####")
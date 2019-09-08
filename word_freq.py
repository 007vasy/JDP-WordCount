"""Word Freq CLI
Usage:
    word_freq.py
    word_freq.py <file_path>
    word_freq.py <file_path> <count_threshold>
    word_freq.py <file_path> <count_threshold> <stop_words_file> 
    word_freq.py -h|--help
    word_freq.py -v|--version
Options:
    <file_path>  file_path argument to point out the file to parse and show the frequency of the words in it.
    <stop_words_file> the words in this file will be excluded from the list.
    <count_threshold> is the threshold (Anything equal or less will be hidden).
    
    -h --help  Show this screen.
    -v --version  Show version.
"""

import os
import sys
from docopt import docopt

def openFileAndReadIn(fileName):
    text = "" 
    try:
        f = open(fileName, 'r')
    except IOError:
        print("ERROR Could not read file:{}".format(fileName))
        sys.exit()

    with f:
        text = f.read()
        f.close()
    return text

def cleanTextAndMakeAList(text):
    for ch in "-.,:'":
         text = text.replace(ch,'')

    text = text.lower()

    return text.split()

def countWordsFreqAndReturnListOfTuples(list_of_words):
    freq_counter = {}

    for w in list_of_words:
        if w not in freq_counter:
            freq_counter[w] = 1;
        else:
            freq_counter[w] += 1

    freq_of_words = []

    for key,val in freq_counter.items():
        freq_of_words.append((val,key))
    return freq_of_words

def filterListOfWords(freq_of_words,count_threshold,stop_words):
    temp_list = []
    if count_threshold != None:
        for (val, key) in freq_of_words:
            if val > count_threshold and key not in stop_words :
                temp_list.append((val,key))
    else:
        temp_list = freq_of_words        

    return temp_list

def printOutWordFreqResult(filtered_freq_of_words):
    print("----")
    filtered_freq_of_words.sort(reverse=True)
    for (val, key) in filtered_freq_of_words:
        print('{}:{}'.format(key,val))
    print("----")
    return

def filePathFeedback(file_path):
    return("{} is the choosen file path".format(file_path))

def minCountFeedback(count_threshold):
    return("_{}_ is the threshold (Anything equal or less will be hidden)".format(count_threshold))

def excludedWordsFeedback(stop_words_file):
    return("{} is the file containing the excluded words".format(stop_words_file))

if __name__ == '__main__':
    print("####")
    arguments = docopt(__doc__, version='1.0')
    
    if arguments['<file_path>']:

        analysis_f_name = arguments['<file_path>']
        print(filePathFeedback(analysis_f_name))
        analysed_text = openFileAndReadIn(analysis_f_name)

        count_threshold = None
        stop_words_file = ""
        stop_words = [] 

        if arguments['<count_threshold>']:
            count_threshold = int(arguments['<count_threshold>'])
            print(minCountFeedback(count_threshold))


        if arguments['<stop_words_file>']:
            stop_words_file = arguments['<stop_words_file>']
            print(excludedWordsFeedback(stop_words_file))

            stop_words = openFileAndReadIn(stop_words_file).split()

        list_of_words = cleanTextAndMakeAList(analysed_text)

        freq_of_words = countWordsFreqAndReturnListOfTuples(list_of_words)

        filtered_freq_of_words = filterListOfWords(freq_of_words,count_threshold,stop_words)

        printOutWordFreqResult(filtered_freq_of_words)

    else:
        print(arguments)
    print("####")
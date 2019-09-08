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

from docopt import docopt

def filePathFeedback(file_path):
    return("{} is the choosen file path".format(file_path))

def excludedWordsFeedback(excluded_words):
    return("{} is the file containing the excluded words)".format(excluded_words))

def minCountFeedback(min_count):
    return("_{}_ is the threshold (Anything equal or less will be hidden)".format(min_count))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    if arguments['<file_path>']:
        print(filePathFeedback(arguments['<file_path>']))
        if arguments['<excluded_words>']:
            print(excludedWordsFeedback(arguments['<excluded_words>']))
        if arguments['<min_count>']:
            print(minCountFeedback(arguments['<min_count>']))
            
    else:
        print(arguments)
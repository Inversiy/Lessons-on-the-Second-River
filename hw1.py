"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

from typing import List
from collections import Counter
import string
import re



def get_longest_diverse_words(file_path: str) -> List[str]:
    '''
        This function find 10 longest words consisting from largest
        amount of unique symbols. First of all, it split every line
        into separate words, and add its into dictionary, where
        keys - its all words from document, values - number of
        unique symbols. After that 10 longest from "leaders" add
        into output list. 
    '''
    words = {}
    with open(file_path, "r") as file:
        part_of_word = ""
        for line in file:
            words_line = line.split()
            split_line = line.split()
            if part_of_word != "" and split_line != []:
                split_line[0] = part_of_word + split_line[0]
                words_line[0] = part_of_word + words_line[0]
                part_of_word = ""
            for i in (range(len(split_line))):
                for j in split_line[i]:
                    if j.lower() not in string.ascii_lowercase \
                                    and j not in string.punctuation:
                        words_line.remove(split_line[i])
                        break
                    if j == "-":
                        part_of_word = split_line[i][:-1]
                        words_line.remove(split_line[i])
                        break
                else:
                    word_clear = re.match(r'((\W)*?(\w)+(\W)*?)', \
                                                    split_line[i], re.M)
                    if word_clear:
                        words_line[words_line.index(split_line[i])] = \
                                                        word_clear.group(1)
            for word in words_line:
                words[word] = len(Counter(word))
    file.close()
    output_list = []
    for i in range(len(list(Counter(words).most_common(10)))):
        output_list.append(list(list(Counter(words).most_common(10))[i])[0])
    return output_list


def get_rarest_char(file_path: str) -> str:
    '''
        This function find the rarest char. First of all,
        it count all symbols, and then return rarest.
    '''
    main_count = Counter()
    with open(file_path, "r") as file:
       for line in file:
           count = Counter(line)
           main_count += count
    return list(main_count.most_common(len(main_count))[-1])[0]


def count_punctuation_chars(file_path: str) -> int:
    '''
        This function count all punctuation chars. First of all,
        it count all symbols, and then sum only punctuation's numbers.
    '''
    main_count = Counter()
    with open(file_path, "r") as file:
       for line in file:
           count = Counter(line)
           main_count += count
    count_punctuation = Counter()
    for i in main_count:
       if i in string.punctuation:
           count_punctuation[i] = main_count[i]
    return sum(count_punctuation[k] for k in count_punctuation)


def count_non_ascii_chars(file_path: str) -> int:
    '''
        This function find all non-ascii chars, that have special look,
        using regular expressions and counters.
    '''
    count_nonASCII = Counter()   
    with open(file_path, "r") as file:
        for line in file:
           count = Counter(re.findall(r'(\\u{1}\w{4})', line, re.M))
           count_nonASCII += count
        return sum(count_nonASCII[x] for x in count_nonASCII)


def get_most_common_non_ascii_char(file_path: str) -> str:
    '''
        This function find non-ascii chars, that have special look, and find the most common one,
        using regular expressions and counters.
    '''
    count_nonASCII = Counter()   
    with open(file_path, "r") as file:
        for line in file:
           count = Counter(re.findall(r'(\\u{1}\w{4})', line, re.M))
           count_nonASCII += count
    return list(count_nonASCII.most_common(1)[0])[0]


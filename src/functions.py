from collections import Counter
from itertools import izip, count
import operator


def write_to_file(lst, f):
    """
    INPUT: list, open file object
    OUTPUT: None

    Write the list to the file with line numbers, starting at 1.
    INPUT: ["a", "b", "c"]
    FILE CONTENTS:
    1 a
    2 b
    3 c

    Hint: Use enumerate for cleaner code
    """

    for i, letter in enumerate(lst):
        f.write(str(i + 1) + ' ' + letter + '\n')



def merge_files(f1, f2, out):
    """
    INPUT: open file, open file, open file
    OUTPUT: None

    f1 and f2 are two files with the same number of lines. Merge the contents
    together, separated with a comma.

    INPUT FILES:
    cat
    dog

    mouse
    rabbit

    OUTPUT FILE:
    cat,mouse
    dog,rabbit

    Hint: Use izip
    """

    file1_lines = f1.read().splitlines()
    #["cat", "dog"]
    file2_lines = f2.read().splitlines()
    #["mouse", "rabbit"]

    #[("cat mouse", "dog rabbit"]
    zipped_lines = izip(file1_lines, file2_lines)
    for stuff in zipped_lines:
        out.write(stuff[0] + ',' + stuff[1] + '\n')



def key_in_value(d):
    """
    INPUT: dict
    OUTPUT: list

    Return the keys from the dictionary where the key is a member in the
    associated value.

    example:
    INPUT: {"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]}
    OUTPUT: ["a", "c"]

    Hint: Use iteritems
    (Can be done on one line with a list comprehension)
    """

    out_list = []
    for k,v in d.iteritems():
        if k in v:
            out_list.append(k)
    return out_list


def most_common_letters(sentence):
    """
    INPUT: string
    OUTPUT: list of strings

    Given a sentence, give the most common letter for each word.
    You should lowercase the letters. If there's a tie, include any of them.

    example:
    INPUT: "Welcome to Zipfian Academy!"
    OUTPUT: 'e t i a'

    Hint: use Counter and the string join method
    (It is possible to do this in one line, but you might lose some
    readability)
    """
    answer_list=[]
    for word in sentence.split():
        answer_list.append(max(Counter(word).iteritems(), key=operator.itemgetter(1))[0])
    return ' '.join(answer_list)

def merge_dictionaries(d1, d2):
    """
    INPUT: dict (string => int), dict (string => int)
    OUTPUT: dict (string => int)

    example:
    INPUT: {"a": 2, "b": 5}, {"a": 7, "c":10}
    OUTPUT: {"a": 9, "b": 5, "c": 10}

    Create a new dictionary that contains all the key, value pairs from d1 and
    d2. If a key is in both dictionaries, sum the values.
    """
    result = dict(d1)
    for k, v in d2.iteritems():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    return result

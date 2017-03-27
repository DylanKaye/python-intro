def list_of_words(f):
    """
    INPUT: file
    OUTPUT: list of words

    Create a list of all the unique words in the text file given.
    """
    empty = set()
    for line in f:
        for word in line.split():
            empty.add(word)
    return empty


def find_new_words(f, word_dict):
    """
    INPUT: file, dictionary
    OUTPUT: list

    Given a text file and a dictionary whose keys are words, return a list
    of the words in the file which are not in the dictionary.
    """

    words = []
    empty = []
    for line in f:
        empty.extend(line.split())
    for word in empty:
        if word not in word_dict.keys():
            words.append(word)
    return words


def get_average_score(f, word_dict):
    """
    INPUT: file, dictionary
    OUTPUT: float

    Given a text file and a dictionary whose keys are words and values are a
    score for the word, return the average score of all the words in the
    document. You should assume that missing words have a score of 1.
    """

    score = 0
    for line in f:
        for i, word in enumerate(line.strip().split()):
            try:
                score += word_dict[word]
            except KeyError:
                score += 1
    return float(score) / i


def find_high_valued_words(word_dict, value):
    """
    INPUT: dict, float
    OUTPUT: list

    Return the items from word_dict whose values are larger than value.
    """

    return [key for key, val in word_dict.iteritems() if val > value]

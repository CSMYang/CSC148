"""Functions for annotating poetry."""

# Type shorthands
from typing import List, TextIO
PronouncingTable = List[List[str]]

# The main module - need to import so that window code works correctly
import annotate_poetry

NO_STRESS_SYMBOL = 'x'
PRIMARY_STRESS_SYMBOL = '/'
SECONDARY_STRESS_SYMBOL = '\\'  # note: len('\\') == 1 due to special character

"""
A pronouncing table: a nested list, [list of str, list of list of str]
  o a two item list, contains two parallel lists
  o the first item is a list of words (each item in this sublist is a str
    for which str.isupper() is True)
  o the second item is a list of pronunciations, where a pronunciation is a
    list of phonemes (each item in this sublist is a list of str)
  o the pronunciation for the word at index i in the list of words is at index
    i in the list of pronunciations
"""

# A small pronouncing table that can be used in docstring examples.
SMALL_TABLE = [['A', 'BOX', 'CONSISTENT', 'DON\'T', 'FOX', 'IN', 'SOCKS'],
               [['AH0'],
                ['B', 'AA1', 'K', 'S'],
                ['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'],
                ['D', 'OW1', 'N', 'T'],
                ['F', 'AA1', 'K', 'S'],
                ['IH0', 'N'],
                ['S', 'AA1', 'K', 'S']]]

"""
A pronouncing dictionary is a list of pronouncing lines, where a pronouncing
line is a line in the CMU Pronouncing Dictionary format:
  a word followed by the phonemes describing how to pronounce the word.
  o example:
    BOX  B AA1 K S
"""

# A small pronouncing dictionary that can be used in docstring examples.
SMALL_PRONOUNCING_DICT = [
    'A  AH0',
    'BOX  B AA1 K S',
    'CONSISTENT  K AH0 N S IH1 S T AH0 N T',
    'DON\'T  D OW1 N T',
    'FOX  F AA1 K S',
    'IN  IH0 N',
    'SOCKS  S AA1 K S']


# ===================== Provided Helper Functions =============================

def prepare_word(s: str) -> str:
    """Return a new string based on s in which all letters have been converted
    to uppercase and punctuation characters have been stripped from both ends.

    Inner punctuation is left unchanged.

    This function prepares a word for looking up in a pronouncing table.

    >>> prepare_word('Birthday!!!')
    'BIRTHDAY'
    >>> prepare_word('"Quoted?"')
    'QUOTED'
    >>> prepare_word("Don't!")
    "DON'T"
    """

    punctuation = """!"`@$%^&_+-={}|\\/—,;:'.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


def get_rhyme_scheme_letter(offset: int) -> str:
    """Return the letter corresponding to the offset from 'A'.  Helpful when
    labelling a poem with its rhyme scheme.

    Precondition: 0 <= offset <= 25

    >>> get_rhyme_scheme_letter(0)
    'A'
    >>> get_rhyme_scheme_letter(25)
    'Z'
    """

    return chr(ord('A') + offset)


# ======== Students: Add Your Code Below This Line ================



# Your code here

def get_word(pronouncing_line: str) -> str:
    """Retrun the word in pronouncing line.
    
    >>> get_word('BOX  B AA1 K S')
    'BOX'
    >>> get_word('FOX  F AA1 K S')
    'FOX'
    """
    return pronouncing_line.split(sep=' ')[0]

def get_pronunciation(pronouncing_line: str) -> List[str]:
    """Return the pronunciation list of the word in pronouncing line.
    >>> get_pronunciation('BOX  B AA1 K S')
    ['B', 'AA1', 'K', 'S']
    >>> get_pronunciation('FOX  F AA1 K S')
    ['F', 'AA1', 'K', 'S']
    """
    return pronouncing_line.split(sep=' ')[2:]

def make_pronouncing_table(pronouncing_list: List[str]) -> PronouncingTable:
    """
    Return the pronouncing table built from the list of pronouncing lines.

    NOTE: This is not the first function that you should write, but we included
    the function header and one example for illustrative purposes. You should
    fill in the proper docstring and add another example to this function. You
    should also write other functions.

    >>> SMALL_TABLE == make_pronouncing_table(SMALL_PRONOUNCING_DICT)
    True
    >>> make_pronouncing_table(['BOX  B AA1 K S', 'IN  IH0 N', 
    'SOCKS  S AA1 K S'])
    [['BOX', 'IN', 'SOCKS'], [['B', 'AA1', 'K', 'S'], ['IH0', 'N'], 
    ['S', 'AA1', 'K', 'S']]]
    """
    list_of_words = []
    list_of_phonemes = []
    for elements in pronouncing_list:
        list_of_words.append(get_word(elements))
        list_of_phonemes.append(get_pronunciation(elements))
    return [list_of_words, list_of_phonemes]    

def look_up_pronunciation(word: str, PronouncingTable) -> List[str]:
    """Return a list of phonemes for the word in the pronouncing table.
    >>>look_up_pronunciation('BOX', [['BOX', 'IN', 'SOCKS'], [['B', 'AA1', 'K', 
    'S'], ['IH0', 'N'], ['S', 'AA1', 'K', 'S']]])
    ['B', 'AA1', 'K', 'S']
    >>>look_up_pronunciation('IN', [['BOX', 'IN', 'SOCKS'], [['B', 'AA1', 'K', 
    'S'], ['IH0', 'N'], ['S', 'AA1', 'K', 'S']]])
    ['IH0', 'N']
    """
    for i in range(len(PronouncingTable[0])):
        if word == PronouncingTable[0][i]:
            return PronouncingTable[1][i]
    return []

def is_vowel_phoneme(phoneme: str) -> bool:
    """Return true if the phoneme string contains vowel phoneme.
    >>>is_vowel_phoneme('AH0')
    True
    >>>is_vowel_phoneme('N')
    False
    """
    if len(phoneme) != 3:
        return False
    elif phoneme[0] not in 'AEIOU':
        return False
    elif not phoneme[1].isupper():
        return False
    elif phoneme[2] not in '012':
        return False
    return True

def last_syllable(list_of_phonemes: List[str]) -> List[str]:
    """Return the list of last vowel phoneme and the phonenes behind it of the 
    list of phonemes.
    >>>last_syllable(['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'])
    ['AH0', 'N', 'T']
    >>>last_syllable(['B', 'AA1', 'K', 'S'])
    [AA1', 'K', 'S']
    """
    list2 = list_of_phonemes[:]
    list2.reverse()
    list3 = []
    for i in range(len(list2)):
        if is_vowel_phoneme(list2[i]):
            list3 = list2[:i + 1]
            list3.reverse()
            return list3
    return []

def convert_to_lines(file: TextIO) -> List[str]:
    """Return
    """
    file = file.readlines()
    list_to_return = []
    for sentence in file:
        if not sentence == '\n':
            sentence.strip()
            sentence2 = sentence[:sentence.rfind('\n')]
            list_to_return.append(sentence2)
    return list_to_return
    
    
    
    
if __name__ == '__main__':

    """Optional: uncomment the lines import doctest and doctest.testmod() to
    have your docstring examples run when you run stress_and_rhyme_functions.py
    NOTE: your docstrings MUST be properly formatted for this to work!
    """
    #import doctest
    #doctest.testmod()

"""
This module provides the simple functionality to determine if 2 words are anagarams of eachother.
"""

# Global vars so that we can print text in color.
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def is_anagram(word_a: str, word_b: str) -> bool:
    """
    This is the main function of this module which takes in 2 strings and returns True if they are
    anagrams, and returns False otherwise.
    """
    if not isinstance(word_a, str) or not isinstance(word_b, str):
        raise RuntimeError("`is_anagram` expected two string inputs but one or both are not.")
    if len(word_a) != len(word_b):
        print(f"{FAIL}'{word_a}' is not an anagram of '{word_b}'{ENDC}")
        return False
    word_a = word_a.lower()
    word_b = word_b.lower()
    dic_a = count_letters(word_a)
    dic_b = count_letters(word_b)
    if dic_a == dic_b:
        print(f"{OKGREEN}'{word_a}' IS an anagram of '{word_b}'{ENDC}")
        return True
    print(f"{FAIL}'{word_a}' is not an anagram of '{word_b}'{ENDC}")
    return False

def count_letters(word: str) -> dict:
    """
    Helper function to count the numbers of each letter in the given word.
    Returns a dictionary where the keys are letters and the values are the number of times
    each letter occurs in the word.
    """
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

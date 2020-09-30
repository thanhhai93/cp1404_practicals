"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac6.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return s * n


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) > length


def run_tests():


    assert repeat_string("Python", 1) == "Python"

    assert repeat_string("hi", 2) == "hi hi"


    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"


    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = car()
    assert test_ca.fuel == 10
def phrase_to_sentence(phrase):


    phrase_to_sentence('hello')
    phrase_to_sentence('It is an ex parrot.')
    phrase_to_sentence('This subject rocks')
    """capitalise the first letter"""
    sentence = phrase.capitalize()
    """add the full stop, but only if we need to"""
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

doctest.testmod


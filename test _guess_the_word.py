import pytest
from guess_the_word import select_word, display_word

# Test if select_word function returns a word from the correct list
def test_select_word():
    word = select_word()
    assert word in ['zelda', 'mario', 'pacman', 'sonic', 'minecraft']

# Test the display_word function
def test_display_word():
    word = 'zelda'
    guessed_letters = ['z', 'e']
    current_display = display_word(word, guessed_letters)
    assert current_display == 'ze___'
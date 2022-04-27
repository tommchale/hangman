'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.


    Parameters:
    ----------
    word_list: list (done)
        List of words to be used in the game
    num_lives: int
        Number of lives the player has (done)

    Attributes:
    ----------
    word: str (done)
        The word to be guessed picked randomly from the word_list
    word_guessed: list (done)
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int (done)
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int (done)
        The number of lives the player has
    list_letters: list (done)
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring (done)
        # set str of the instance to random option in the word list
        self.str = random.choice(word_list)
        # create empty list for list of the letters of the word, with '_' for each letter not yet guessed
        self.word_guessed = []
        for item in list(self.str):
            self.word_guessed.append('_')
        # Change list of letters in word to a set, for unique values, then compute length
        self.num_letters = len(set(self.str))
        # Create a list for list of letters that have been tried
        self.list_letters = []

        # TODO 2: Print two message upon initialization: (done)
        # 1. "The mistery word has {num_letters} characters"
        print('The mystery word has', self.num_letters, ' unique characters')
        # 2. {word_guessed}
        print(self.word_guessed)

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        count = 0
        # Iterable check whilst count is less that list unique values in set
        while count < self.num_letters:
            for item in list(self.str):
                if letter.lower() == item:
                    print('\n Congratulations that is a match ! \n ')
                    count = count + 1
                elif letter != item:
                    continue
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
     #   pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried (done)
        2. If the character is a single character (done)
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter (done)
        # TODO 1: Assign the letter to a variable called `letter` (done)
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character" (done)
        # create count integer for the loop

        while True:
            letter = input('\n Please guess a letter : \n \n')
            # if length of character input is equal to 1, accept
            if len(list(letter)) == 1:
                # If items in list of guessed letters
                if self.list_letters:
                    while True:
                        # Iterates through list of guessed letters
                        for item in self.list_letters:
                            # If item in list of previously guessed letters matches guess
                            if item == letter:
                                print('\n The letter', item,
                                      'has already been tried')
                                break
                            # If item in list of previously guessed letters does not match guess
                            elif item != letter:
                                for item in list(self.str):
                                    self.check_letter(letter)
                                continue
                        break
                # If no items in list of guessed letters
                else:
                    self.list_letters.append(letter)
                    self.check_letter(letter)

            else:
                print('\n Please enter only one character..')

                # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried". (done)
                # TODO 3: If the letter is valid, call the check_letter method
                #  pass

                # def play_game(word_list):
                #   # As an aid, part of the code is already provided:
                #   game = Hangman(word_list, num_lives=5)
                # TODO 1: To test this task, you can call the ask_letter method (done)
                # TODO 2: To test this task, upon initialization, two messages should be printed (done)
                # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word (done)

                # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
                # If the user guesses the word, print "Congratulations! You won!"
                # If the user runs out of lives, print "You lost! The word was {word}"

                #  pass

                # if __name__ == '__main__':
                #   word_list = ['apple', 'banana', 'orange',
                #               'pear', 'strawberry', 'watermelon']
                #  play_game(word_list)
Player1 = Hangman(['help', 'me', 'fog'])
Player1.ask_letter()
# %%

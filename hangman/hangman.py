
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
        # set str of the instance to random option in the word list
        self.str = random.choice(word_list)
        # create empty dictionary for key value paris of the letters of the word, with '_' for each letter not yet guessed
        self.word_guessed = []
        for item in list(self.str):
            self.word_guessed.append('_')
        # Change list of letters in word to a set, for unique values, then compute length
        self.num_letters = len(set(self.str))
        # Create attribute for number of lives
        self.num_lives = num_lives
        # Create a list for list of letters that have been tried
        self.list_letters = []

        print('The mystery word has', self.num_letters, ' unique characters')
        print(self.word_guessed)
        print('change for branch tester!')

        self.hangman_animation = [

            ''' 
               ___
              |   |
              | __O__
              |   |
              |  ( )
              |_____               
            
            
            ''',

            '''  
               ___
              |   |
              |  
              |   
              |  
              |_____   
              
              ''',
            '''
               ___
              |   
              |
              |
              |
              |_____

              ''',
            '''
               
              |   
              |  
              |   
              |  
              |_____

              ''',
            '''
                                                                    
             _____             
              
              
              '''


        ]

    def check_letter(self, letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # Boolean if guess is not correct
        guess_success = False
        # List indexing value
        str_index = 0
        for item in list(self.str):
            if letter == item:
                guess_success = True
                # Add letter into position in array
                self.word_guessed[str_index] = letter
                # Increase count of word index
                str_index = str_index + 1
            elif letter != item:
                str_index = str_index + 1

        self.list_letters.append(letter)

        if guess_success == False:
            if self.num_lives > 1:
                self.num_lives = self.num_lives - 1
                print(' \n Sorry ', letter, ' is not in the word. \n \n You have ',
                      self.num_lives, ' live(s) left.')
                print(self.hangman_animation[self.num_lives])
                print(self.word_guessed)
            else:
                print(' \n Game Over \n')
                self.num_lives = self.num_lives - 1
                print(self.hangman_animation[self.num_lives])
                print(' \n The word was', self.str, ' ! \n ')

        if guess_success == True:
            if self.num_letters > 1:
                print(self.word_guessed)
                print('\n Nice ', letter, ' is in the word! \n ')
                self.num_letters = self.num_letters - 1
            else:
                print(self.word_guessed)
                print(' \n Congratulation you won the game! \n')
                self.num_lives = 0

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried (done)
        2. If the character is a single character (done)
        If it passes both checks, it calls the check_letter method.
        '''
        while self.num_lives >= 1:
            letter = input('\n Please guess a letter : \n \n')
            # if length of character input is equal to 1, accept
            # Ensure input is in lower case
            letter = letter.lower()
            if len(list(letter)) == 1:
                # If items in list of guessed letters
                if self.list_letters:
                    # Iterates through list of guessed letters
                    for item in self.list_letters:
                        # If item in list of previously guessed letters matches guess
                        if letter == item:
                            print('\n The letter ', item,
                                  'has already been tried')
                            break
                        # If item in list of previously guessed letters does not match guess
                        elif letter != item:
                            pass
                    if letter != item:
                        self.check_letter(letter)
                # If no items in list of guessed letters
                else:
                    self.check_letter(letter)
            else:
                print('\n Please enter only one character...')


def play_game(word_list):

    # Create instance of the class called game.
    game = Hangman(word_list)
    game.ask_letter()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange',
                 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

# %%

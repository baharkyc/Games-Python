"""
File: word_guess.py
-------------------
In this game the player has to guess a random word letter by letter
in 8 guesses.

"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word, guess_count):
    """
    This function is where the game play happens. It asks the user for letter
    till the word guess is complete or the player runs out of 8 guesses.
    """

    # create a list for current state of the word and assign dashes to each item.
    current_word = []
    for char in secret_word:
        current_word.append('-')
    
    
    while guess_count > 0:
        #opening messages.
        print ('The word now looks like this: ' , ''.join(current_word))
        print ('You have ', guess_count, ' guesses left.')
        guess_letter = (input('Type a single letter here, then press enter: ')).upper()
  
        
        #if the guess is wrong, guess count decreases by one.
        if guess_letter not in secret_word:
            guess_count -= 1
            print ('There are no ', guess_letter, ' in the word.')
            
        #if the guess is right keep the letter in the current_word list.
        else:
            for i in range(len(secret_word)):
                if guess_letter == secret_word[i]:
                    current_word[i] = guess_letter
            print ('That guess is correct.')

        #decide if player guessed all the letters right.
        if ''.join(current_word) == secret_word:
            print('Congratulations, the word is: ' , secret_word)
            break
        #decide if player lost.
        elif guess_count == 0:
            print('Sorry, you lost. The secret word was: ', secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  
    """
    
    #open the file and read the lines.
    word_list = []
    text_file = open(LEXICON_FILE, 'r')
    lines = text_file.readlines()
    
    #append stripped elements into the word_list list.
    for i in lines:
        words = i.strip()
        word_list.append(words)
    
    #Set a random index to get the word from.
    index = random.randrange(len(word_list)-1)
    return((word_list[index]).upper())
    

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    
    print("Welcome to the word guessing game! \n You have " , INITIAL_GUESSES, "guesses to predict the word. Good luck!")
    secret_word = get_word()
    play_game(secret_word, INITIAL_GUESSES)




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
    
    

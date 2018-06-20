# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for secret_word_letter in secret_word:
        if secret_word_letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_so_far = ''
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            guessed_so_far += '_ '
        else:
            guessed_so_far += secret_word[i]

    return guessed_so_far





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    unused_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            unused_letters += letter
    return unused_letters


def compute_score(secret_word, remaining_guesses):
    number_of_unique_letters = len(secret_word)
    for letter in secret_word:
        if secret_word.count(letter)>1:
             number_of_unique_letters -= secret_word.count(letter)-1
    return remaining_guesses * number_of_unique_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman !\nI am thinking of a word that is',len(secret_word),'letters long\n----------')
    number_of_guesses = 6
    number_of_warnings = 3
    letters_guessed = []
    consonants = 'bcdfghjklmnpqrstvwxyz'
    while number_of_guesses > 0:
        print('-----------------')
        print('You have ', number_of_guesses , 'guesses left')
        print('You have ', number_of_warnings , 'warnings left')
        print('Available letters: ', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ').lower()
        if guess.isalpha() ==False:
            number_of_warnings -= 1
            if number_of_warnings <= 0:
                number_of_guesses -= 1
                print('Oops!that is not a valid letter \nYou have no warnings left so you lose a guess')
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops!that is not a valid letter \nYou have ',number_of_warnings,' warnings left')
                print(get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            number_of_warnings -= 1
            if number_of_warnings <= 0:
                number_of_guesses -= 1
            print('You have already guessed this letter!\nYou have ',number_of_warnings,' warnings left')
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                if guess in consonants:
                    number_of_guesses -= 1
                else:
                     number_of_guesses -= 2
                print('Oops! That is not a letter in my word' , get_guessed_word(secret_word, letters_guessed))
                print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            print('----------\nCongratulations, you won!')
            print('Your total score for this game is: ', compute_score(secret_word,number_of_guesses))
            break
        elif number_of_guesses == 0:
            print('You ran out of guesses. The word was: ',secret_word)
       






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #In replacement of the strip()method
    word = ''
    for char in my_word:
        if char != ' ':
            word += char
    my_word = word
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != other_word[i]:
            if my_word[i] != '_':
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matching_words = []
    for word in wordlist:
        if match_with_gaps(my_word,word):
            matching_words.append(word)
    if len(matching_words) > 0:
        print('Possible matches are: \n',' '.join(matching_words))
    else:
        print('No matches found')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman !\nI am thinking of a word that is',len(secret_word),'letters long\n----------')
    number_of_guesses = 6
    number_of_warnings = 3
    letters_guessed = []
    consonants = 'bcdfghjklmnpqrstvwxyz'
    while number_of_guesses > 0:
        print('-----------------')
        print('You have ', number_of_guesses , 'guesses left')
        print('You have ', number_of_warnings , 'warnings left')
        print('Available letters: ', get_available_letters(letters_guessed))
        guess = input('Please guess a letter: ').lower()
        if guess == '*':
            show_possible_matches(secret_word)
        elif guess.isalpha() ==False:
            number_of_warnings -= 1
            if number_of_warnings <= 0:
                number_of_guesses -= 1
                print('Oops!that is not a valid letter \nYou have no warnings left so you lose a guess')
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops!that is not a valid letter \nYou have ',number_of_warnings,' warnings left')
                print(get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            number_of_warnings -= 1
            if number_of_warnings <= 0:
                number_of_guesses -= 1
            print('You have already guessed this letter!\nYou have ',number_of_warnings,' warnings left')
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                if guess in consonants:
                    number_of_guesses -= 1
                else:
                     number_of_guesses -= 2
                print('Oops! That is not a letter in my word' , get_guessed_word(secret_word, letters_guessed))
                print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            print('----------\nCongratulations, you won!')
            print('Your total score for this game is: ', compute_score(secret_word,number_of_guesses))
            break
        elif number_of_guesses == 0:
            print('You ran out of guesses. The word was: ',secret_word)
       



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

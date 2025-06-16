import random
from words import words  # Importing word list from external file
import string

# List of Hangman ASCII stages from empty to fully hanged
hangman_stages = [
    """
       --------
       |      |
       |      
       |    
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """
]

# Selects a valid word (no hyphens or spaces) from the list
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

# Main Hangman game function
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase) # A-Z
    used_letters = set()  # Letters guessed by the user
    lives = 7 # Total number of tries

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # letters used 
        # " ".join(["a", "b" "cd"]) --> "a b cd"
        print("You have", lives, "left and you have used these letters: ", " ".join(used_letters))

        # Display current word progress 
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        # Show hangman stage based on remaining lives
        print(hangman_stages[7 - lives])

        # Get user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1 # takes away a life if wrong
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("You've already used that character. Please try again. ")

        else:
            print("Invalid character. Please try again.")

    # End of game messages
    if lives == 0:
        print(hangman_stages[-1])  # final stage of hangman
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word ", word, "!")


hangman()
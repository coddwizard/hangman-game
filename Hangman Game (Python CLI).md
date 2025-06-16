Hangman Game (Python CLI)

A simple command-line Hangman game written in Python.  
Guess the word letter by letter before the Hangman is fully drawn!

---

Features

- Random word selection from a 1000+ word list
- 7-stage ASCII Hangman graphics
- Tracks and displays guessed letters
- Case-insensitive letter input
- Fully terminal-based / CLI game
- Beginner-friendly, clean code

---

Requirements

- Python 3.x  
(No additional libraries required.)

---

How to Run

Make sure the project contains the following files:

- `hangman.py` → main game script  
- `words.py` → a file that includes a list variable:  
  ```python
  words = [...]  # JSON wordlist with 2000+ words


Preview

You have 3 left and you have used these letters:  F U O I N S R A T E
Current word:  T R A N S - O R T

       --------
       |      |
       |      O
       |     \|/
       |
       |
       -

Guess a letter: p
You guessed the word  TRANSPORT !
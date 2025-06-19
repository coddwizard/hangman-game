# Import necessary libraries
import tkinter as tk
import random
from words import words  # Python file with a word list named 'words'

# Drawing stages
hangman_stages = [
    """
     --------
     |      |
     |
     |
     |
     |
    -""",
    """
     --------
     |      |
     |      O
     |
     |
     |
    -""",
    """
     --------
     |      |
     |      O
     |      |
     |
     |
    -""",
    """
     --------
     |      |
     |      O
     |     /|
     |
     |
    -""",
    """
     --------
     |      |
     |      O
     |     /|\\
     |
     |
    -""",
    """
     --------
     |      |
     |      O
     |     /|\\
     |     /
     |
    -""",
    """
     --------
     |      |
     |      O
     |     /|\\
     |     / \\
     |
    -"""
]



# Function to handle guessed letter
def guess_letter(letter, btn):
    global lives

    btn.config(state="disabled")   # Disable the clicked button

    if letter in selected_word:
        for i, char in enumerate(selected_word):
            if char == letter:
                word_display[i] = letter
        word_label.config(text=" ".join(word_display))

        if "_" not in word_display:
            word_label.config(text=f"🎉 You guessed the word!, {selected_word}")
            disable_all_buttons()
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        ascii_label.config(text=hangman_stages[min(6,7 - lives)])

        if lives == 0:
            word_label.config(text=f"💀 You died! Word was: {selected_word}")
            ascii_label.config(text=hangman_stages[-1])
            disable_all_buttons()


# Function to disable all letter buttons and enable "Start Game"
def disable_all_buttons():
    for btn in letter_buttons:
        btn.config(state="disabled")

    start_button.config(state="normal")



# Randomly select a valid word
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


# Start a new game session
def start_game():
    global selected_word, word_display, letter_buttons, lives

    selected_word = get_valid_word(words)   # Pick a new word
    word_display = ["_" for _ in selected_word]   # Create blanks
    lives = 7


    word_label.config(text=" ".join(word_display))
    lives_label.config(text=f"Lives: {lives}")
    ascii_label.config(text=hangman_stages[0])


    for btn in letter_buttons:
        btn.config(state="normal")

    start_button.config(state="disabled")
    


# Create the main game window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x650")


# Title Label
title = tk.Label(root, text="Welcome to Hangman!", font=("Helvetica", 20))
title.pack(pady=20)

# Start Button
start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14), command=start_game)
start_button.pack(pady=10)

# Word Display
word_label = tk.Label(root, text="", font=("Helvetica", 24))
word_label.pack(pady=20)

# Lives Display
lives_label = tk.Label(root, text="", font=("Helvetica", 16))
lives_label.pack(pady=10)


# Drawing Display
ascii_label = tk.Label(root, text="", font = ("Courier", 12), justify= "left")
ascii_label.pack(pady=10)


# Letter Buttons Grid
letter_frame = tk.Frame(root)
letter_frame.pack()

letter_buttons = []
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    btn = tk.Button(letter_frame, text=letter, width=4, font=("Helvetica", 12), state="disabled")
    btn.config(command=lambda l=letter, b=btn: guess_letter(l, b))
    btn.grid(row=i//9, column=i%9, padx=2, pady=2)
    letter_buttons.append(btn)

# Start the Tkinter event loop
root.mainloop()

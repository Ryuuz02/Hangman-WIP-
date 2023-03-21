# Import Statements
from random import choice
from time import sleep

# Title: Hangman
# Author: Jacob Bode

# Reads the words from the words file
with open("words.txt", "r") as f:
    words = f.readlines()
    words = [x.strip() for x in words]

# Chooses a random word
word = choice(words)

# Clean up the word
word = word.lower()
word = word.replace("-", " ")

# Makes an underscore version of the word to display
underscore_word = []
for i in range(0, len(word)):
    underscore_word.append("_")

# Preset settings
max_fails = 6
fails = 0

def draw_gallows(guesses):
    print("___________")
    print("| /       |")
    match guesses:
        case 0:
            print("|/")
            print("|")
            print("|")
            print("|")
        case 1:
            print("|/        O")
            print("|          ")
            print("|          ")
            print("|")
        case 2:
            print("|/        O")
            print("|         |")
            print("|         |")
            print("|")
        case 3:
            print("|/        O")
            print("|        /|")
            print("|         |")
            print("|")
        case 4:
            print("|/        O")
            print("|        /|\\")
            print("|         |")
            print("|")
        case 5:
            print("|/        O")
            print("|        /|\\")
            print("|         |")
            print("|        /")
        case 6:
            print("|/        O")
            print("|        /|\\")
            print("|         |")
            print("|        / \\")
    print("|")
    print("|___________\n")


# print("The word is " + word)

guessed_letters = []

# Prints out an ASCII art for the gallows and the game
while fails != max_fails and "_" in underscore_word:
    draw_gallows(fails)
    print("Previously guessed letters " + str(guessed_letters))
    print("Here is your word, do your best to guess what it is")
    print(*underscore_word, sep="")
    guess_letter = input("Type your letter then press enter\n").lower()
    # Check if the guess is 1 character
    if len(guess_letter) == 1:
        # Check if the guess is a letter
        if guess_letter.isalpha():
            # Check if the letter has already been guessed
            if guess_letter in guessed_letters:
                print("You already guessed that letter!")
            # If the letter is in the word
            elif guess_letter in word:
                print("Correct!")
                for i in range(0, len(word)):
                    if word[i] == guess_letter:
                        underscore_word[i] = guess_letter
            # If the letter is not in the word
            else: 
                print("Incorrect!")
                guessed_letters.append(guess_letter)
                fails += 1
        else:
            print("That's not a letter!")
    else:
        print("That's more than one letter!")
    sleep(1)

# Prints out the result of the game
if fails == max_fails:
    draw_gallows(fails)
    print("You lost!")
    print("The word was " + word)
else:
    print("You won!")

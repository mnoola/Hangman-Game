''' A simple console-based hangman game where the player has to guess a word by suggesting letters 
within a certain number of guesses. '''

import random
from hangman_words import words_list
from hangman_art import stages, logo

lives = 6
print(logo)

chosen_word = random.choice(words_list) 

print("\nWelcome to Hangman!")
print("You have 6 attempts to guess the word.")
print("You can guess one letter at a time.")

print("\nThe word has", len(chosen_word), "letters.")

placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"

print("Word: ", placeholder)

game_over = False
correct_guesses = []

while not game_over:

    print(f"***********************{lives}/6 LIVES LEFT***********************")
    guess = input("\nGuess a letter: ").lower()

    if guess in correct_guesses:
        print("You've already guessed the letter: \n", guess)
        continue

    display_word = ""

    for letter in chosen_word:
        if letter == guess:
            display_word += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display_word += letter
        else:
            display_word += "_"

    print("\nCurrent word: ", display_word)

    if guess not in chosen_word:
        lives -= 1
        print(f" You guessed {guess}, which is not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print("\nYou Lose. Game Over! The word was:", chosen_word)
            print("***********************YOU LOSE***********************")

    if "_" not in display_word:
        game_over = True
        print("***********************YOU WIN***********************")
        print("\nCongratulations! You've guessed the word:", chosen_word)

    print(stages[lives])


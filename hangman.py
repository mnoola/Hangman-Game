import random

# word_list = ["mother", "father", "brother", "sister", "uncle", "aunt", "cousin", "nephew", "niece"]
word_list = ["mother", "father"]

def check_guess(letter, display_word, chosen_word):
    print(letter)
    print(display_word)
    print(chosen_word)
    
    
    if letter == guess:
        display_word += letter
    else:
        display_word += "_"

    return display_word

def get_random_word():
    return random.choice(word_list) 

chosen_word = get_random_word()
# print("\nChosen word:", chosen_word)

print("\nWelcome to Hangman!")
print("You have 6 attempts to guess the word.")
print("You can guess one letter at a time.")

print("\nThe word has", len(chosen_word), "letters.")

display_word = ""
for _ in range(len(chosen_word)):
    display_word += "_"

print("Word: ", display_word)

guess = input("\nGuess a letter: ").lower()

for i in range(6):
    if guess in chosen_word:
        print("Correct guess!")
        for j in chosen_word:
            if j == guess:
                print()
                
        a = check_guess(guess, display_word, chosen_word)
    else:
        print("Wrong guess!")
        break


print("\nGame Over! The word was :", chosen_word)


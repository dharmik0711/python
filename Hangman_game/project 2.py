#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from hangman_guessing import guess_list
from hangman_life import game_name, lives

guessing_word = random.choice(guess_list)
word_len = len(guessing_word)
tries = 6
game_over = False

print(game_name)
print("The word you need to guess has " + str(word_len) + " letters.")

result = ['_' for _ in range(word_len)]

while not game_over:
    user_guessing = input("Guess a letter: ").lower()

    if user_guessing in result:
        print("You already guessed the letter '" + user_guessing + "'. Try a different one.")
        continue

    for position in range(word_len):
        letter = guessing_word[position]
        if letter == user_guessing:
            result[position] = letter

    if user_guessing not in guessing_word:
        print(f"The letter '{user_guessing}' is not in the word, try again!")
        tries -= 1
        if tries == 0:
            game_over = True
            print("Game over! You lose. The word was '" + guessing_word + "'. Play again!")

    print(f"{' '.join(result)}")

    if '_' not in result:
        game_over = True
        print("Congratulations! You guessed the word and won the game!")

    print(lives[tries])


# In[ ]:





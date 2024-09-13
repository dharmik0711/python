#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

while True:    
    print("TO WIN THE GAME, CHOOSE A NUMBER. IF IT MATCHES WITH THE COMPUTER'S NUMBER, YOU WILL WIN; ELSE, THE COMPUTER WINS.")
    your_score = 0
    computer_score = 0
    
    num = int(input("Select the color by typing the number beside it: \n 1. Black \n 2. White \n 3. Blue \n 4. Red \n 5. Green\n"))
    while num < 1 or num > 5:
        print("Enter a valid number between 1 and 5.")
        num = int(input("Select the color by typing the number beside it: \n 1. Black \n 2. White \n 3. Blue \n 4. Red \n 5. Green\n"))
    
    if num == 1:
        choice_col = "Black"
    elif num == 2:
        choice_col = "White"
    elif num == 3:
        choice_col = "Blue"
    elif num == 4:
        choice_col = "Red"
    elif num == 5:
        choice_col = "Green"   

    print("You chose " + choice_col + " color")    
    print("Now it's the computer's turn...")

    computer_choice = random.randint(1, 5)

    if computer_choice == 1:
        comp_col = "Black"
    elif computer_choice == 2:
        comp_col = "White"
    elif computer_choice == 3:
        comp_col = "Blue"
    elif computer_choice == 4:
        comp_col = "Red"
    elif computer_choice == 5:
        comp_col = "Green"  

    print("Computer selected " + comp_col + " color")

    if comp_col == choice_col:
        print("Your choice is equal to the computer's choice! You win!")
        your_score += 1
    else:
        print("Your choice is not equal to the computer's choice! Computer wins!")
        computer_score += 1

    print("Your score is:", your_score)
    print("Computer's score is:", computer_score)

 
    play = input("Do you want to continue the game? Type 'yes' to continue or 'no' to exit: ").lower()
    if play == "no":
        print("Thank you for playing the game!")
        break


# In[ ]:





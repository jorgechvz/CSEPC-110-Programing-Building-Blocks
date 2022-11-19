'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 5 (Week 7 - Week 8)
For this assignment, you will create an interactive word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way.
'''
import random
import time 
from time import sleep
from os import system
import sys

#We create lists for the program

words_characteresBoM = ['Moroni', 'Mosiah', 'Alma', 'Lehi', 'Nefi', 'Sariah']
words_animals = ['lion', 'elephant', 'bird', 'dog', 'butterfly', 'giraffe']
words_country = ['Peru', 'Netherlands', 'Gales', 'Spain', 'France', 'Argentina']
words_professions = ['Doctor', 'Nurse', 'Engineer', 'Lawyer', 'Trainer']

#-------------------------------------------------------------------------------------------------------------------------
#Funtions 
def title():#Title funtion 
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Wordle Game".center(150,'-'),"{}\n".format(t))
def menu(): #Menu funtion
    print("\n"+"Wordle Game".center(54," ")+"\n")
    print("+"+"+".rjust(50,'-'))
    print("|"+"MENU".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    print("|"+"1. Play Game".center(49," ")+"|")
    print("|"+"2. Exit Game".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    option = input("Choose one option: ") #We create the menu for the game
    if option == '1':
        choose_list()
    elif option == '2':
        sure_exit()
    else: 
        print("You need to choose a correct option, please enter again.")
        sleep(2)
        system('cls')
        menu()
def choose_list():#Choose list funtion. In this funtion, we can choose a topic for the wordle game
    system('cls')
    title()
    print("Welcome to Wordle Game\n")
    print("+"+"+".rjust(50,'-'))
    print("|"+"Topics for the Wordle Game".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    print("|"+"1. Characteres of the Book of Mormon".center(49," ")+"|")
    print("|"+"2. Animals".center(49," ")+"|")
    print("|"+"3. Countries".center(49," ")+"|")
    print("|"+"2. Professions".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    choose = input("\nChoose one option.\nPlease type CHARACTERES or ANIMALS or COUNTRIES or PROFESSIONS: ")
    if choose.lower() == "characteres":
        system('cls')
        title()
        word = random.choice(words_characteresBoM) #The "random" function picks a random word from our list
        wordle_main(word)
    elif choose.lower() == "animals":
        system('cls')
        title()
        word = random.choice(words_animals)#The "random" function picks a random word from our list
        wordle_main(word)
    elif choose.lower() == "countries":
        system('cls')
        title()
        word = random.choice(words_country)#The "random" function picks a random word from our list
        wordle_main(word)
    elif choose.lower() == "professions":
        system('cls')
        title()
        word = random.choice(words_professions)#The "random" function picks a random word from our list
        wordle_main(word)
    else:
        print("\n Please type a correct option")
        sleep(3)
        system('cls')
        choose_list() 
def wordle_main(word):#Main program funtion
    hint = '_'*len(word) #We put a hint of the word that we are going to guess but we hide it in this form "_" each letter of the word.
    print(f"Your hint is:\n{hint}")
    inner_loop = 6 #We have 6 chances to guess the word
    attemp = 0 #We put the counter of the times we try to guess the word in 0
    while inner_loop > 0: #If the chances is better than 0 run the program
        print(f"\n\nYou have {inner_loop} chances to guess the word") #We print the number of chances we have
        guess = input("\nWhat is your guess: ")
        for index in range(word.__len__()):#we create a "for" loop with an index in range of the length of the word
            if index < len(guess):#Here we see if the length of the index of the "guess" is less than the length of the "word"
                if guess[index].lower() == word[index].lower():#In this part if any of the letters of "word" is the same and in the same place of "guess" it is printed in capital letters
                    print(guess[index].upper(),end=' ')
                elif guess[index].lower() in word.lower():#In this part, if any of the letters of "word" is the same but is not in the same place as "guess", it is printed in lowercase
                    print(guess[index].lower(),end=' ')
                else:#In this part, if any of the letters of "word" is not found in "guess", "_" is printed for each letter
                    print("_"*len(guess[index]),end=' ')
        if word.lower() == guess.lower():#If "word" is exactly equal to "guess", the entire word is printed in uppercase
            print(f"\n\nCongratulations. You guessed the correct word")
            inner_loop -= 6 #We remove 6 to close the loop
        inner_loop -=1 #We remove 1 for each missed chance
        attemp += 1 #We add 1 for each guess word
    if inner_loop == 0: 
        print("You lose")
    else:
        print(f"\nGuess the word '{word.upper()}' I take you {attemp} guesses.")
    again()
def again(): #Again funtion. This funtion is for play again the wordle game
    answer = input("\nDo you play again the Wordle Game??\nPlease type 'YES' or 'NO': ")
    if answer.lower()=="yes":
        system('cls')
        choose_list()
    elif answer.lower()=="no":
        sure_exit()
    else:
        print("You need to choose a correct option, please enter again.")
        sleep(2)
        again()
def sure_exit(): #Sure exit program funtion
    a = 0
    while a == 0: 
        x = input("Do you want to exit of Wordle Game??\nPlease type YES or NO: ")
        if x.lower()=="yes": 
            system('cls')
            exit_game()
        elif x.lower()=="no":
            system('cls')
            menu()
            break
        else:
            a = 0        
def exit_game():  #Exit program funtion
    system('cls')
    title()
    print("\n"+"Thanks for using the Wordle Game. Come back soon!!!".center(150,' ')+"\n")
    sys.exit(5)

menu() #Run the program
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
def title(): #Title funtion 
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
def choose_list(): #Choose list funtion. In this funtion, we can choose a topic for the wordle game
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
        word = random.choice(words_characteresBoM)
        wordle_main(word)
    elif choose.lower() == "animals":
        system('cls')
        title()
        word = random.choice(words_animals)
        wordle_main(word)
    elif choose.lower() == "countries":
        system('cls')
        title()
        word = random.choice(words_country)
        wordle_main(word)
    elif choose.lower() == "professions":
        system('cls')
        title()
        word = random.choice(words_professions)
        wordle_main(word)
    else:
        print("\n Please type a correct option")
        sleep(3)
        system('cls')
        choose_list() 
def wordle_main(word): #Main program funtion
    guess ="" #We set the variable guess empty because that way we can use it in the loop
    attemp = 0 #We put the counter of the times we try to guess the word in 0
    while word != guess: #We create the loop for the wordle game
        guess=input("\nWhat is your guess: ").lower() #we use .lower() to convert the string to lowercase
        attemp += 1 #The counter will increase by 1 each time we use the loop.
        if word.lower() == guess: #If the word is equal to guess, the loop will end
            print("\nCongratulations! you guessed it")
            print(f"It took you {attemp} guesses")
        else: 
            print("You guess was not correct") 
    again()
def again(): #Again funtion. This funtion is for play again the wordle game
    answer = input("\nDo you play again the Wordle Game??\nPlease type 'YES' or 'NO': ")
    if answer.lower()=="yes":
        system('cls')
        menu()
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
def exit_game(): #Exit program funtion
    system('cls')
    title()
    print("\n"+"Thanks for using the Wordle Game. Come back soon!!!".center(150,' ')+"\n")
    sys.exit(5)
menu()
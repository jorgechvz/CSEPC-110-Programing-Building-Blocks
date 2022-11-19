'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 4 (Week 5 - Week 6)
In a text-based adventure game, the user is presented a scenario with different options. Depending on the option they choose, they have different consequences, which in turn present different choices for the next action.
'''
#libraries
import time 
from time import sleep
from os import system
import sys

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the title and menu

def title():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("The Last Knight".center(150,'-'),"{}\n".format(t))
def menu():
    print("\n"+"The Last Knight".center(54," ")+"\n")
    print("+"+"+".rjust(50,'-'))
    print("|"+"MENU".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    print("|"+"1. Play Game".center(49," ")+"|")
    print("|"+"2. Exit Game".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    option = input("Choose one option: ") #We create the menu for the game
    if option == '1':
        personage()
    elif option == '2':
        sure_exit()
    else: 
        print("You need to choose a correct option, please enter again.")
        sleep(3)
        system('cls')
        menu()

#--------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the main-game        

def personage():
    system('cls')
    title()
    global name, character #Variable that we use in whole game
    print("Welcome to The Last Knight\n")
    print("Since ancient times many dragons have attacked entire cities creating panic among the inhabitants around the world.\nIn the city of Neuss there are 3 knights who are willing to confront them to restore order to the world. Aegon the Unlikely, Duncan the Tall, and Daeron the Strong.\n")
    print("You have 3 personages to choose:\n1.Aegon\n2.Duncan\n3.Daeron")
    print("\nNote: Each character has 3 lives and also each character will only have the availability to ask for help 2 times in the game. This help message will appear when you have only one life in the game.")
    character = {} #we create a variable of list for create a personage
    a = 0
    while a == 0: #Loop for choose personage
        name = str(input("\nPlease choose your personage:"))
        if name.lower() == "aegon":
            character["character"] = "Aegon"
            character["live"] = 3
            character["help"] = 2
            break
        elif name.lower() == "duncan":
            character["character"] = "Duncan"
            character["live"] = 3
            character["help"] = 2
            break
        elif name.lower() == "daeron":
            character["character"] = "Daeron"
            character["live"] = 3
            character["help"] = 2
            break
        else:
            print("You need to choose a correct personage, please enter again.")
            a = 0   
    print("\nYou choose", character["character"], "this personage have", character["live"],"lives.")
    print("\nNow you are ready to start this dragon hunting adventure.")
    b = 0
    while b == 0: #Loop for the start game
        start_option = input("Do you have want to start the adventure?\nPlease type 'YES' or 'NO': ")
        if start_option.lower() == "yes":
            level1()
            break
        elif start_option.lower() == "no":
            sure_exit()
            break
        else:
            print("\nYou need to choose a correct option, please enter again.")
            b = 0
def level1():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 1: The way to the Castle".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nRumor has it that there are some dragons in a faraway castle, go so you can fight them and free that castle.")
    decision = input("Do you want to go that castle?\nPlease type 'YES' or 'NO': ")#loop for the first decision in Level1
    if decision.lower()=="yes":
        sub_part_leve1()
    elif decision.lower()=="no":
        lose_game()
    else:
        choose_well()
        level1()
def level2():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 2: The Dark Town".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nWelcome to level 2, this is the last level of the first edition of the game. It's amazing that you've come this far! In this level you will find yourself in a town very far from the city of Neuss. This town has been affected by a dense darkness. You will only find one dragon in this town but there are many traps that have been set inside the town. You must be careful. You have to walk in the right direction to reach the dragon and kill it. Warnings have been placed along the way to help you get on the right path. Pay attention!! Good luck!!")
    option = input("Do you want continue in the game?\nPlease type 'YES' or 'NO': ") #Loop for decision in second part in level 2
    if option.lower() == "yes":
        lvl2_firstpart()
    elif option.lower() == "no":
        lose_game()
    else:
        choose_well()
        level2()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the parts of Level 1

def sub_part_leve1():
    system("cls")
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 1: The way to the Castle".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nYou are now inside the castle. Nearby sources say that there are 2 dragons, one is on the first floor of the castle and the other is on the last tower of the castle. Face the dragon on the first floor first but be careful remember you only have 3 lives.")
    a = 0 #loop for the decision in the part of sub level 1
    while a == 0:
        decision1 = str(input("Do you want to FIGHT the dragon or RUN AWAY?\nPlease type 'FIGHT' or 'RUN AWAY': "))
        if decision1.lower() == "fight":
            sublevel1()
            break
        elif decision1.lower() == "run away":
            print("You ran out of the castle")
            sleep(3)
            lose_game()
            break
        else:
            print("\nYou need to choose a correct option, please enter again.")
            a = 0
def sublevel1():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 1: The way to the Castle - I Chapter".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nYou decided to fight, inside the castle, on the first floor you will find a spear and a sword. The spear has a power of 15 and the sword has a power of 20. Only the dragon can die with a power of 18 or more.\nRemember choose well!!!")
    decision3 = input("Do you choose the SWORD(20 power) or the SPEAR(15 power)?\nPlease type 'SWORD' o'SPEAR': ")
    if decision3.lower()=="sword":
        won_level()
        sublevel2()
    elif decision3.lower()=="spear":
        print("\nOh no!! The dragon kill you")
        character["live"] = character["live"]-1
        if character["live"] == 0:
            lose_game()
        elif character["live"] <= 1:
            a = 0 #Loop for the help message 
            while a==0:
                help_me = input("\nYou now have only one life, do you want us to help you so you don't lose?\nPlease type 'YES' or 'NO': ")
                if help_me.lower()=="yes":
                    character["help"] = character["help"] - 1
                    if character["help"] > 0:
                        system('cls')
                        title()
                        print("\nNow you only have",character["help"],"option to ask for help in the whole game")
                        print("\nHelp message: You must look carefully at the power of each weapon, remember that to kill the dragon, the power of your weapon must be equal to the life of the dragon.The weapon you need does not have the ability to launch, it is only for wielding.")
                        sleep(15)
                        sublevel1()
                        break
                    elif character["help"] <= 0:
                        system('cls')
                        title()
                        print("You no longer have any more helps in the game. We are sorry.")
                        sublevel1()
                        break
                elif help_me.lower() == "no":
                    print("\nLet's try again, remember to choose well.")
                    sleep(3)
                    system('cls')
                    title()
                    print("Now you have",character["live"], "live(s)")
                    sleep(5)
                    sublevel1()
                    break
                else:
                    print("\nYou need to choose a correct option, please enter again.")
                    a = 0
        elif character["live"] > 0:
            print("\nLet's try again, remember to choose well.")
            sleep(3)
            system('cls')
            title()
            print("Now you have",character["live"], "live(s)")
            sleep(5)
            sublevel1()
    else:
        choose_well()
        sublevel1()
def sublevel2():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 1: The way to the Castle - II Chapter".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nYou are already in the last tower, this dragon is stronger, it has 40 live but don't scare you, in this tower you will find a fire thrower that has only 18 power and you will also find a 25 crossbow, to kill the dragon you have to reach a power of 40, you will have to attack it twice.")
    decision4 = input("\nDo you choose the FIRE THROWER(18 power) or the CROSSBOW(20 power)?\nPlease type 'FIRE THROWER' or 'CROSSBOW': ")
    crossbow = 20
    fire_thrower = 18
    if decision4.lower()=="crossbow":
        attack_lvl1(crossbow)        
    elif decision4.lower()=="fire thrower":
        attack_lvl1(fire_thrower)
    else:
        choose_well()
        sublevel2()

#Funtions for attack and lose live for Level 1

def attack_lvl1(weapon): #Funtion for the attack in level 1
    live_dragon = 40
    print("\nWe will launch the first attack")
    sleep(2)
    first_attack= live_dragon - weapon
    print("Now the dragon has {} health".format(first_attack))
    if first_attack < 40:
        c = 0
        while c ==0:
            attack = input("\nWe will launch the second attack, do you want to do it?\nPlease type 'YES' or 'NO': ")
            if attack.lower()=="yes":
                second_atack = first_attack - weapon
                if second_atack == 0:
                    won_level()
                    level2()
                    break
                elif second_atack > 0: 
                    lose_sublevel2()
                    break
            elif attack.lower()=="no":
                if first_attack == 0:
                    won_level()
                    level2()
                    break
                elif first_attack > 0:
                    lose_sublevel2()
                    break
            else:
                print("\nYou need to choose a correct option, please enter again.")
                c=0
def lose_sublevel2(): #Funtion for the "lose" in level 1
    print("Oh no!! The dragon kill you")
    character["live"] = character["live"]-1
    if character["live"] == 0:
        lose_game()
    elif character["live"] <= 1:
        a = 0
        while a==0:
            help_me = input("\nYou now have only one life, do you want us to help you so you don't lose?\nPlease type 'YES' or 'NO': ")
            if help_me.lower()=="yes":
                character["help"] = character["help"] - 1
                if character["help"] > 0:
                    system('cls')
                    title()
                    print("\nNow you only have",character["help"],"option to ask for help in the whole game")
                    print("\nHelp message: You must look carefully at the power of each weapon, remember that to kill the dragon, the power of your weapon must be equal to the life of the dragon. In this case you have to attack him twice.The weapon you need is similar to a bow.")
                    sleep(15)
                    sublevel2()
                    break
                elif character["help"] == 0:
                    system('cls')
                    title()
                    print("You no longer have any more helps in the game. We are sorry.")
                    sleep(5)
                    sublevel2()
                    break
            elif help_me.lower() == "no":
                print("\nLet's try again, remember to choose well.")
                sleep(3)
                system('cls')
                title()
                print("Now you have",character["live"], "live(s)")
                sleep(5)
                sublevel2()
                break
            else:
                print("\nYou need to choose a correct option, please enter again.")
                a = 0                        
    elif character["live"] > 0:
        print("\nLet's try again, remember to choose well.")
        sleep(3)
        system('cls')
        title()
        print("Now you have",character["live"], "live(s)")
        sleep(5)
        sublevel2()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the parts of Level 2    

def lvl2_firstpart():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 2: The Dark Town - I Chapter".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nThis is the first chapter of the level, now you are about to enter the town. While you are walking to the entrance of the town you notice that there are two paths you can take, one is to the EAST and the other to the WEST. You hear very loud noises coming from the east path and see that the other path is clear.")
    path = input("\nWhich path do you want to choose? Only one of them is correct. Remember to be careful in your choice.\nPlease type 'EAST' or 'WEST': ")
    if path.lower()=="west":
        lvl2_part2()
    elif path.lower()=="east":
        print("Oh no!! You made your decision wrong :C")
        character["live"] = character["live"]-1
        if character["live"] == 0:
            lose_game()
        elif character["live"] <= 1:
            a = 0
            while a==0:
                help_me = input("\nYou now have only one life, do you want us to help you so you don't lose?\nPlease type 'YES' or 'NO': ")
                if help_me.lower()=="yes":
                    character["help"] = character["help"] - 1
                    if character["help"] > 0:
                        system('cls')
                        title()
                        print("\nNow you only have",character["help"],"option to ask for help in the whole game")
                        print("\nHelp message: The path that you must take you can pass quietly without hearing any noise")
                        sleep(10)
                        lvl2_firstpart()
                        break
                    elif character["help"] == 0:
                        system('cls')
                        title()
                        print("You no longer have any more helps in the game. We are sorry.")
                        sleep(5)
                        lvl2_firstpart()
                        break
                elif help_me.lower() == "no":
                    print("\nLet's try again, remember to choose well.")
                    sleep(3)
                    system('cls')
                    title()
                    print("Now you have",character["live"], "live(s)")
                    sleep(5)
                    lvl2_firstpart()
                    break
                else:
                    print("\nYou need to choose a correct option, please enter again.")
                    a = 0                        
        elif character["live"] > 0:
            print("\nLet's try again, remember to choose well.")
            sleep(3)
            system('cls')
            title()
            print("Now you have",character["live"], "live(s)")
            sleep(5)
            lvl2_firstpart()
    else:
        choose_well()
        lvl2_firstpart()
def lvl2_part2():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 2: The Dark Town - II Chapter".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nNow you have reached the second stage of level 2, at this stage you are already inside the town, while walking you found a big hole with lava, around you you see things that you can choose to help you cross the hole. You have a LADDER that you can use as a bridge, you have a ROPE that you can use to swing across to the other side of the hole, and you see that you can WALK to the edge of the hole to get across.")
    decision = input("What decision are you going to make?\nPlease type 'LADDER' or 'ROPE' or 'WALK': ")
    if decision.lower()=="ladder":
        lose_part2()
    elif decision.lower()=="rope":
        lose_part2()
    elif decision.lower()=="walk":
        lvl2_finalpart()
    else:
        choose_well()
        lvl2_part2()
def lvl2_finalpart():
    system('cls')
    title()
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("|"+"Level 2: The Dark Town - II Chapter".center(120," "),"|"+" Lives: {}".center(44," ").format(character["live"])+"|")
    print("+"+"+".rjust(122,'-')+"+".rjust(44,'-'))
    print("\nYou have reached the last part of the level and the game. You are now in front of the dragon, your mission is to kill it. For you to achieve that there are some weapons around you that you can use. There is a KATANA (20 power), a CANNON (40 power), a HAMMER (30 power) and DAGGER (33 power). The dragon has 100 health. You only have 3 chances to attack it with the weapon of your choice. The sum of those 3 chances has to be equal to or greater than the dragon's life to kill it. Go for the dragon!!")
    katana = 20
    cannon = 40
    hammer = 30
    dagger = 33
    arm = input("\nWhat weapon do you want to take?\nPlease type 'KATANA' or 'CANNON' or 'HAMMER' or 'DAGGER': ")
    if arm.lower() == "katana":
        attack_lvl2(katana)
    elif arm.lower() == "cannon":
        attack_lvl2(cannon)
    elif arm.lower() == "hammer":
        attack_lvl2(hammer)
    elif arm.lower() == "dagger":
        attack_lvl2(dagger)
    else:
        choose_well()
        lvl2_finalpart()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for attack and lose live for level 2

def lose_part2():
    print("Oh no!! You made your decision wrong :C")
    character["live"] = character["live"]-1
    if character["live"] == 0:
        lose_game()
    elif character["live"] <= 1:
        a = 0
        while a==0:
            help_me = input("\nYou now have only one life, do you want us to help you so you don't lose?\nPlease type 'YES' or 'NO': ")
            if help_me.lower()=="yes":
                character["help"] = character["help"] - 1
                if character["help"] > 0:
                    system('cls')
                    title()
                    print("\nNow you only have",character["help"],"option to ask for help in the whole game")
                    print("\nHelp message: You don't need any tools to cross the hole, you just need your feet to get through.")
                    sleep(15)
                    lvl2_part2()
                    break
                elif character["help"] == 0:
                    system('cls')
                    title()
                    print("You no longer have any more helps in the game. We are sorry.")
                    sleep(5)
                    lvl2_part2()
                    break
            elif help_me.lower() == "no":
                print("\nLet's try again, remember to choose well.")
                sleep(3)
                system('cls')
                title()
                print("Now you have",character["live"], "live(s)")
                sleep(5)
                lvl2_part2()
                break
            else:
                print("\nYou need to choose a correct option, please enter again.")
                a = 0                        
    elif character["live"] > 0:
        print("\nLet's try again, remember to choose well.")
        sleep(3)
        system('cls')
        title()
        print("Now you have",character["live"], "live(s)")
        sleep(5)
        lvl2_part2()
def attack_lvl2(weapon):
    dragon_live = 100
    print("\nWe will launch the first attack")
    sleep(2)
    first_attack = dragon_live - weapon
    print("Now the dragon has {} health".format(first_attack))
    a = 0
    while a==0:
        decision_attack = input("\nWe will launch the second attack, do you want to do it?\nPlease type 'YES' or 'NO': ")
        if decision_attack.lower()=="yes":
            second_attack = first_attack - weapon
            print("Now the dragon has {} health".format(second_attack))
            sleep(2)
            b = 0
            while b == 0:
                second_decision_attack = input("\nWe will launch the third attack, do you want to do it?\nPlease type 'YES' or 'NO': ")
                if second_decision_attack.lower() == "yes":
                    third_attack = second_attack - weapon
                    if third_attack <= 0:
                        win_game()
                        break
                    elif third_attack > 0: 
                        print("\nYour power did not reach 100")
                        lose_finalpart()
                        break
                elif second_decision_attack.lower() == "no":
                    if second_attack <= 0:
                        win_game()
                        break
                    elif second_attack > 0:
                        print("\nYour power did not reach 100")
                        lose_finalpart()
                        break
                else:
                    print("\nYou need to choose a correct option, please enter again.")
                    b = 0
        elif decision_attack.lower()=="no":
            if first_attack == 0:
                win_game()
                break
            elif first_attack > 0:
                print("\nYour power did not reach 100")
                lose_finalpart()
                break
        else:
            print("\nYou need to choose a correct option, please enter again.")
            a=0
def lose_finalpart():
    print("\nOh no!! The Dragon kill you :C")
    character["live"] = character["live"]-1
    if character["live"] == 0:
        lose_game()
    elif character["live"] <= 1:
        a = 0
        while a==0:
            help_me = input("\nYou now have only one life, do you want us to help you so you don't lose?\nPlease type 'YES' or 'NO': ")
            if help_me.lower()=="yes":
                character["help"] = character["help"] - 1
                if character["help"] > 0:
                    system('cls')
                    title()
                    print("\nNow you only have",character["help"],"option to ask for help in the whole game")
                    print("\nHelp message: Remember that the sum of the 3 chances you have to hit it must add up to the dragon's health or greater. The weapon that fulfills that, has a hole.")
                    sleep(15)
                    lvl2_finalpart()
                    break
                elif character["help"] == 0:
                    system('cls')
                    title()
                    print("You no longer have any more helps in the game. We are sorry.")
                    sleep(5)
                    lvl2_finalpart()
                    break
            elif help_me.lower() == "no":
                print("\nLet's try again, remember to choose well.")
                sleep(3)
                system('cls')
                title()
                print("Now you have",character["live"], "live(s)")
                sleep(5)
                lvl2_finalpart()
                break
            else:
                print("\nYou need to choose a correct option, please enter again.")
                a = 0                        
    elif character["live"] > 0:
        print("\nLet's try again, remember to choose well.")
        sleep(3)
        system('cls')
        title()
        print("Now you have",character["live"], "live(s)")
        sleep(5)
        lvl2_finalpart() 

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the use global in the game

def won_level():
    system('cls')
    title()
    print("Well done, you kill them")
    character["live"] = character["live"] + 1
    print("\nYou won a 1 live more.\nYou now have",character["live"],"live(s)")
    sleep(5)
    system('cls')
    title()
def choose_well():
    system('cls')
    title()
    print("\nYou need to choose a correct option, please enter again.")
    sleep(3)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the win and lose game

def win_game():
    system('cls')
    title()
    print("Congratulations, you win!!!!".center(150,' '))
    print("\n"+"You have passed all levels of the game successfully. You were the last knight to defend the city of Neuss. Now your city is safe.".center(150,' ')+"\n")
    print("1. Back to Menu")
    print("2. Exit Game")
    option = input("Please choose one option: ")
    if option == "1":
        menu()
    elif option == "2":
        sure_exit() 
    else:
        choose_well()
        menu()
def lose_game():
    system('cls')
    title()
    print("+"+"+".rjust(50,'-'))
    print("|"+"You Lose".center(49," ")+"|")
    print("+"+"+".rjust(50,'-'))
    print("|"+"1.".rjust(18,' ') + "Play Again"+"|".rjust(22,' '))
    print("|"+"2.".rjust(18,' ') + "Exit Game"+"|".rjust(23,' '))
    print("+"+"+".rjust(50,'-'))
    option = input("Choose one option: ")
    if option == '1':
        system('cls')
        menu()
    elif option == '2':
        sure_exit()
    else: 
        print("You need to choose a correct option, please enter again.")
        sleep(3)
        system('cls')
        lose_game()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Funtions for the exit game

def sure_exit():
    a = 0
    while a == 0: 
        x = input("Do you want to exit of The Last Knight??\nPlease type YES or NO: ")
        if x.lower()=="yes": 
            system('cls')
            exit_game()
            break 
        elif x.lower()=="no":
            system('cls')
            menu()
            break
        else:
            a = 0        
def exit_game():
    system('cls')
    title()
    print("\n"+"Thanks for using the game: The Last Knight. Come back soon!!!".center(150,' ')+"\n")
    sys.exit(5)

#-----------------------------------------------------------------------------------------------------------------------------------------------
menu() #Run game

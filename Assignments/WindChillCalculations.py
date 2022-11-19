""" 
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 7 (Week 13)
Your assignment is to write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.""" 

import time 
from time import sleep
from os import remove, system
import sys
import math

def title(): #Funtion for the title
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Wind Chill Chart".center(150,'-'),"{}\n".format(t))

#Funtions for the convertions and wind chill chart formula
def celcius_to_fahrenheit(celcius):
    temp_fahrenheit = (celcius * (9/5)) + 32
    return temp_fahrenheit

def wind_chill_chart(temp, wind):
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * (pow(wind,0.16)) + 0.4275 * temp * (pow(wind,0.16))
    return wind_chill

def menu(): #funtion for the program menu
    title()
    print("1. For Fahrenheit: ")
    print("2. For Celsius")
    print("3. Exit")
    option = input("Please enter an action: ")
    if option.lower() == "1":
        system('cls')
        title() 
        program_fahrenheit() #Call the funtion add_product
    elif option == "2":
        system('cls')
        title()
        program_celcius()
    elif option == "3":
        sure_quit_program() #call the tuntion sure_quit_program
    else: 
        print("\nPlease enter a correct option")
        sleep(3)
        system("cls")
        menu()
    
#Funtions for the main program to fahrenheit and celcius
def program_fahrenheit():
    temp = float(input("What is the temperature?: "))
    print(f"\nFor {temp:.1f}°F\n")
    for i in range(5,61,5):
        wind_chill_calculations = wind_chill_chart(temp,i)
        print(f"At temperature {temp:.1f}°F, and wind speed {i} mph. the windchill is: {wind_chill_calculations:.2f}°F")
    input("Press ENTER to return menu...")
    system("cls")
    menu()

def program_celcius():
    temp = float(input(f"What is the temperature?: "))
    temp = celcius_to_fahrenheit(temp)
    print(f"\nFor {temp:.1f}°F\n")
    for i in range(5,61,5):
        wind_chill_calculations = wind_chill_chart(temp,i)
        print(f"At temperature {temp:.1f}°F, and wind speed {i} mph. the windchill is: {wind_chill_calculations:.2f}°F")
    input("Press ENTER to return menu...")
    system("cls")
    menu()

#Funtios to quit program
def sure_quit_program(): #Sure exit program funtion
    a = 0
    while a == 0: 
        x = input("Do you want to exit of Wind Chill Chart??\nPlease type YES or NO: ")
        if x.lower()=="yes": 
            system('cls')
            exit_game()
        elif x.lower()=="no":
            system('cls')
            menu()
            a = 1
        else:
            a = 0        
def exit_game():  #Exit program funtion
    system('cls')
    title()
    print("\n"+"Thanks for using Wind Chill Chart. Come back soon!!!".center(150,' ')+"\n")
    sys.exit(5)
menu()
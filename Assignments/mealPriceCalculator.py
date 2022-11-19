'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 3 
Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.
'''
#libraries
import time
from os import system
import sys
#Funtion for title
def title():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Meal Price Calculator".center(100,'-'),"{}\n".format(t))
#Function to make the program more interactive
def welcome():
    title()
    global name
    print("Welcome to Meal Price Calculator\n")
    name = str(input("Please type your name:"))
    calculator()
#Funtion for the input data of meal price calculator
def calculator():
    system('cls')
    title() #Call the funtion title
    print("Thank you very much for using Meal Price Calculator {}, we hope that this program will help you with what you need.\nPlease type your answers to the follow questions :D!!\n".format(name))
    #Declare global variables for the program
    global child_meal, adult_meal, drink_child, drink_adult, children, adults, rate 
    #Variables for data input for the program, we create a loop for verify the input data is a "int" or "float"
    #The "while True" loop will help us to ensure that the program does not finish until the user has entered a correct value. We use "Try" and "Except" to search for errors. If the user enters the data correctly, the loop will end and go to the next question. If in case it finds an error, "Except" acts to catch the error and display a message.
    while True: 
        try:
            child_meal= float(input("What's the price of a child's meal: "))
            break
        except ValueError: #We use the "ValueError" exception to catch the type of error.
            print("This is not a correct price, please enter a correct price")
    while True:
        try:        
            adult_meal= float(input("What's the price of a adult's meal: "))
            break
        except ValueError:
            print("This is not a correct price, please enter a correct price")
    while True:
        try:
            drink_child=float(input("What's the price of child's drink: "))
            break
        except ValueError:
            print("This is not a correct price, please enter a correct price")
    while True:
        try:
            drink_adult=float(input("What's the price of adults's drink: "))
            break
        except ValueError:
            print("This is not a correct price, please enter a correct price")
    while True:
        try:
            children= int(input("How many children are there: "))
            break
        except ValueError:
            print("Child numbers must be an integer, please enter an integer")
    while True:
        try:
            adults= int(input("How many adults are there: "))
            break
        except ValueError:
            print("Adults numbers must be an integer, please enter an integer")
    while True:
        try:
            rate= float(input("What is the sales tax rate: "))
            break
        except ValueError:
            print("This is not a correct number for a sales tax, please enter a correct one.")
    system('cls')
    verify() #Call the funtion "Verify"
   
#Funtio to Verify
def verify():
    title()
    #Results of input data 
    print("Your price of a child's meal is: ${:.2f}".format(child_meal))
    print("Your price of a adult's meal is: ${:.2f}".format(adult_meal))
    print("Your price of a child's drink is: ${:.2f}".format(drink_child))
    print("Your price of a adult's drink is: ${:.2f}".format(drink_adult))
    print("There are {} children".format(children))
    print("There are {} adults".format(adults))
    print("Your rate is: {}%".format(rate))
    a = 0
    while a == 0: #We create a loop to verify input data
        x = input("\n{} the input data into the calculator is correct??\nPlease type YES or NO: ".format(name))
        if x.lower()=="yes": #We use the "lower" method to validate the input string
            system("cls")
            operations() #If it's good, we call the funtion "operations"
        elif x.lower()=="no":
            system('cls')
            calculator()#If it's not good, we call the "calculator" function again to enter the input data again.
        else:
            a = 0
#Funtion of the operations 
def operations():
    #Development to calculate the sale
    subtotal = ((child_meal + drink_child) * children) + ((adult_meal + drink_adult) * adults) #Subtotal calculation
    salesTax = (subtotal * rate)/100 #Sales tax calculation
    total = subtotal + salesTax #Total of sale
    title()
    #Results of program
    print("{} the results of Meal Price Calculator is: \n".format(name))
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Sales Tax ({0}% of ${1:.2f}): ${2:.2f}".format(rate, subtotal, salesTax))
    print("Total: ${:.2f}".format(total))  
    a = 0
    while a == 0: #We create a loop to see if we want to add tip
        x = input("\n{} do you want to add tip???\nPlease type YES or NO: ".format(name))
        if x.lower()=="yes": #We use the "lower" method to validate the input string
            give_tip = float(input("\nHow much percentage of ${:.2f} (Total) do you want to tip??: ".format(total)))
            tip_total = (total*give_tip)/100 #Tip calculation
            total1 = subtotal + salesTax + tip_total #Total to pay
            system('cls')#clean the window of console
            #Results for sale
            title()#call the funtion title
            print("Your new calculation with the tip included is: ")
            print("\nSubtotal: ${:.2f}".format(subtotal))
            print("Sales Tax ({0}% of ${1:.2f}): ${2:.2f}".format(rate, subtotal, salesTax))
            print("Total: ${:.2f}".format(total))
            print("\nTip ({0}% of ${1:.2f}): ${2:.2f}".format(give_tip, total, tip_total))
            print("Total to pay: ${:.2f}".format(total1).upper())  
            #Variable for payment
            while True:
                try:
                    payment = float(input("\nWhat's the payment amount: $"))
                    #Development to calculate the change
                    change = payment - total1
                    #Result for change 
                    print("\nYour change is: ${:.2f}".format(change))
                    again()  
                except ValueError:
                    print("This isn't a correct payment amount, plese type a correct payment amount")
        elif x.lower()=="no":
            #Variable for payment
            while True:
                try:
                    payment = float(input("\nWhat's the payment amount: $"))
                    #Development to calculate the change
                    change = payment - total
                    #Result for change 
                    print("\nYour change is: ${:.2f}".format(change))
                    again()  
                except ValueError:
                    print("This isn't a correct payment amount, plese type a correct payment amount")
        else:
            a = 0

#Program exit funtion
def again():
    a = 0
    while a == 0: #We create a loop to see if we want to use the program again
        x = input("\n{} do you want to use the Meal Price Calculator again??\nPlease type YES or NO: ".format(name))
        if x.lower()=="yes": #We use the "lower" method to validate the input string
            system('cls')
            welcome() #If the answer is yes, we call the funtion "Calculator"
        elif x.lower()=="no":
            exitCalculator() #if the answer is no, we call the funtion "ExitCalculator"
        else:
            a = 0

#Funtion for a safe exit
def exitCalculator():
    a = 0
    while a == 0: #We create a loop to see if it is safe to exit
        x=input("Are you sure you want to leave??\nPlease type YES or NO: ")
        if x.lower()=='yes':#We use the "lower" method to validate the input string
            system('cls')
            print('Thank you for using the "Meal Price Calculator" {}. Come back soon!!'.center(100,'-').format(name)+'\n\n') #if the answer is yes, we close the program
            sys.exit(3) #Waiting time to close the program
        elif x.lower()=='no':
            again() #if the answer is no, we call the funtion "again"  
        else:
            a = 0

#We run the funtions
welcome()

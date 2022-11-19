'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 5 (Week 9 - Week 10)
For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.
'''

import time 
from time import sleep
from os import remove, system
import sys

products=[] #Variable for the list

def title(): #Funtion for the title
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Shopping Cart".center(150,'-'),"{}\n".format(t))
def menu(): #funtion for the program menu
    title()
    print("1. Add product: ")
    print("2. Remove product")
    print("3. View cart")
    print("4. Compute Total")
    print("5. Exit")
    option = input("Please enter an action: ")
    if option.lower() == "1":
        system('cls')
        title() 
        add_product() #Call the funtion add_product
    elif option == "2":
        system('cls')
        title()
        remove() #call the funtion remove
    elif option == "3":
        system('cls')
        title()
        view() #call the funtion view
    elif option=="4":
        system("cls")
        title()
        compute_total() #call the funtion compute_total
    elif option == "5":
        sure_quit_program() #call the tuntion sure_quit_program
    else: 
        menu()
def add_product(): #Funtion for the add product
    add_products = input("What item would you like to add?: ") 
    products.append(add_products) #add to the list products
    print(f"Your product was added: {add_products.capitalize()}")
    sleep(3)
    a = 0
    while a == 0:
        add_again = input("Add another?\nType 'YES' or 'NO': ")
        if add_again.lower() == "yes":
            system("cls")
            title()
            add_product()
            a = 1
        elif add_again.lower() == "no":
            system("cls")
            menu()
            a = 1
        else:
            print("Please type a correct option")
            a = 0
def remove(): #Funtion remove item in the list products
    if len(products) == 0:
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0:
        print("+----+--------------+")
        print("| ID |    PRODUCT   |")
        print("+----+--------------+")
        for index in range(len(products)): #Loop "for" each item in the length of the list products
            print("|"+f"{index+1}".center(4,' ')+"|"+f"{products[index]}".center(14,' ').capitalize() +"|")
            print("+----+--------------+")
        i = int(input("\nWhat product do you want to remove?\nPlease type the product's ID: "))
        i -= 1 
        a = 0
        while a == 0:
            sure = input("Are you sure?\nType 'YES' or 'NO': ")
            if sure.lower() == "yes":
                products.remove(products[i])
                print("Item removed")
                sleep(2)
                system("cls")
                menu()
                a = 1
            elif sure.lower() == "no":
                system("cls")
                title()
                remove()
                a = 1
            else:
                print("Please type a correct option")
                a = 0
def view():
    if len(products) == 0:
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0:
        print("+----+--------------+")
        print("| ID |    PRODUCT   |")
        print("+----+--------------+")
        for index in range(len(products)):
            print("|"+f"{index+1}".center(4,' ')+"|"+f"{products[index]}".center(14,' ').capitalize() +"|")
            print("+----+--------------+")
        sleep(5)
        system("cls")
        menu()
def compute_total():
    print("This part of the program is in process, come back later")
    sleep(5)
    system("cls")
    menu()

def sure_quit_program(): #Sure exit program funtion
    a = 0
    while a == 0: 
        x = input("Do you want to exit of Shopping Cart??\nPlease type YES or NO: ")
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
    print("\n"+"Thanks for using Shopping Cart. Come back soon!!!".center(150,' ')+"\n")
    sys.exit(5)
menu()
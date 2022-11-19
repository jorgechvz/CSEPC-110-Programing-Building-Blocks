'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 5 (Week 9 - Week 10)
For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.
'''

import time 
from time import sleep
from os import remove, system
import sys
from turtle import back

products=[]
prices=[]

def title():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Shopping Cart".center(150,'-'),"{}\n".format(t))

def menu():
    title()
    print("1. Add product and price: ")
    print("2. Remove product")
    print("3. View cart")
    print("4. Compute Total")
    print("5. Modify")
    print("6. Exit")
    option = input("Que desea hacer: ")
    if option.lower() == "1":
        system('cls')
        title()
        add_product()
    elif option == "2":
        system('cls')
        title()
        remove()
    elif option == "3":
        system('cls')
        title()
        view()
    elif option=="4":
        system('cls')
        title()
        compute_total()
    elif option =="5":
        system('cls')
        title()
        modify()
    elif option == "6":
        sure_quit_program()
    else: 
        menu()

def add_product():
    return_menu=""
    while return_menu != "menu":
        return_menu = input("If you want return to menu, type 'MENU'.If you want continue, type any letter: ").lower()
        add_products = input("What product would you like to add?: ").lower()
        products.append(add_products)
        add_price = float(input("Add the price of the new product: "))
        prices.append(add_price)
        id_product = products.index(add_products)+1
        print(f"\nYour product was added.\nProduct name: {add_products.capitalize()}\nProduct price: ${add_price:.2f}\nProduct ID: {id_product}")
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
    system("cls")
    menu()

def remove():
    if len(products) == 0:
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0:
        print("+----+--------------+---------+")
        print("| ID |    PRODUCT   |  PRICE  |")
        print("+----+--------------+---------+")
        for i in range(len(products)):
            print("|"+f"{i+1}".center(4,' ')+"|"+f"{products[i].capitalize()}".center(14,' ') +"|"+ f"${prices[i]:.2f}".center(9," ")+"|")
            print("+----+--------------+---------+")
        return_remove=""
        while return_remove != "menu":
            return_remove = input("If you want return to menu, type 'MENU'.If you want continue, type any letter: ").lower()
            i = int(input("\nWhat product do you want to remove?\nPlease type the product's ID: "))
            i -= 1 
            a = 0
            while a == 0:
                sure = input("Are you sure?\nType 'YES' or 'NO': ")
                if sure.lower() == "yes":
                    products.remove(products[i])
                    prices.remove(prices[i])
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
        system("cls")
        menu()

def view():
    if len(products) == 0:
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0:
        print("+----+--------------+---------+")
        print("| ID |    PRODUCT   |  PRICE  |")
        print("+----+--------------+---------+")
        for i in range(len(products)):
            print("|"+f"{i+1}".center(4,' ')+"|"+f"{products[i].capitalize()}".center(14,' ') +"|"+ f"${prices[i]:.2f}".center(9," ")+"|")
            print("+----+--------------+---------+")
        return_view=""
        while return_view =="menu":
            return_view = input("If you want return to menu, type 'MENU'").lower()
            system("cls")
            menu()
            
def compute_total():
    if len(products) == 0:
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0:
        print("+--------------+---------+")
        print("|    PRODUCT   |  PRICE  |")
        print("+--------------+---------+")
        for i in range(len(products)):
            print("|"+f"{products[i].capitalize()}".center(14,' ') +"|"+ f"${prices[i]:.2f}".center(9," ")+"|")
            print("+--------------+---------+")
        sum_prices = sum(prices)
        print("|"+"TOTAL PRICE".center(14,' ')+"|"+f"${sum_prices:.2f}".center(9,' ')+"|")
        print("+--------------+---------+")
        return_compute=""
        while return_compute == "menu":
            return_compute = input("If you want return to menu, type 'MENU'").lower()
            system("cls")
            menu()
    
def modify():
    if len(products) == 0:
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0:
        print("+----+--------------+---------+")
        print("| ID |    PRODUCT   |  PRICE  |")
        print("+----+--------------+---------+")
        for i in range(len(products)):
            print("|"+f"{i+1}".center(4,' ')+"|"+f"{products[i].capitalize()}".center(14,' ')+"|"+ f"${prices[i]:.2f}".center(9," ")+"|")
            print("+----+--------------+---------+")
        return_menu_modify=""
        while return_menu_modify != "menu":
            return_menu_modify = input("If you want return to menu, type 'MENU'.If you want continue, type any letter: ").lower()
            edit = int(input("Enter the ID of the product you want to modify: "))
            edit -= 1
            products[edit] = input("Enter the new product name: ").lower()
            new_price = input("Do you want modify the price?\nPlease type 'YES' or 'No': ")
            if new_price.lower() == "yes":
                prices[edit] = float(input("Enter the new product price: "))
                system("cls")
                title()
                print("Your new shopping cart is")
                view()
            elif new_price.lower() == "no":
                print("Your new shopping cart is")
                view()
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






'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 5 (Week 9 - Week 10)
For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.
'''

import time 
from time import sleep
from os import remove, system
import sys

#Variables for the list
products=[]
prices=[]

#Funtion for the tittle
def title():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Shopping Cart".center(150,'-'),"{}\n".format(t))


#Funtion for the program menu
def menu():
    title()
    print("1. Add product")
    print("2. Remove product")
    print("3. View cart")
    print("4. Compute Total")
    print("5. Modify")
    print("6. Exit")
    option = input("What would you like to do?: ")
    if option.lower() == "1":
        system('cls')
        title()
        add_product() #Call the funtion add_product
    elif option == "2":
        system('cls')
        title()
        remove_product_ID() #Call the funtion remove_product_ID
    elif option == "3":
        system('cls')
        title()
        view() #Call the funtion view
    elif option=="4":
        system('cls')
        title()
        compute_total() #Call the funtion compute_total
    elif option =="5":
        system('cls')
        title()
        modify() #Call the funtion modify
    elif option == "6":
        sure_quit_program() #Call the funtion modify
    else: 
        print("Please choose a correct option")
        sleep(3)
        system("cls")
        menu()

def add_product(): #Funtion for the add product
    return_add_product = input("If you want return to menu, type 'MENU' or press ENTER to continue...").lower() 
    if return_add_product!= "menu":
        system("cls")
        title()
        add_products = input("What product would you like to add?: ").lower()
        products.append(add_products) #add to list products
        add_price=""
        while True: #loop to validate that a correct price has been entered
            try: #We create the exceptions
                add_price = float(input("Add the price of the new product: "))
                prices.append(add_price)
                id_product = products.index(add_products)+1 #Operation to create the ID 
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
                break
            except ValueError: #If is ValueError 
                print("This is not a correct price, please enter a correct price")
                   
    else:   
        system("cls")
        menu()

def remove_product_ID(): #Funtion remove item in the list products and prices
    if len(products) == 0: #If the list is empty
        print("Your list is empty, add products")
        sleep(3)
        system("cls")
        menu()
    elif len(products) > 0: 
        print("+----+--------------+---------+")
        print("| ID |    PRODUCT   |  PRICE  |")
        print("+----+--------------+---------+")
        for i in range(len(products)): #Loop "for" each item in the length of the list products
            print("|"+f"{i+1}".center(4,' ')+"|"+f"{products[i].capitalize()}".center(14,' ') +"|"+ f"${prices[i]:.2f}".center(9," ")+"|")
            print("+----+--------------+---------+")
        return_remove = input("If you want return to menu, type 'MENU' or press ENTER to continue...").lower()
        if return_remove != "menu":
            remove_product = int(input("\nWhat product do you want to remove?\nPlease type the product's ID: "))
            remove_product -= 1 #Operation to remove the correct item in the list
            if remove_product < len(products): #Verify if the ID exist
                a = 0
                while a == 0:
                    sure = input("Are you sure?\nType 'YES' or 'NO': ")
                    if sure.lower() == "yes":
                        products.remove(products[remove_product])
                        prices.remove(prices[remove_product])
                        print("Item removed")
                        sleep(2)
                        system("cls")
                        menu()
                        a = 1
                    elif sure.lower() == "no":
                        system("cls")
                        title()
                        remove_product_ID()
                        a = 1
                    else:
                        print("Please type a correct option")
                        a = 0
            else:
                print("\nThe product ID I entered does not exist. Try again.")
                sleep(3)
                system("cls")
                title()
                remove_product_ID()  
        else:    
            system("cls")
            menu()

def view(): #Funtion to view the shopping cart
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
        input("\nPress ENTER to return to menu...")
        system("cls")
        menu()
            
def compute_total(): #Funtion to find the sum of all product's price
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
        sum_prices = sum(prices) #We use the funtion "sum" to find the sum of all product's price. Too can use a loop "for", example: for price in prices: sum_of_prices += price
        print("|"+"TOTAL PRICE".center(14,' ')+"|"+f"${sum_prices:.2f}".center(9,' ')+"|")
        print("+--------------+---------+")
        input("\nPress ENTER to return to menu...")
        system("cls")
        menu()
def modify(): #Funtion to modify some product or price
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
        return_menu_modify = input("If you want return to menu, type 'MENU' or press ENTER to continue...").lower()
        if return_menu_modify != "menu":
            edit = int(input("Enter the ID of the product you want to modify: "))
            edit -= 1
            if edit < len(products):
                print("\nWhat do you want to modify?\n1.Product Name\n2.Producto Price\n3.Product name and price")
                a = 0
                while a == 0:
                    choose=input("Choose one option: ")
                    if choose == "1":
                        products[edit] = input("Enter the new product name: ").lower()
                        system("cls")
                        title()
                        print("Your new shopping cart is")
                        a = 1
                        view()
                    elif choose == "2":
                        prices[edit] = float(input("Enter the new product price: "))
                        system("cls")
                        title()
                        print("Your new shopping cart is")
                        a = 1
                        view()
                    elif choose == "3":
                        products[edit] = input("Enter the new product name: ").lower()
                        prices[edit] = float(input("Enter the new product price: "))
                        system("cls")
                        title()
                        print("Your new shopping cart is")
                        a = 1
                        view()
                    else: 
                        print("This is a not correct option")
                        a = 0
            else:
                print("\nThe product ID I entered does not exist. Try again.")
                sleep(3)
                system("cls")
                title()
                modify()
        else:
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






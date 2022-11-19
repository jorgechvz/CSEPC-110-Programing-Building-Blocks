'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 6 (Week 11 - Week 12)
For this assignment you will write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.
'''
import time 
from time import sleep
from os import system
import sys

a = 0
while a == 0: #We create a loop for the menu
    #The variables that we using in the program.
    max_life = -1
    max_life_1 = -1
    year_max = ""
    year_max_1 = ""
    country_max = ""
    year_min = ""
    year_min_1 = ""
    min_life = 9999999999
    min_life_1 = 9999999999
    country_min = ""
    average = 0
    count = 0
    average_1 = 0
    count_1 = 0
    #Menu
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Life Expectancy".center(150,'-'),"{}\n".format(t))
    print("1. Life Expectancy Overall")
    print("2. Life Expectancy For year")
    print("3. Life Expectancy For country")
    print("4. Life Expectancy in a Range Years")
    print("5. Compare two countries")
    print("6. Exit program")
    option = input("Choose one option: ")
    if option == "2":
        choose_year = input("\nChoose a year(1882 - 2019): ")
    elif option == "3":
        choose_country = input("\nChoose a country: ")
    elif option == "4":
        print("\nHere we can see the maximum and minimum life expectancy in a certain range of years and in which country it occurred.")
        range_min_year = input("\nEnter the first year of the range you want(minor range): ")
        range_max_year = input("Enter the second year of the range you want(higher range): ")
    elif option == "5":
        choose_country_1 = input("\nChoose a first country: ").lower()
        choose_country_2 = input("Choose a second country: ").lower()
    elif option == "6":
        system('cls')
        print("\n"+"Thanks for using Life Expectancy. Come back soon!!!".center(150,' ')+"\n")
        a = 1
        sys.exit(5)
    #We open the file with the "with" funtion 
    with open("Files/life-expectancy.csv",'r+') as life_expectancy:
        next(life_expectancy) #We use "next" to skip the first line of the file
        for line in life_expectancy: #Loop for the lines in the file 
            clean_line = line.strip() #We clean white spaces
            parts = clean_line.split(",") #We divide the information
            country = parts[0].strip()
            code = parts[1].strip()
            year = parts[2].strip()
            life = float(parts[3])
            if option == "1": #for the option 1
                if life > max_life:
                    max_life = life
                    year_max = year
                    country_max = country
                if life < min_life:
                    min_life = life
                    year_min = year
                    country_min = country
            elif option == "2": #for the option 2
                if choose_year == year:
                    count += 1
                    average += life
                    avg = average / count
                    if life > max_life:
                        max_life = life
                        country_max = country
                    if life < min_life:
                        min_life = life
                        country_min = country
            elif option == "3": #for the option 3
                if choose_country.lower() == country.lower():
                    if life > max_life:
                        max_life = life
                        year_max = year
                    if life < min_life:
                        min_life = life
                        year_min = year
            elif option == "4": # for the option 4
                if range_min_year <= year <= range_max_year:
                    if life > max_life:
                        max_life = life
                        year_max = year
                        country_max = country
                    if life < min_life:
                        min_life = life
                        year_min = year
                        country_min = country
            elif option == "5": # for the option 5
                if choose_country_1.lower() == country.lower():
                    count += 1
                    average += life
                    avg = average / count
                    if life > max_life:
                        max_life = life
                        year_max = year
                    if life < min_life:
                        min_life = life
                        year_min = year
                if choose_country_2.lower() == country.lower():
                    count_1 += 1
                    average_1 += life
                    avg_1 = average_1 / count_1
                    if life > max_life_1:
                        max_life_1 = life
                        year_max_1 = year
                    if life < min_life_1:
                        min_life_1 = life
                        year_min_1 = year
    #Outputs
    if option == "1":
        print(f"\nThe overall max life expectancy is: {max_life} from {country_max} in {year_max}")
        print(f"The overall min life expectancy is: {min_life} from {country_min} in {year_min}")
        input("Press ENTER to return to menu...")
        system("cls")
        a = 0
    elif option == "2":
        print(f"\nFor the year {choose_year}:")
        print(f"The average life expectancy acroos all contries was {avg:.2f}") 
        print(f"The max life expectancy was in {country_max} with {max_life}")          
        print(f"The min life expectancy was in {country_min} with {min_life}")
        input("Press ENTER to return to menu...")
        system("cls")
        a = 0
    elif option == "3":
        print(f"\nFor the country {choose_country.capitalize()}:")
        print(f"The max life expectancy was in {year_max} with {max_life}")          
        print(f"The min life expectancy was in {year_min} with {min_life}")
        input("Press ENTER to return to menu...")
        system("cls")
        a = 0
    elif option == "4":
        print(f"\nThe overall max life expectancy is: {max_life} from {country_max} in {year_max}")
        print(f"The overall min life expectancy is: {min_life} from {country_min} in {year_min}")
        input("\nPress ENTER to return to menu...")
        system("cls")
        a = 0
    elif option == "5":
        print("+-----------+------------------+------------------+")
        print("|"+"COUNTRY".center(11," ")+"|"+f"{choose_country_1.capitalize()}".center(18," ")+"|"+f"{choose_country_2.capitalize()}".center(18," ")+"|")
        print("+-----------+------------------+------------------+")
        print("|"+"LIFE-MAX".center(11," ")+"|"+f"{max_life}".center(18," ")+"|"+f"{max_life_1}".center(18," ")+"|")
        print("+-----------+------------------+------------------+")
        print("|"+"LIFE-MIN".center(11," ")+"|"+f"{min_life}".center(18," ")+"|"+f"{min_life_1}".center(18," ")+"|")
        print("+-----------+------------------+------------------+")
        print("|"+"YEAR-MAX".center(11," ")+"|"+f"{year_max}".center(18," ")+"|"+f"{year_max_1}".center(18," ")+"|")
        print("+-----------+------------------+------------------+")
        print("|"+"YEAR-MIN".center(11," ")+"|"+f"{year_min}".center(18," ")+"|"+f"{year_min_1}".center(18," ")+"|")
        print("+-----------+------------------+------------------+")
        if max_life < max_life_1:
            btw_max = max_life_1 - max_life
            btw_min = min_life_1 - min_life
            print(f"\nThe diference of max life expectancy between {choose_country_1.capitalize()} and {choose_country_2.capitalize()} is: {btw_max:.2f}")
            print(f"\nThe diference of min life expectancy between {choose_country_1.capitalize()} and {choose_country_2.capitalize()} is: {btw_min:.2f}")
        elif max_life > max_life_1:
            btw_max = max_life - max_life_1
            btw_min = min_life - min_life_1
            print(f"\nThe diference of max life expectancy between {choose_country_1.capitalize()} and {choose_country_2.capitalize()} is: {btw_max:.2f}")
            print(f"\nThe diference of min life expectancy between {choose_country_1.capitalize()} and {choose_country_2.capitalize()} is: {btw_min:.2f}")
        input("Press ENTER to return to menu...")
        system("cls")
        a = 0
    
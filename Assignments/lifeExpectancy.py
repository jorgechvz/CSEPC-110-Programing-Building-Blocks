'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 6 (Week 11 - Week 12)
For this assignment you will write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.
'''
import time 
from time import sleep
from os import system
import sys
def title(): #Funtion for the title
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Life Expectancy".center(150,'-'),"{}\n".format(t))
def menu():
    title()
    print("1. Life Expectancy Overall")
    print("2. Life Expectancy For year")
    print("3. Life Expectancy For country")
    print("4. Range Life")
    choose = input("Choose one option: ")
    if choose == "1":
        system("cls")
        title()
        overall()
    elif choose == "2":
        system("cls")
        title()
        for_year()
    elif choose == "3":
        system("cls")
        title()
        for_country()
    elif choose == "4":
        system("cls")
        title()
        range_life()
    else:
        system("cls")
        title()
        menu()
def overall():
    max_life = -1
    year_max = ""
    country_max = ""
    year_min = ""
    min_life = 9999999999
    country_min = ""
    with open("Files/life-expectancy.csv",'r+') as life_expectancy:
        next(life_expectancy)
        for line in life_expectancy:
            clean_line = line.strip()
            parts = clean_line.split(",")
            country = parts[0].strip()
            code = parts[1].strip()
            year = parts[2].strip()
            life = float(parts[3])
            if life > max_life:
                max_life = life
                year_max = year
                country_max = country
            if life < min_life:
                min_life = life
                year_min = year
                country_min = country
    print(f"The overall max life expectancy is: {max_life} from {country_max} in {year_max}")
    print(f"The overall min life expectancy is: {min_life} from {country_min} in {year_min}")
    input("\nPress ENTER to return to menu...")
    system("cls")
    menu()

def for_year():
    max_life = -1
    country_max = ""
    min_life = 9999999999
    country_min = ""
    average = 0
    count = 0
    choose_year = input("\nChoose a year: ")
    with open("Files/life-expectancy.csv",'r+') as life_expectancy:
        next(life_expectancy)
        for line in life_expectancy:
            clean_line = line.strip()
            parts = clean_line.split(",")
            country = parts[0].strip()
            code = parts[1].strip()
            year = parts[2].strip()
            life = float(parts[3])
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
    print(f"\nFor the year {choose_year}:")
    print(f"The average life expectancy acroos all contries was {avg:.2f}") 
    print(f"The max life expectancy was in {country_max} with {max_life}")          
    print(f"The min life expectancy was in {country_min} with {min_life}") 
    input("\nPress ENTER to return to menu...")
    system("cls")
    menu()
def for_country():
    highest_country = -1
    lowest_country = 99999999999
    highest_country_year = ""    
    lowest_country_year = ""
    choose_country = input("Choose a country: ")
    with open("Files/life-expectancy.csv",'r+') as life_expectancy:
        next(life_expectancy)
        for line in life_expectancy:
            clean_line = line.strip()
            parts = clean_line.split(",")
            country = parts[0].strip()
            code = parts[1].strip()
            year = parts[2].strip()
            life = float(parts[3])
            if choose_country.lower() == country.lower():
                if life > highest_country:
                    highest_country = life
                    highest_country_year = year
                if life < lowest_country:
                    lowest_country = life
                    lowest_country_year = year
    print(f"\nFor the country {choose_country.capitalize()}:")
    print(f"The max life expectancy was in {highest_country_year} with {highest_country}")          
    print(f"The min life expectancy was in {lowest_country_year} with {lowest_country}")  
    input("\nPress ENTER to return to menu...")
    
    system("cls")
    menu()
def range_life():
    max_life = -1
    year_max = ""
    country_max = ""
    year_min = ""
    min_life = 9999999999
    country_min = ""
    range_min_year = input("Ingrese el rango menor de vida: ")
    range_max_year = input("Ingrese el rango mayor de vida: ")
    with open("Files/life-expectancy.csv",'r+') as life_expectancy:
        next(life_expectancy)
        for line in life_expectancy:
            clean_line = line.strip()
            parts = clean_line.split(",")
            country = parts[0].strip()
            code = parts[1].strip()
            year = parts[2].strip()
            life = float(parts[3])
            if range_min_year <= year <= range_max_year:
                if life > max_life:
                    max_life = life
                    year_max = year
                    country_max = country
                if life < min_life:
                    min_life = life
                    year_min = year
                    country_min = country
    print(f"The overall max life expectancy is: {max_life} from {country_max} in {year_max}")
    print(f"The overall min life expectancy is: {min_life} from {country_min} in {year_min}")
    input("\nPress ENTER to return to menu...")
    system("cls")
    menu()

menu()
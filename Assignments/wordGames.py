'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks - Assignment 2 
Implement a program that asks the user for a series of words and the displays the story with the user's words inserted into the appropiate places.
'''
#Libraries
import time #Library time
from os import system #Library for the clean window

#funtion for title of program
def title():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
    print("Word Games".center(100,'-'),"\t{}\n".format(t)) 
title() #Call the funtion title

#Variables
adjective = str(input("Please type your adjective: "))
animal = str(input("Please type your animal: "))
verb0 = str(input("Please type your first verb: "))
exclamation = str(input("Please type your exclamation: "))
verb1 = str(input("Please type your second verb: "))
verb2 = str(input("Please type your thrid verb: "))

#Output
system("cls") #clean the window 
title() #call the funtion title
print("¡¡¡your story is!!!".center(100,'*').upper())
time.sleep(1) #Time to wait for the result to execute

print('\nThe another day, I was really in trouble. It all started when I saw a very {0} {1} {2} down the hallway. \n"{3}"! I yelled, But all I could think to do was to {4} over and over. \nMiraculously, that caused it to stop, but not before it tried to {5} right in front of my family\n'.format(adjective,animal,verb0,exclamation.capitalize(),verb1,verb2))

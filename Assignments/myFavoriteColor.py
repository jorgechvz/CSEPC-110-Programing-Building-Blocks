'''
Chavez Ponce Jorge Alberto
CSE 110 Programming Building Blocks
Write a program that asks a user for their favorite color, then allow them to type in their color. Finally, have the program respond to them by displaying the text "Your favorite color is" followed by the color they typed.
'''
import time #Import the time library

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #Function to enter the time

print("What's your favorite color?".center(100,'-'),"\t{0}\n".format(t)) 

#Variables. We use str for a text string
name = str(input("Please type your name: "))
color = str(input("\nPleas type your favorite color: "))

#Output
print("\n")
print("Hey {0} your favorite color is {1}!!!".format(name,color).upper().center(70,'*'))

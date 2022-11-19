import sys
from os import system
def valalpha(a):
    v = 0;
    if str.isalpha(a)==True:
        v=1
    else:
        print("That is a not color")
    return v

def main():
    print("What's your favorite color?".center(80,'-'))
    while True:
        while True:
            name = str(input("\nPlease type your name: "))
            if valalpha(name)==1:
                break
        while True:
            color = str(input("Please type your color: "))
            if valalpha(color)==1:
                break
        print("\n\n{0} your favorite color is {1}\n\n".format(name,color))
        salir()    


def salir():
    a = 0
    while a == 0:
        x = input("Desea salir? \n a) Si. \n b) No.\n")
        if x.lower()=="si":
            seguro()
        elif x.lower()=="no":
            system("cls")
            main()
        else:
            a = 0
def seguro():
    a = 0
    while a == 0:
        x=input("¿Esta realmente seguro de que desea salir? \n a) Si. \n b) No. \n")
        if x.lower()=='si':
            print("Gracias por usar el programa")
            sys.exit(1)
        elif x.lower()=='no':
            system("cls")
            main()
            
        else:
            a = 0


main()

     

      

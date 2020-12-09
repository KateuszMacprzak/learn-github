import random
name=input("Enter your name: ")
print("Welcome in game %s"%name)
print ("You have to choose the number that probram choose from 1 to 3. Good luck !")
los=random.randint(1,3)
value=input('Wpisz swój typ liczby: ')
if(los==value):
    print("Gratulacje, udało Ci się wygrać !")
else:
    print ("Niestety, przegrałeś ! :(")
    print("It was %s"%los)
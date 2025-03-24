#Get user's name
name=str(input("Please enter your name "))

#The greeting
print("HI", name)
print("Welcome to the MASTERMIND GAME")
print("Can you defeat me and become a MASTERMIND???")

#print("Color Mapping")
#print("1-White 2-Blue 3-Red 4-Yellow 5-Green 6-Purple")

import random

#Generate four random numbers from 1 to 6
a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
d=random.randint(1,6)
#print(1000*a + 100*b + 10*c + d)

#Initialize variables for user inputs and the attempts
guess1=0
guess2=0
guess3=0
guess4=0
attempt=1

#Check whether the number of attempts exceed 8 and whether the guess is incorrect
while attempt<=8 or guess1 != a or guess2 != b or guess3 != c or guess4 != d:

    if (attempt==9):
        print("no more attempts left")
        print("You Lose")
        exit()
                
    print("attempt ",attempt)
    #Get user input
    guess1=int(input("What's your first guess= "))
    guess2=int(input("What's your second guess= "))
    guess3=int(input("What's your third guess= "))
    guess4=int(input("What's your fourth guess= "))
            
    #Stop when user input 0 for all the four guesses
    if guess1==0 and guess2==0 and guess3==0 and guess4==0:
        print("GAME OVER")
        break
            
    #Display the user's each guess
    print("Guess  - ", guess1 , guess2 , guess3 , guess4,end = '\n')

    #Check whether the user's guess is correct or not
    if(a==guess1):
        r1=1
    elif(b==guess1 or c==guess1 or d==guess1):
        r1=0
    else:
        r1="."

    if(b==guess2):
        r2=1
    elif(a==guess2 or c==guess2 or d==guess2):
        r2=0
    else:
        r2="."

    if(c==guess3):
        r3=1
    elif(a==guess3 or b==guess3 or d==guess3):
        r3=0
    else:
        r3="."

    if(d==guess4):
        r4=1
    elif(a==guess4 or b==guess4 or c==guess4):
        r4=0
    else:
        r4="."
    #Display whether the user's guess is correct or not
    print("Result - ",r1,r2,r3,r4,end = '\n')

    #After user guess 4 numbers the next attempt will begin
    attempt=attempt+1

    #When user guess all 4 correctly
    if(a==guess1 and b==guess2 and c==guess3 and d==guess4):
        print("Congratulations! You won on your attempt",attempt-1)
        print("You've become a MASTERMIND!")
        break


        #m_continue=''
        #str(input("Do You want to play another game (Yes/No)",m_continue))
        #if(m_continue==yes):
            #attempt=1
        #if(m_continue==no):
            #attempt=9
                

    
        


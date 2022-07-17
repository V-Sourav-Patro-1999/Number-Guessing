#UNIcompiler
#Task 1- Number Guessing
import random
N=random.randint(1,100)
print("Welcome to Number Guessing :-)")
print("Rules:- You have to Guess the correct number between 1 to 100.")
Guess=61
def guessthenumber(i):
    N=int(input("Guess a Number:- "))
    if(N==Guess):
        print("Congratulations!!")
        print(f"Your Guess is Correct and You have taken {i} attempts for the right answer.")
    elif(N>Guess):
        print("SORRY :(")
        print(f"Number is too High, You have taken {i} attempts.\n")  
        i=i+1
        guessthenumber(i)  
    else:
        print("SORRY :(")
        print(f"Number is too Low, You have taken {i} attempts.\n")
        i=i+1
        guessthenumber(i)    
i=1
guessthenumber(i)
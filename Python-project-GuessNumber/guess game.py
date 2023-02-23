import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess= int(input(f'guess a random number'))
        if guess < random_number:
            print("sorry guess is to low guess again")
        elif guess >random_number:
            print("guess is to high")
    print(f"jackpot you did it ")
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"is {guess} to high(H),too  low (L), or correct (C)??").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"yay! computer guesed the your number correctly,{guess}, correctly!")

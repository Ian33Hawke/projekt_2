#Michaela Hrušková
import random

number = []
attempts = 0

def MakeNumber():
    for i in range(4):
        x = random.randrange(0, 9)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        MakeNumber()

def PlayGame():
    global attempts
    bulls = 0
    cows = 0
    attempts += 1
    guess = []
    choice = input(">>> ")
    if len(choice) != 4:
        print("Your input must be 4 digits long!")
        PlayGame()
    elif choice[0] == "0":
        print("Your input must'nt begin with a 0!")
        PlayGame()
    elif len(choice) > len(set(choice)):
        print("Your input has duplicates!")
        PlayGame()
    else:
        try:
            val = int(choice)
        except ValueError:
            print("Your input must be numbers!")
            PlayGame()
    for i in range(4):
        guess.append(int(choice[i]))
        for j in range(4):
            if(guess[i] == number[j]):
                cows += 1
    for x in range(4):
        if guess[x] == number[x]:
            bulls += 1
    print(bulls," bulls")
    print(cows," cows")
    if(bulls == 4):
        print(choice)
        print("Correct, you've guessed the right number in ", attempts, "guesses!")
    if(bulls != 4):
        PlayGame()

if __name__ == "__main__":
    print("Play Bulls @ Cows")
    MakeNumber()
    print(number)
    PlayGame()
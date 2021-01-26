import random
from art import logo
print(logo)

num_generator = random.randint(1,100)
#print(num_genertor)
level = input("what level do you want, 'easy' or 'hard'? : ")
easy  = 10
hard  = 5
def user_chose():
    return guess

def decide_x(x, y): # x = guess , y = num_generator
    if x > y:
        return "too high"
    elif x < y:
        return "too low"
    else:
        return "You get number!"

def rest_live():
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        return "Wrong text"

n = rest_live()
print(f"You have {n} attemps remaining to guess!")
end_game = False
while not end_game:
    
    guess = int(input("Please enter number: "))
    a1 = decide_x(guess, num_generator)
    if a1 == "too high" or a1 == "too low":
        n = n-1
        if n == 0:
            end_game = True
            print("You lose!!!")
        else:
            print(a1)
            print(f"You have {n} attemps remaining to guess!")
    elif a1 == "You get number!" :
        end_game = True
        print("You win!!!")



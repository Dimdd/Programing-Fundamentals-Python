import random

computer_number = random.randint(1, 100)
guessing_counter=-1
is_guessed=True
guessing_number=int(input("How many time you would like to guess?:"))
my_number = int(input("Please guess a number between 1 and 100:"))


if my_number>100 or my_number<1:
    print("You are out of range. Please guess again:", end=" ")
    my_number=int(input())
elif my_number!=0:
    print("WTF??")
    my_number = int(input())

while my_number != computer_number:
    guessing_counter+=1
    if guessing_counter>guessing_number:
        print("Game Over!")
        print("f(You own me ${}")
        is_guessed=False
        break
    if my_number > computer_number:
        if my_number - computer_number > 50:
            print("Your number is much higher! Please guess again:", end=" ")
            my_number = int(input())
            continue
        else:
            print("Your number is higher! Please guess again:", end=" ")
            my_number = int(input())
            continue

    elif my_number < computer_number:
        if computer_number - my_number > 50:
            print("Your number is much lower! Please guess again:", end=" ")
            my_number = int(input())
            continue
        else:
            print("Your number is low! Please guess again:", end=" ")
            my_number = int(input())
            continue

if is_guessed:
    print("Congratulation!You won $10")
import random

computer_number = random.randint(1, 100)
is_guessed = False
number_of_guesses = 0
money_won = 0
money_lose = 0
guessing_number = input("How many time you would like to guess?(max 10):")


while not guessing_number.isdigit() or int(guessing_number)>10:
    print("WRONG Input!.Maximum 10 guesses.\nPlease enter again", end=" ")
    guessing_number = input("how many time you would like to guess?:")

guessing_number = int(guessing_number)
my_money = int(input("Please enter your money $"))
my_money_profit=my_money

my_number = input("Please guess a number between 1 and 100:")
if int(my_number)==computer_number:
    is_guessed=True
else:


    while not my_number.isdigit() or int(my_number) > 100 or int(my_number) < 1:
        number_of_guesses += 1
        print("WRONG Input!. Please guess again:", end=" ")
        if number_of_guesses == guessing_number:
            break
        my_number = input()

    for current_guess in range(1, guessing_number):

        if number_of_guesses >= guessing_number:
            break
        number_of_guesses += 1
        my_number = int(my_number)
        my_money_profit = (my_money / guessing_number) * 10 * 1.2

        if my_number > computer_number:

            if my_number - computer_number > 50:
                print("Your number is much higher!\nPlease guess again:", end=" ")
            else:
                print("Your number is higher!\nPlease guess again:", end=" ")

        elif my_number < computer_number:

            if computer_number - my_number > 50:
                print("Your number is much lower!\nPlease guess again:", end=" ")
            else:
                print("Your number is low!\nPlease guess again:", end=" ")
        else:
            print()
            print(f"Congratulation!You won ${my_money_profit}")
            is_guessed = True
            break
        my_number = input()
        while not my_number.isdigit() or int(my_number) > 100 or int(my_number) < 1:
            number_of_guesses += 1
            print("WRONG Input!. Please guess again:", end=" ")
            if number_of_guesses >= guessing_number:
                break
            my_number = input()

if not is_guessed:
    print("Game Over!")
    print(f"You LOST ${my_money}")
    print(f"Winning number is {computer_number}")
    print(my_money_profit)
elif is_guessed and guessing_number==1:

    print(f"Congratulation!You won ${my_money_profit*10}")
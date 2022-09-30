import random

player_move = input("Choose rock, paper,scissor:").lower()
if player_move != "rock" and player_move != "scissors" and player_move != "paper":
    print("Invalid input.Try again....")
    player_move = input("Choose rock,paper,scissor:").lower()

computer_move = random.randint(1, 3)

if computer_move == 1:
    computer_move = "rock"
elif computer_move == 2:
    computer_move = "paper"
elif computer_move == 3:
    computer_move = "scissors"
print(f"Computer move: {computer_move}")

if computer_move == "rock" and player_move == "scissors":
    print("You Lose!")
elif computer_move == "paper" and player_move == "rock":
    print("You Lose!")
elif computer_move == "scissors" and player_move == "paper":
    print("You Lose!")
elif computer_move == player_move:
    print("DRAW")
else:

    print("You Win!")

"""
ROCK PAPER SCISSOR
"""

import random

def play():
    i = 0
    score_user = 0
    score_computer = 0
    while i <= 3:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print('It\'s a tie\n')
            print(f"Computer score: {score_computer}")
            print(f"user score: {score_user}\n")

            # r > s, s > p, p > r
        if is_win(user, computer):
            score_user +=1
            print(f"Computer score: {score_computer}")
            print(f"user score: {score_user}\n")

        if is_win(computer, user):
            score_computer += 1
            print(f"Computer score: {score_computer}")
            print(f"user score: {score_user}\n")
        i += 1

    if score_computer > score_user:
        print('You lost\n')
    if score_user > score_computer:
        print('You won\n')

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

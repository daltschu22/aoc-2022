#!/usr/bin/env python
# Written by daltschu22 -- https://github.com/daltschu22

import sys

player_1_score = 0
player_2_score = 0

def r_p_s(player_1, player_2):
    if player_1 == 'rock' and player_2 == 'paper':
        return player_2
    elif player_1 == 'rock' and player_2 == 'scissors':
        return player_1
    elif player_1 == 'paper' and player_2 == 'rock':
        return player_1
    elif player_1 == 'paper' and player_2 == 'scissors':
        return player_2
    elif player_1 == 'scissors' and player_2 == 'rock':
        return player_2
    elif player_1 == 'scissors' and player_2 == 'paper':
        return player_1
    else:
        return None

def main():
    # Get the input file and read lines
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        data = f.readlines()

    ro_pa_sc = {
        'rock': ['A', 'X'],
        'paper': ['B', 'Y'],
        'scissors': ['C', 'Z']
    }

    player_1_score = 0
    player_2_score = 0

    for line in data:
        split_line = line.split()
        col_a = split_line[0]
        col_b = split_line[1]

        player_1 = ''
        player_2 = ''
        for key, value in ro_pa_sc.items():
            if col_a in value:
                player_1 = key
            if col_b in value:
                player_2 = key

        #PART 2 LOSE CONDITION
        if col_b == 'Y': #draw
            player_2 = player_1
        if col_b == 'X': #lose
            if player_1 == 'rock':
                player_2 = 'scissors'
            elif player_1 == 'paper':
                player_2 = 'rock'
            elif player_1 == 'scissors':
                player_2 = 'paper'
        if col_b == 'Z': #win
            if player_1 == 'rock':
                player_2 = 'paper'
            elif player_1 == 'paper':
                player_2 = 'scissors'
            elif player_1 == 'scissors':
                player_2 = 'rock'

        if player_1 == 'rock':
            player_1_score += 1
        elif player_1 == 'paper':
            player_1_score += 2
        elif player_1 == 'scissors':
            player_1_score += 3

        if player_2 == 'rock':
            player_2_score += 1
        elif player_2 == 'paper':
            player_2_score += 2
        elif player_2 == 'scissors':
            player_2_score += 3

        winner = r_p_s(player_1, player_2)

        if winner is None:
            player_1_score += 3
            player_2_score += 3
        if winner == player_1:
            player_1_score += 6
        elif winner == player_2:
            player_2_score += 6


    print(f'Player 1: {player_1_score}')
    print(f'Player 2: {player_2_score}')



if __name__ == '__main__':
    main()

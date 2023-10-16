'''
Created on Oct 9, 2023
@author: Benjamin Pierce
Program simulates a dice rolling game.
Player A gets 2 points if the die roll is 1 or 2.
Player B gets 1 point if the die roll is 3, 4, 5, or 6.
Player A rolls first, first player to 10 points wins.

Winner: Player A
'''
import random

#Function simulating single turn for Player A
def player_a_turn():
    roll = random.randint(1, 6)  #Roll 6-sided die
    if roll in (1, 2):
        return 2  #Player A scores 2 points for a roll of 1 or 2
    else: 
        return 0  #Player A scores 0 points for other rolls

#Function simulating single turn for Player B
def player_b_turn():
    roll = random.randint(1, 6)  #Roll 6-sided die
    if roll in (3, 4, 5, 6):
        return 1  #Player B scores 1 point for a roll of 3, 4, 5, or 6
    else: 
        return 0  #Player B scores 0 points for other rolls

#Function simulating the game for a given target score
def simulate_game(target_score):
    player_a_score = 0
    player_b_score = 0
    while player_a_score < target_score and player_b_score < target_score:
        player_a_score += player_a_turn()
        if player_a_score >= target_score:
            return "Player A wins"
        
        player_b_score += player_b_turn()
        if player_b_score >= target_score:
            return "Player B wins"

#Simulate the game for different target scores
target_scores = [10]  #Score of 10 wins the game
for target_score in target_scores:
    result = simulate_game(target_score)
    print(f"For a target score of {target_score}, {result}")
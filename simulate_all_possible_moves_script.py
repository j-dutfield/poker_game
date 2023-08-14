#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:43:47 2023

@author: jamesdutfield
"""

# This is a test of the functionality of the poker_game and poker_player classes

# Simulating all possible move sequences of flop street in 2, 3, and 8 players
# This includes all board states leading up to the final sequences

from poker_game import poker_game

print("Simulating all moves for flop round of three-player-game")
three_player_game = poker_game()
three_player_game.simulate_round()
print("Total possible sequences: " + str(three_player_game.move_count))
print("Simulation Finished")

print(" ")
print("#####################")
print(" ")

print("Simulating all moves for flop round of two-player-game")
two_player_game = poker_game(number_players=2)
two_player_game.simulate_round()
print("Total possible sequences: " + str(two_player_game.move_count))
print("Simulation Finished")

print(" ")
print("#####################")
print(" ")

print("Simulating all moves for flop round of eight-player-game")
eight_player_game = poker_game(number_players=8)
eight_player_game.simulate_round()
print("Total possible sequences: " + str(eight_player_game.move_count))
print("Simulation Finished")

print(" ")
print("#####################")
print(" ")

print("Summary Counts")
print("2-player total possible sequences: " + str(two_player_game.move_count))
print("3-player total possible sequences: " + str(three_player_game.move_count))
print("8-player total possible sequences: " + str(eight_player_game.move_count))

print(" ")
print("End of Script")
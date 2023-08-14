#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:41:54 2023

@author: james-dutfield
"""

import copy

class poker_game():
  """Poker_game object to simulate all possible moves of a round of poker under the following contraints:
  - Bet size is always equal to parameter bet_size (default = 10)
  - Raise is always equal to parameter raise_size (default = 10 chips over bet)
  - Fold can only be used in response to a bet or raise
  - Number or players is equal to parameter number_players.
  - Cannot currently incorporate pre-flop round or deal cards

  Works for 2-8 players (only checked/tested in-depth for 3 players).

  Future work:
  - Traverse through all rounds of a poker game including pre-flop
  - Incorporate card dealing
  - Make playable by humans
  - Make playable with bots
  """
  
  class poker_player():
    """Poker player object used to track the state of each player."""
    def __init__(self, bet_size, raise_size, in_game=True):
      self.in_game = in_game
      self.round_commitment = 0
      self.bet_size = bet_size
      self.raise_size = raise_size

    def make_move(self, move_type, state):
      if self.in_game:
        if move_type == "BET":
          self.round_commitment = self.bet_size
          state = "BET"
        elif move_type == "RAISE":
          self.round_commitment = self.bet_size + self.raise_size
          state = "RAISE"
        elif move_type == "FOLD":
          self.in_game = False
        elif move_type == "CALL":
          if state == "BET":
            self.round_commitment = self.bet_size
          elif state == "RAISE":
            self.round_commitment = self.bet_size + self.raise_size

      return state

  def __init__(self, number_players=3, current_pot_size=60, bet_size=10, raise_size=10):
    self.number_players = number_players
    self.current_pot_size = current_pot_size
    self.move_count=0

    self.player_1 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
    self.player_2 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
    table_order = [self.player_1, self.player_2]

    if number_players > 2:
      self.player_3 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
      table_order.append(self.player_3)
    if number_players > 3:
      self.player_4 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
      table_order.append(self.player_4)
    if number_players > 4:
      self.player_5 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
      table_order.append(self.player_5)
    if number_players > 5:
      self.player_6 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
      table_order.append(self.player_6)
    if number_players > 6:
      self.player_7 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
      table_order.append(self.player_7)
    if number_players > 7:
      self.player_8 = self.poker_player(bet_size = bet_size, raise_size=raise_size)
      table_order.append(self.player_8)

    self.table_order = table_order

  def simulate_round(self):

    def enact_all_options(board_state):
      # board_state=[[players], current_position, relative_position, state, history, round_active]
      board_states = []
      state = board_state[3]
      current_position = board_state[1]
      history = board_state[4]
      current_number_players = self.number_players - history.count("FOLD")

      turn_options = {"NO_BET": ["BET", "CHECK"],
                    "BET": ["CALL", "RAISE", "FOLD"],
                    "RAISE": ["CALL", "FOLD"]}

      if board_state[5] and current_number_players > 1: # if round_active and players>1
        if board_state[0][current_position].in_game:
          for option in turn_options[state]:
            board_state_temp = copy.deepcopy(board_state)
            temp_player = copy.deepcopy(board_state_temp[0][current_position])
            new_state = temp_player.make_move(option, state)
            board_state_temp[4] = history + [option]

            # update relative position
            if (state == "NO_BET" and new_state == "BET") or (state == "BET" and new_state == "RAISE"):
              board_state_temp[2] = 1
              board_state_temp[3] = new_state
            else:
              board_state_temp[2] += 1
              if board_state_temp[2] > current_number_players-1:
                board_state_temp[5] = False
            board_state_temp[0][current_position] = temp_player


            # update absolute board position
            board_state_temp[1] += 1
            if board_state_temp[1] > self.number_players-1:
              board_state_temp[1] = 0

            # add board state to list & print output
            pot_size = count_pot(self.current_pot_size, board_state_temp)
            self.move_count+=1
            print("-".join(board_state_temp[4]) + "=" + str(pot_size))
            board_states.append(board_state_temp)
      else:
        board_state[5] = False
        return []

      return board_states

    def count_pot(previous_pot_size, board_state):
      round_pot_size = sum([player.round_commitment for player in board_state[0]])
      return previous_pot_size + round_pot_size

    board_state = [self.table_order, 0, 0, "NO_BET", [], True] # [[players], current_position, relative_position, state, history, round_active]
    board_states = enact_all_options(board_state)
    loop_count = 0

    while board_states != []:

      new_layer_states = []
      for board in board_states:

        if board_state[5]:
          branch_states = enact_all_options(board)
          new_layer_states = new_layer_states + branch_states

      board_states = new_layer_states
      loop_count+=1
      if loop_count > 100:
        print("Infinite Loop Error")
        break
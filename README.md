**Poker Game** - by James Dutfield

My approach was to represent the poker game as a class with players, and to use this to search through all possible move sequences.

The simulation can run with 2-8 players, however I have only confirmed the results for the requested 3-player case.

The repo currently includes:
- poker_game.py: the poker_game class
- simulate_all_possible_moves_script.py: a test of the functionality of the poker_game and poker_player classes by simulating all possible move sequences of flop street with 2, 3, and 8 players

**This is a work in progress.**

Future work:
  - Traverse through all rounds of a poker game including pre-flop
  - Incorporate card dealing
  - Make playable by humans
  - Make playable vs rule-based bots
  - Advance bots using reinforcement learning

Requirements:
- Python 3.7.4
- No additional libraries used
## Description
### This refactored game of Pig is a game where 2 players roll a die and ends when a player reaches 100 points or the time ends.

## Game Instructions:
### To start the game use the following command: `python3 start.py --player1 computer --player2 human`.
### To start the game use the following command: `python3 start.py --player1 computer --player2 human --timed`. for a timed game that lasts a minute

## Players:
### The game needs two params:
### --player1 
### --player2 
### which accept the value of : "human" or "computer"

## Time:
## --timed parameter of 1 min.

## Game Play:
### A player will roll the die and continue to roll, accumulating tally points until they decide to hold or they roll a '1'. 
### If they hold the tally points will be added to their overall score. 
### If they roll a '1' the tally points are lost. 

## Keys:
### 'r' : roll
### 'h' : hold

## Tests:
### Run the tests using the following command: `python3 tests.py` .

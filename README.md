## Description
### This game is a refactored version [Here's the original](https://github.com/leov2000/IS211_Assignment7). This version includes the option to play with a timer of 1 min and also gives the option to play against a computer. The game ends when a player reaches 100 points or the time ends.

## Game Instructions:
### To start the game without a timer use the following: `python3 start.py --player1 computer --player2 human`.
### To start the game with a 1 min timer use the following: `python3 start.py --player1 computer --player2 human --timed`. 

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

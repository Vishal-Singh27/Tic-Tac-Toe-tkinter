# CS50p Final Project
# Introduction
This project is Tic-Tac-Toe game, I made the GUI using tkinter, and implemented the AI using Minimax algorithm.
I have also created executable files of it in mac-executable and window-executable.
Future updates on software on [Github Repo Link](https://github.com/Vishal-Singh27/Tic-Tac-Toe-tkinter/)

## Requirements
The only requirement is to have python install!
> If you dont have python installed, in windows install it by microsoft store and in mac install via Homebrew.

## Usage
Go to the mac-executable or windows-executable folder depending on your system and run the executable file "Tic-Tac-Toe".
Or by running runner.py

## Future release news
I will keep updating this game. I got several ideas in mind about integrating sql and keep game scores, plating human vs human and lot more updates to come. Also my main plan is to have alpha pruning in my minimax algorithm, also I might add depth first 

# Explanation of my code
## How files are Managed
Their are 3 main python codes in this directory:
#### boardlogic.py 
#### tkinterbuttonclass.py
#### boardlogic.py

## Lets look at each files one by one!
### boardlogic.py
This file has code and logic of minimax algorithm.
This file has the Board class which has all the classmethods that will help us in our code.
#### Lets look at the classmethods!
player classmethod:
> This classmethod needs an input of a board as an argument and it gives out which player's turn in the board.

player result:
> This classmethod returns a board when a given action is given on the board.

player actions:
> This classmethod returns set of all possible actions in a given board.

player nooxo:
> This classmethod returns no. of X and no. of O in a board. It's return value can be unpacked to 2 variables

player winner:
> This classmethod returns the winner(if any) in a given board.

player terminal:
> This classmethod checks if a game is finished or not.

initial_state:
> This classmethod returns an initial board with all blocks set to None.

utility:
> This classmethod returns 1 if X wins -1 if O wins 0 if game is tied.

minimax, findmin, findmax:
> This classmethod that carries out the main minimax algorithm part. Where findmin and findmax recurringly call each other till a board is at terminal state and then compare utility where X tries to get the maximum utility and O tries to get minimum utility.

### boardlogic.py
This file has code and logic of game button which we click to convert a button to X or O in our game.
This file has the Buttons class which has all the methods that will help us in our code
Lets look what the classmethods do:
Firstly lets see \_\_init\_\_
> In \_\_init\_\_ when a Buttons type is initialized it creates buttons on the screen, It can take arguments of like rowspan/columnspan/padx/pady/...etc. When those buttons are clicked a clicked method of our class is called

boardcondition:
> This method returns the board's in 2d list, based on all the button's configurations.

declare_winner:
> This method declares the winner of the board and is called after checking if the state is terminal state.

### runner.py
This file does all the tkinter's window operation and contains the start button whiich when clicked calls the start() function and that function creates a window asking if the user want to play as X or play as O

Depending on the user's choice, the buttons call either playasx or playaso which start's the game!

I hope you like this game!
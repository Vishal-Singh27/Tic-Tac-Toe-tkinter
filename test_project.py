from boardlogic import Board, X, O, EMPTY


# Testing termial classmethod.
def test_terminal():
    # Testing out boards
    board = [
        [X, O, X],
        [O, O, X],
        [X, X, O],
    ]
    # Checking the result
    assert Board.terminal(board)
    
    board = [
        [X, O, X],
        [O, O, X],
        [X, O, EMPTY],
    ]
    # Checking the result
    assert Board.terminal(board)
    
    board = [
        [X, O, X],
        [O, O, X],
        [X, EMPTY, EMPTY],
    ]
    # Checking the result
    assert Board.terminal(board) == False
  

# Testing utility classmethod.
def test_utility():
    # Testing out boards
    board = [
        [O, O, X],
        [O, X, X],
        [X, X, O],
    ]
    # Checking the result
    assert Board.utility(board) == 1
    
    board = [
        [X, O, X],
        [O, O, X],
        [X, O, EMPTY],
    ]
    # Checking the result
    assert Board.utility(board) == -1
    
    board = [
        [X, O, X],
        [O, O, X],
        [X, X, O],
    ]
    # Checking the result
    assert Board.utility(board) == 0
    
    
# Testing winner classmethod.
def test_winner():
    # Testing out boards
    board = [
        [O, O, X],
        [O, X, X],
        [X, X, O],
    ]
    # Checking the result
    assert Board.winner(board) == X
    
    board = [
        [X, O, X],
        [O, O, X],
        [X, O, EMPTY],
    ]
    # Checking the result
    assert Board.winner(board) == O
    
    board = [
        [X, O, X],
        [O, O, X],
        [X, X, O],
    ]
    # Checking the result
    assert Board.winner(board) == None
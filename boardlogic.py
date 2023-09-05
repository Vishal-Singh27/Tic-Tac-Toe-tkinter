# Importing necessary packages and libraries
import math
import copy

# Initializing some variables that are of use later
EMPTY = None
X = 'X'
O = 'O'


# Creating our class
class Board:
    # Initializing method
    def __init__(self, board):
        self.board = board
    
    # This classmethod gives 
    @classmethod
    def player(cls, board):
        xcount, ocount = cls.noofxo(board)
            
        if xcount > ocount:
            return "O"
        elif xcount == ocount:
            return "X"
        else:
            raise ValueError("Board is invalid")
    
    # Gives out resultant board if given an action
    @classmethod
    def result(cls, board, action):
        newboard = copy.deepcopy(board)
        newboard[action[0]][action[1]] = cls.player(board)
        return newboard
        
    # Gives out every set of actions possible in a board
    @classmethod
    def actions(cls, board):
        acts = set()
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    acts.add((row, col))
        return acts
        
    # Returns the no. of X and O in a board
    @classmethod
    def noofxo(cls, board=None):
        xcount = 0
        ocount = 0
        if not board:
            for row in cls.board:
                for cell in range(3):
                    if not row[cell]:
                        continue
                    if row[cell].lower() == 'x':
                        xcount += 1
                    elif row[cell].lower() == 'o':
                        ocount += 1
        else:
            for row in board:
                for cell in range(3):
                    if not row[cell]:
                        continue
                    if row[cell].lower() == 'x':
                        xcount += 1
                    elif row[cell].lower() == 'o':
                        ocount += 1
        return xcount, ocount
    
    # Checks and if there is a winner in game, then returns the winner(X or O)
    @staticmethod
    def winner(board):
        # Checking horizontally.
        for row in board:
            check = 0
            for col in row[1:]:
                if col == row[0]:
                    check += 1
            if check == 2:
                return row[0]
            
        # Checking Vertically.
        for col in range(3):
            check = 0
            for row in [1, 2]:
                if board[0][col] != EMPTY:
                    if board[row][col] == board[0][col]:
                        check += 1
            
            if check == 2:
                return board[0][col]
            
        # Checking diagonally.
        check = 0
        for i in [1, 2]:
            if board[i][i] == board[0][0] and board[0][0] != EMPTY:
                check += 1
            if check == 2:
                return board[0][0]
            
        check = 0
        col = 1
        for row in [1, 2]:
            if board[row][col] == board[0][2] and board[0][2] != EMPTY:
                check += 1
            col = 0
            if check == 2:
                return board[0][2]
        
        # Else return none.
        return None
    
    # Checks if the game is finished
    @classmethod
    def terminal(cls, board):
        if cls.winner(board):
            return True
        for row in board:
            if None in row:
                return False
        return True
    
    # If require, we can use this class method to initialize a new board
    @classmethod
    def initial_state():
        return Board([
            [None, None, None],
            [None, None, None], 
            [None, None, None]
        ])
    
    # Returns the utility of the board
    @classmethod
    def utility(cls, board):  
        if cls.terminal(board):
            winner = cls.winner(board)
        else:
            raise Exception("Utility is executed when it is not terminal state!")
        
        if winner == X:
            return 1
        elif winner == O:
            return -1
        else:
            return 0
          
    # When we print self.board what will come out
    def __str__(self):
        return str(self.board)
            
    # Classmethod that starts the minimax algorithm
    @classmethod
    def minimax(cls, board):
        act = None
        if cls.player(board) == X:
            ans = -math.inf
            for action in cls.actions(board):
                result = cls.findmin(cls.result(board, action))
                if result > ans:
                    ans = result
                    act = action
        
        elif cls.player(board) == O:
            ans = math.inf
            for action in cls.actions(board):
                tmp = min(math.inf, cls.findmax(cls.result(board, action)))
                if ans[0] > tmp:
                    ans[0] = tmp
                    ans[1] = action
                    
        return ans[1]
    
    # Classmethod that finds minimum utility of all actions at a board state
    @classmethod
    def findmin(cls, board):
        if cls.terminal(board):
            return cls.utility(board)
        
        ans = math.inf
        for action in cls.actions(board):
            tmp = min(math.inf, cls.findmax(cls.result(board, action)))
            if ans > tmp:
                ans = tmp
        return ans
                    
    # Classmethod that finds maximum utility of all actions at a board state
    @classmethod
    def findmax(cls, board):
        if cls.terminal(board):
            return cls.utility(board)
        
        ans = -math.inf
        for action in cls.actions(board):
            tmp = max(-math.inf, cls.findmin(cls.result(board, action)))
            if ans < tmp:
                ans = tmp
        return ans
    
    def __str__(self):
        return self.board
    

def main():
    # Some Tests
    
    # Testboard1
    print("Testboard1: ")
    test_board1 = [
        ['X', None, 'None'],
        [None, 'O', O],
        [O, 'X', 'X']
    ]

    print(Board.minimax(test_board1))

    # Testboard2
    print("Testboard2: ")
    test_board2 = [
        ['X', 'O', None],
        [None, 'O', None],
        ['O', 'X', X]
    ]
    print(Board.minimax(test_board2))

    # Testboard3
    print("Testboard3: ")
    test_board3 = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    print(Board.winner(test_board3))
    print(Board.minimax(test_board3))

    # Testboard4
    print("Testboard4: ")
    test_board4 = [
        ['X', 'O', X],
        ['O', 'X', None],
        [O, None, None]
    ]
    print(Board.minimax(test_board4))

    # Testboard5
    print("Testboard5: ")
    test_board5 = [
        [None, 'O', 'X'],
        [None, 'O', 'X'],
        [X, 'X', 'O']
    ]
    print(Board.minimax(test_board5))
    
    # Testboard 6
    print("test_board 6")
    test_board6 = [
        [None, 'O', 'X'],
        [None, None, 'X'],
        [None, None, None]
    ]
    print(Board.minimax(test_board6))
    
    
# Making sure that only call main when program is ran by terminal
if __name__ == "__main__":
    main()
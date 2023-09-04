import math
import copy

# Initializing some variables that are of use later
EMPTY = None
X = 'X'
O = 'O'

# Creating our class
class Board:
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
    
    @classmethod
    def result(cls, board, action):
        newboard = copy.deepcopy(board)
        newboard[action[0]][action[1]] = cls.player(board)
        return newboard
        
    @staticmethod
    def actions(board):
        acts = set()
        for row in range(3):
            for cell in range(3):
                if board[row][cell] == EMPTY:
                    acts.add((row, cell))
        return acts
        
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
                if board[row][col] == board[0][col]:
                    check += 1
            
            if check == 2:
                return board[0][col]
            
        # Checking diagonally.
        check = 0
        for i in [1, 2]:
            if board[i][i] == board[0][0]:
                check += 1
            if check == 2:
                return board[0][0]
            
        check = 0
        col = 1
        for row in [1, 2]:
            if board[row][col] == board[0][2]:
                check += 1
            col = 0
            if check == 2:
                return board[0][2]
        
        # Else return none.
        return None
    
    @classmethod
    def terminal(cls, board):
        check = 0
        if cls.winner(board):
            return True
        for row in board:
            if None in row:
                return False
        return True
        
    @classmethod
    def initial_state():
        return Board([
            [None, None, None],
            [None, None, None], 
            [None, None, None]
        ])
        
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
          
    def __str__(self):
        return str(self.board)
            
    @classmethod
    def minimax(cls, board):
        if cls.terminal(board):
            return None
        
        if cls.player(board) == X:
            ans = [-math.inf, None]
            for action in cls.actions(board):
                tmp = max(-math.inf, cls.findmin(cls.result(board, action)))
                if ans[0] < tmp:
                    ans[0] = tmp
                    ans[1] = action
                    
        elif cls.player(board) == O:
            ans = [math.inf, None]
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
    
        ans = [-math.inf, None]
        for action in cls.actions(board):
            tmp = max(-math.inf, cls.findmin(cls.result(board, action)))
            if ans < tmp:
                ans = tmp
        return ans
    

def main():
    print("Testboard1: ")
    test_board1 = [
        ['X', None, 'None'],
        [None, 'O', O],
        [O, 'X', 'X']
    ]
    # Player: 'O' (since X count: 3, O count: 3)
    # Best Move: (1, 0)
    # Expected Output: (1, 0)
    print(Board.minimax(test_board1))

    print("Testboard2: ")
    test_board2 = [
        ['X', 'O', None],
        [None, 'O', None],
        ['O', 'X', X]
    ]
    # Player: 'X' (since X count: 3, O count: 3)
    # Best Move: (2, 2)
    # Expected Output: (2, 2)
    print(Board.minimax(test_board2))

    print("Testboard3: ")
    test_board3 = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]
    # Player: 'X' (since X count: 5, O count: 4)
    # Best Move: (1, 1)
    # Expected Output: (1, 1)
    print(Board.minimax(test_board3))

    print("Testboard4: ")
    test_board4 = [
        ['X', 'O', X],
        ['O', 'X', None],
        [O, None, None]
    ]
    # Player: 'X' (since X count: 2, O count: 2)
    # Best Move: (2, 0)
    # Expected Output: (2, 0)
    print(Board.minimax(test_board4))

    print("Testboard5: ")
    test_board5 = [
        [None, 'O', 'X'],
        [None, 'O', 'X'],
        [X, 'X', 'O']
    ]
    # Player: 'X' (since X count: 6, O count: 3)
    # Best Move: (0, 2)
    # Expected Output: (0, 2)
    print(Board.minimax(test_board5))
    

if __name__ == "__main__":
    main()

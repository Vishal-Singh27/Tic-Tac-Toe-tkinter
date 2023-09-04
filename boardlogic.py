import math
import copy

EMPTY = None
X = 'X'
O = 'O'

class Board():
    def __init__(self, board):
        self.board = board
        
    @classmethod
    def player(self, board):
        
        xcount, ocount = self.noofxo(board)
            
        if xcount > ocount:
            return "O"
        elif xcount == ocount:
            return "X"
        else:
            raise ValueError("Board is invalid")
    
    @classmethod
    def result(self, board, action):
        newboard = copy.deepcopy(board)
        newboard[action[0]][action[1]] = self.player(board)
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
    def noofxo(self, board=None):
        xcount = 0
        ocount = 0
        if not board:
            for row in self.board:
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
    def terminal(self, board):
        check = 0
        if self.winner(board):
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
    def utility(self, board):  
        if self.terminal(board):
            winner = self.winner(board)
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
    def minimax(self, board):
        if self.terminal(board):
            return None
        
        if self.player(board) == X:
            ans = [-math.inf, None]
            for action in self.actions(board):
                tmp = max(-math.inf, self.findmin(self.result(board, action)))
                if ans[0] < tmp:
                    ans[0] = tmp
                    ans[1] = action
                    
        elif self.player(board) == O:
            ans = [math.inf, None]
            for action in self.actions(board):
                tmp = min(math.inf, self.findmax(self.result(board, action)))
                if ans[0] > tmp:
                    ans[0] = tmp
                    ans[1] = action
                    
        return ans[1]
        
    @classmethod
    def findmin(self, board):
        if self.terminal(board):
            return self.utility(board)
        
        ans = math.inf
        for action in self.actions(board):
                tmp = min(math.inf, self.findmin(self.result(board, action)))
                if tmp > ans:
                    return ans
                if ans > tmp:
                    ans = tmp
                    
        return ans
            
    
    @classmethod
    def findmax(self, board, maxi=None):
        if self.terminal(board):
            return self.utility(board)
    
        ans = -math.inf
        for action in self.actions(board):
                tmp = max(-math.inf, self.findmin(self.result(board, action)), maxi=ans)
                if tmp < ans:
                    return ans
                if ans < tmp:
                    ans = tmp
        return ans

test_board1 = [
    ['X', None, 'None'],
    [None, 'O', O],
    [O, 'X', 'X']
]
# Player: 'O' (since X count: 3, O count: 3)
# Best Move: (1, 0)
# Expected Output: (1, 0)
print(Board.minimax(test_board1))

test_board2 = [
    ['X', 'O', 'X'],
    [None, 'O', None],
    ['O', 'X', None]
]
# Player: 'X' (since X count: 3, O count: 3)
# Best Move: (2, 2)
# Expected Output: (2, 2)

print(Board.minimax(test_board2))

test_board3 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]
# Player: 'X' (since X count: 5, O count: 4)
# Best Move: (1, 1)
# Expected Output: (1, 1)
print(Board.minimax(test_board3))

test_board4 = [
    ['X', 'O', None],
    ['O', 'X', None],
    [None, None, None]
]
# Player: 'X' (since X count: 2, O count: 2)
# Best Move: (2, 0)
# Expected Output: (2, 0)
print(Board.minimax(test_board4))

test_board5 = [
    ['None', 'O', 'X'],
    [None, 'O', 'X'],
    [X, 'X', 'O']
]
# Player: 'X' (since X count: 6, O count: 3)
# Best Move: (0, 2)
# Expected Output: (0, 2)


print(Board.minimax(test_board5))
# Importing libraries and packages
from boardlogic import Board
from tkinter import Tk, Button
from tkinter import messagebox

# Initializing some global variables
X = 'X'
O = 'O'
EMPTY = None


# Making a class containg all buttons and functionality.
class Buttons():
    # Initializing the buttons
    def __init__(self, window, startrow=0, rowspan=1, columnspan=1, startcolumn=0, padx=5, pady=5, player=X):
        self.buttons = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.player = player
        self.startrow = startrow
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.startcolumn = startcolumn
        self.padx = padx
        self.pady = pady
        self.window = window
        gridrow = startrow
        for row in range(3):
            gridcol = startcolumn
            for col in range(3):         
                self.buttons[row][col] = Button(
                    window, text="-", 
                    command=lambda r=row, c=col: self.clicked(row=r, col=c, window=window),
                    padx=padx, pady=pady
                )
                self.buttons[row][col].grid(row=gridrow, column=gridcol, columnspan=columnspan, rowspan=rowspan)
                gridcol += columnspan
            gridrow += rowspan
            
        if player == O:
            newrow, newcol = Board.minimax(self.boardcondition())
            self.buttons[newrow][newcol].configure(text=X, state="disabled")
            self.buttons[newrow][newcol].configure(bg='white')  
            
    # If button is clicked
    def clicked(self, window, row, col):
        self.buttons[row][col].configure(text=Board.player(self.boardcondition()), state="disabled", bg='white')
        window.update()
        if Board.terminal(self.boardcondition()):
            self.declare_winner(window)
        else:
            nextrow, nextcol = Board.minimax(self.boardcondition())
            self.buttons[nextrow][nextcol].configure(text=Board.player(self.boardcondition()), state="disabled")
            self.buttons[nextrow][nextcol].configure(bg='white')
            if Board.terminal(self.boardcondition()):
                self.declare_winner(window)
    
    # To get current board state in a 2d list
    def boardcondition(self):
        board = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col].cget("text") == X:
                    board[row][col] = X
                elif self.buttons[row][col].cget("text") == O:
                    board[row][col] = O
        return board
    
    # If the self is printed out
    def __str__(self):
        return self.boardcondition()
    
    # To decare the winner in the messagebox
    def declare_winner(self, window):
        window.update()
        winner = Board.winner(self.boardcondition())
        if self.player == winner:
            response = messagebox.askyesno("You Won!!", "Congratulations! You Won!, Wanna play again?")
            if response == 0:
                window.destroy()
            else:
                self = Buttons(self.window, self.startrow, self.rowspan, self.columnspan,
                               self.startcolumn, self.padx, self.pady, self.player)
                
        elif winner == None:
            response = messagebox.askyesno("Tied!", "Game tied, wanna try again?")
            if response == 0:
                window.destroy()
            else:
                self = Buttons(
                    self.window, self.startrow, self.rowspan, self.columnspan, 
                    self.startcolumn, self.padx, self.pady, self.player
                )
        else:
            response = messagebox.askyesno("You Lose!", "You lost!, wanna try again?")
            if response == 0:
                window.destroy()
            else:
                self = Buttons(self.window, self.startrow, self.rowspan, self.columnspan,
                               self.startcolumn, self.padx, self.pady, self.player)
            

# Main function if we wanna check if program is working
def main():
    # Starting root window
    root = Tk()
    
    # Making the buttons using our class
    Buttons(root, player=X, rowspan=3, columnspan=3, padx=20, pady=20)
    
    # To start main event loop
    root.mainloop()
    
    
# If program is executed through terminal then call main() 
if __name__ == "__main__":
    main()
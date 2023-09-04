from tkinter import *
from boardlogic import Board


OFF = False
ON = True 
EMPTY = None
X = "X"
O = "O"


# Starting our root window
root = Tk()


buttons = [[EMPTY] * 3] * 3


def initial_buttons():
    global buttons
    global root
    global startbutton
    startbutton.configure(text='Start', bg='black', state='disabled')
    for row, gridrow in zip(range(3), [1, 2, 3]):
        for col, gridcol in zip(range(3), [0, 2, 4]):
            buttons[row][col] = Button(root ,text="-", padx=10, pady=10, command=lambda: click(buttons[row][col]))
            buttons[row][col].grid(row=gridrow, column=gridcol, columnspan=2)


def click(button):
    boardcondition = get_boardstate()
    button.configure(text=Board.player(boardcondition), state="disabled")
    
    
def set_boardstate(buttons):
    board = [list()]
    
    for row in range(3):
        for col in range(3):
            if buttons[i][f].cget("text") == X:
                buttons[i][f].configure(text=X, state="Disabled")
            elif buttons[i][f].cget("text") == O:
                buttons[i][f].configure(text=O, state="Disabled")

def get_boardstate():
    global buttons
    board = [list()] * 3
    for row in range(3):
        for col in range(3):
            if buttons[row][col].cget("text") == X:
                board[row].append(X)
            elif buttons[row][col].cget("text") == O:
                board[row].append(O)
            else:
                board[row].append(EMPTY)
    return board
            
                
    
startbutton = Button(text="Start", command=initial_buttons, padx=10, pady=10)
startbutton.grid(row=0, column=3)

# Making the root loop till the program is closed
root.mainloop()
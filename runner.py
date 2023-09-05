# Importing necessary libraries
from tkinter import Tk, Button, Toplevel, Label
from tkinterbuttonclass import Buttons, O

# Starting our root window
root = Tk()
root.title("Tic-Tac-Toe by Vishal Singh")

# Label at top
label = Label(root, text="Tic Tac Toe by Vishal Singh")
label.grid(row=0, column=3)

def start():    
    newwindow = Toplevel()
    Button(newwindow, text="Play as X", command=lambda: playasx(newwindow)).pack()
    Button(newwindow, text="Play as O", command=lambda: playaso(newwindow)).pack()
    

# If user chooses to play as X
def playasx(window):
    global label
    window.destroy()
    startbutton.destroy()
    label.destroy()
    Buttons(root, padx=50, pady=50, columnspan=2)


# If user chooses to play as O
def playaso(window):
    global label
    window.destroy()
    startbutton.destroy()
    label.destroy()
    Buttons(root, player=O, padx=50, pady=50, columnspan=2)


# A button to start the game
startbutton = Button(text="Start", command=start, padx=10, pady=10)
startbutton.grid(row=1, column=3)

# Starting the main event loop
root.mainloop()
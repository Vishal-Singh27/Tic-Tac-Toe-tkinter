# Importing necessary libraries
from tkinter import Tk, Button, Toplevel
from tkinterbuttonclass import Buttons, EMPTY, X, O

# Starting our root window
root = Tk()

def start():    
    newwindow = Toplevel()
    Button(newwindow, text="Play as X", command=lambda: playasx(newwindow)).pack()
    Button(newwindow, text="Play as O", command=lambda: playaso(newwindow)).pack()
    

# If user chooses to play as X
def playasx(window):
    window.destroy()
    startbutton.destroy()
    Buttons(root, padx=40, pady=40, columnspan=2)


# If user chooses to play as O
def playaso(window):
    window.destroy()
    startbutton.destroy()
    Buttons(root, player=O, padx=20, pady=20, columnspan=2)


startbutton = Button(text="Start", command=start, padx=10, pady=10)
startbutton.grid(row=0, column=3)

# Making the root loop till the program is closed
root.mainloop()
# Importing necessary libraries
from tkinter import Tk, Button, Toplevel, Label
from tkinterbuttonclass import Buttonsforai, O

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
    aibutton.destroy()
    label.destroy()
    Buttonsforai(root, padx=50, pady=50, columnspan=2)


# If user chooses to play as O
def playaso(window):
    global label
    window.destroy()
    aibutton.destroy()
    label.destroy()
    Buttonsforai(root, player=O, padx=50, pady=50, columnspan=2)


# Button to start the game vs AI
aibutton = Button(text="PlaywithAI", command=start, padx=10, pady=10)
aibutton.grid(row=1, column=3)

# Button to start the game vs human
humanbutton = Button(text="PlaywithAI", command=start, padx=10, pady=10)
humanbutton.grid(row=1, column=3)

# Starting the main event loop
root.mainloop()
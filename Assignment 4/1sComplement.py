from automata.tm.dtm import DTM
import tkinter as tk
from tkinter import *

dtm = DTM(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        'q0':{
            '1': ('q1', '0', 'R'),
            '0': ('q1', '1', 'R')
        },
        'q1':{
            '1': ('q1', '0', 'R'),
            '0': ('q1', '1', 'R'),
            'B': ('q2', 'B', 'L')
        }
    },
    initial_state='q0',
    blank_symbol='B',
    final_states={'q2'}
)


# gui code

# function for submit button
def submit():
    userStr = userEntry.get()
    outputMsg.config(text="")  # set result output text to be blank
    if dtm.accepts_input(userStr):
        outputMsg.config(text=dtm.read_input(userStr))
        outputMsg.place(x=150, y=200, anchor='center')
    else:
        outputMsg.config(text="Input Rejected. Please try again")
        outputMsg.place(x=150, y=200, anchor='center')


# function for delete button to clear the input field
def delete():
    userEntry.delete(0, tk.END)
    outputMsg.config(text="")


# function to exit the program
def exit():
    window.destroy()


# creating the gui window
window = tk.Tk()
window.geometry("300x300")
window.title("Part 3 - 1s Complement")

# creating prompt
prompt = tk.Label(text="Enter your string: ")
prompt.place(x=150, y=10, anchor='center')

# creating input field
userEntry = tk.Entry()
userEntry.place(x=150, y=35, anchor='center')

# creating output message
outputMsg = Label(master=window)

# creating buttons
submit = Button(master=window, text="Submit", command=submit)
submit.place(x=150, y=80, anchor='center')

delete = Button(master=window, text="Delete", command=delete)
delete.place(x=150, y=120, anchor='center')

exitBtn = Button(master=window, text="Exit GUI", command=exit)
exitBtn.place(x=150, y=150, anchor='center')

window.mainloop()
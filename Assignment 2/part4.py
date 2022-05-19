#Roman Melnik - 2693934
#CIS 490 Professor Essa
#Assignment 2 - Part 3

from automata.fa.dfa import DFA
import tkinter as tk
from tkinter import *

#student id is 2693934
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3','q4', 'q5', 'q6', 'q7', 'q8'},
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    transitions={
        'q0': {'0': 'q8', '1': 'q8', '2': 'q1', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q1': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q2', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q2': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q3'},
        'q3': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q4', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q4': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q5'},
        'q5': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q6', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q6': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q7', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q7': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q8': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'}
    },
    initial_state='q0',
    final_states={'q7'}

)

#gui code

#function for submit button
def submit():
    userID = userEntry.get()
    outputMsg.config(text="") #set result output text to be blank
    if dfa.accepts_input(userID):
        outputMsg.config(text="ID Accepted")
        outputMsg.place(x=150, y=200, anchor='center')
    else:
        outputMsg.config(text="ID Rejected. Please try again")
        outputMsg.place(x=150, y=200, anchor='center')


#function for delete button to clear the input field
def delete():
    userEntry.delete(0, tk.END)
    outputMsg.config(text="")


#function to exit the program
def exit():
    window.destroy()


#creating the gui window
window = tk.Tk()
window.geometry("300x300")
window.title("Part 4")

#creating prompt 
prompt = tk.Label(text="Enter 7-digit CSU ID: ")
prompt.place(x=150, y=10, anchor='center')

#creating input field
userEntry = tk.Entry()
userEntry.place(x=150, y=35, anchor='center')

#creating output message
outputMsg = Label(master=window)

#creating buttons
submit = Button(master=window, text="Submit", command=submit)
submit.place(x=150, y=80, anchor='center')

delete = Button(master=window, text="Delete", command=delete)
delete.place(x=150, y=120, anchor='center')

exitBtn = Button(master=window, text="Exit GUI", command=exit)
exitBtn.place(x=150, y=150, anchor='center')

window.mainloop()


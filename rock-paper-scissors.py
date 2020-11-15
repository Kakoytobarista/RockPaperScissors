import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random
import time
from tkinter import messagebox
from random import randint

pc_score = 0
user_score = 0
pc_figure = ""
user_figure = ""


def rock():
    global user_figure
    Kbut['bg'] = 'green'
    Nbut["bg"] = 'white'
    Bbut['bg'] = 'white'
    user_figure = "rock"
    PCbut['state'] = 'normal'


def paper():
    global user_figure
    Kbut['bg'] = 'white'
    Nbut["bg"] = 'white'
    Bbut['bg'] = 'green'
    user_figure = "paper"
    PCbut['state'] = 'normal'


def scissors():
    global user_figure
    Kbut['bg'] = 'white'
    Nbut["bg"] = 'green'
    Bbut['bg'] = 'white'
    user_figure = "scissors"
    PCbut['state'] = 'normal'


def go():
    global pc_figure, user_figure, user_score, pc_score
    t4['text'] = 'PC chooses - '
    for i in range(30):
        ran = randint(1, 4)
        if ran == 1:
            pc_figure = "rock"
        if ran == 2:
            pc_figure = "paper"
        if ran == 3:
            pc_figure = "scissors"

        t4['text'] = 'PC chooses -' + pc_figure
        t4.update()
        time.sleep(0.1)

    if pc_figure == user_figure:
        messagebox.showinfo('result', 'Drow')
    else:
        if pc_figure == 'rock' and user_figure == 'scissors':
            pc_score += 1
            messagebox.showinfo('result', "PC Win")
        if pc_figure == 'rock' and user_figure == 'paper':
            user_score += 1
            messagebox.showinfo('result', 'leather bastards won')
        if pc_figure == 'scissors' and user_figure == 'paper':
            pc_score += 1
            messagebox.showinfo('result', 'PC Win')
        if pc_figure == 'scissors' and user_figure == 'rock':
            user_score += 1
            messagebox.showinfo('result', 'leather bastards won')
        if pc_figure == 'paper' and user_figure == 'rock':
            pc_score += 1
            messagebox.showinfo('result', 'PC Win')
        if pc_figure == 'paper' and user_figure == 'scissors':
            user_score += 1
            messagebox.showinfo('result', 'leather bastards won')

        t5['text'] = 'Player - ' + str(user_score)
        t6['text'] = 'PC - ' + str(pc_score)

    PCbut['state'] = 'disabled'


win = Tk()
win.title('Rock, Paper, Scissors')
win.geometry(f'390x655+450+200')
win.resizable(False, False)
win['bg'] = '#544435'
t1 = Label(win, text='Rock, Paper, Scissors', fg='#d49949', pady=10, bg='#544435', font=('Gasrux', 12, 'bold'), relief='groove')
t1.grid(row=0, column=1)
t2 = Label(win, text='player chooses:', fg='green', bg='#544435', pady=10, font='Roboto')
t2.grid(row=1, column=1)

Kbut = Button(win, text='Rock', command=rock, highlightbackground='green')
Kbut.grid(row=2, column=0)
Nbut = Button(win, text='Scissors', command=scissors, highlightbackground='green')
Nbut.grid(row=2, column=1, pady=8)
Bbut = Button(win, text='Paper', command=paper, highlightbackground='green')
Bbut.grid(row=2, column=2)

# t3 = Label(win, text='PC chooses - 0', fg='blue', bg='#c0c0c0')
# t3.grid(row=3, column=1)
PCbut = Button(win, text="Generate", command=go, highlightbackground='red', borderwidth=10, activebackground='red')
PCbut['state'] = 'disabled'
PCbut.grid(row=4, column=1)

t4 = Label(win, text='the computer chose: ', fg='#df3928', bg='#544435', pady=15, font='Roboto')
t4.grid(row=6, column=1)

t5 = Label(win, text='Player - 0', fg='green', relief=tk.RAISED, font=('Arial', 11, 'bold'))
t5.grid(row=7, column=0, padx=10)

t6 = Label(win, text='PC - 0', fg='red', relief=tk.RAISED, font=('Arial', 11, 'bold'))
t6.grid(row=7, column=2, padx=30)

im = PhotoImage(file='paper01.png')
l = Label(win, image=im)
l.grid(row=15, column=1, pady=30)

regulations = "Options: The players take turns putting 3x3 signs on the empty cells of the field \
                The first player to line up his 3 pieces vertically, horizontally or diagonally wins. The first move \
               is made by the player placing crosses."
performance_words2 = tk.Label(win, text=regulations,
                              font="Oswald 10", bg='#4e443b',
                              fg='#daaf62', anchor='s',
                              wraplength=190, takefocus=100, relief='sunken', borderwidth=10
                              )
performance_words2.grid(row=19, column=1)

win.mainloop()

from tkinter import *
import random

player = set()
computer = set()
button = []
c = {0, 1, 2, 3, 4, 5, 6, 7, 8} #заменить!
def buttons():
    root = Tk()
    screen_height = root.winfo_screenheight()
    a = screen_height/8
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[0].grid(row = 0, column = 0, sticky = "snew", ipadx = a, ipady = a)
    button[0].config(command = lambda: click(1))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[1].grid(row = 0, column = 1, sticky = "snew", ipadx = a, ipady = a)
    button[1].config(command = lambda: click(2))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[2].grid(row = 0, column = 2, sticky = "snew", ipadx = a, ipady = a)
    button[2].config(command = lambda: click(3))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[3].grid(row = 1, column = 0, sticky = "snew", ipadx = a, ipady = a)
    button[3].config(command = lambda: click(4))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[4].grid(row = 1, column = 1, sticky = "snew", ipadx = a, ipady = a)
    button[4].config(command = lambda: click(5))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[5].grid(row = 1, column = 2, sticky = "snew", ipadx = a, ipady = a)
    button[5].config(command = lambda: click(6))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[6].grid(row = 2, column = 0, sticky = "snew", ipadx = a, ipady = a)
    button[6].config(command = lambda: click(7))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[7].grid(row = 2, column = 1, sticky = "snew", ipadx = a, ipady = a)
    button[7].config(command = lambda: click(8))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = '#FFFF00'))
    button[8].grid(row = 2, column = 2, sticky = "snew", ipadx = a, ipady = a)
    button[8].config(command = lambda: click(9))

def click(number): #номер клетки
    global player
    global computer
    
    process(number)
    player.add(number-1)
    art_intellect(number)
        
def process(number):
    if number == 1:
        button[0].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 2:
        button[1].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 3:
        button[2].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 4:
        button[3].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 5:
        button[4].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 6:
        button[5].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 7:
        button[6].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 8:
        button[7].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    elif number == 9:
        button[8].config(text = "X", bg = '#7FFFD4', state = DISABLED)
    
def art_intellect(number):
    if number == 1:
        if 1 in player and 2 not in computer and 2 not in player:
            button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(2)
        elif 2 in player and 1 not in computer and 1 not in player:
            button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(1)
        elif 4 in player and 8 not in computer and 8 not in player:
            button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(8)
        elif 8 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        elif 3 in player and 6 not in computer and 6 not in player:
            button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(6)
        elif 6 in player and 3 not in computer and 3 not in player:
            button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(3)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)
            
    if number == 2:
        if 0 in player and 2 not in computer and 2 not in player:
            button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(2)
        elif 2 in player and 0 not in computer and 0 not in player:
            button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(0)
        elif 4 in player and 7 not in computer and 7 not in player:
            button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(7)
        elif 7 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 3:
        if 0 in player and 1 not in computer and 1 not in player:
            button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(1)
        elif 1 in player and 0 not in computer and 0 not in player:
            button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(0)
        elif 5 in player and 8 not in computer and 8 not in player:
            button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(8)
        elif 8 in player and 5 not in computer and 5 not in player:
            button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(5)
        elif 4 in player and 6 not in computer and 6 not in player:
            button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(6)
        elif 6 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 4:
        if 0 in player and 6 not in computer and 6 not in player:
            button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(6)
        elif 6 in player and 0 not in computer and 0 not in player:
            button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(0)
        elif 4 in player and 5 not in computer and 5 not in player:
            button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(5)
        elif 5 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 5:
        if 1 in player and 7 not in computer and 7 not in player:
            button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(7)
        elif 7 in player and 1 not in computer and 1 not in player:
            button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(1)
        elif 3 in player and 5 not in computer and 5 not in player:
            button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(5)
        elif 5 in player and 3 not in computer and 3 not in player:
            button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(3)
        elif 0 in player and 8 not in computer and 8 not in player:
            button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(8)
        elif 8 in player and 0 not in computer and 0 not in player:
            button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(0)
        elif 2 in player and 6 not in computer and 6 not in player:
            button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(6)
        elif 6 in player and 2 not in computer and 2 not in player:
            button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(2)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 6:
        if 2 in player and 8 not in computer and 8 not in player:
            button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(8)
        elif 8 in player and 2 not in computer and 2 not in player:
            button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(2)
        elif 3 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        elif 4 in player and 3 not in computer and 3 not in player:
            button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(3)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 7:
        if 7 in player and 8 not in computer and 8 not in player:
            button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(8)
        elif 8 in player and 7 not in computer and 7 not in player:
            button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(7)
        elif 0 in player and 3 not in computer and 3 not in player:
            button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(3)
        elif 3 in player and 0 not in computer and 0 not in player:
            button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(0)
        elif 4 in player and 2 not in computer and 2 not in player:
            button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(2)
        elif 2 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 8:
        if 6 in player and 8 not in computer and 8 not in player:
            button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(8)
        elif 8 in player and 6 not in computer and 6 not in player:
            button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(6)
        elif 1 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        elif 4 in player and 1 not in computer and 1 not in player:
            button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(1)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)

    if number == 9:
        if 7 in player and 6 not in computer and 6 not in player:
            button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(6)
        elif 6 in player and 7 not in computer and 7 not in player:
            button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(7)
        elif 2 in player and 5 not in computer and 5 not in player:
            button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(5)
        elif 5 in player and 2 not in computer and 2 not in player:
            button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(2)
        elif 4 in player and 0 not in computer and 0 not in player:
            button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(0)
        elif 0 in player and 4 not in computer and 4 not in player:
            button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(4)
        else:
            A = c - player - computer
            b = int(random.choice(list(A)))
            button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
            computer.add(b)
        
        
        
def StartPlay():
    global player 
    global computer 
    EmplyCells = [] 
    for i in range(9): 
        if ( (i+1 in player) or (i+1 in computer)): 
            EmplyCells.append(i+1) 
            RandomIndex = randint(0, len(EmplyCells)-1) 
            click(EmplyCells[RandomIndex])



from tkinter import *
import random
import math
import time 
import sys

player = set()
computer = set()
button = []
c = {0, 1, 2, 3, 4, 5, 6, 7, 8} #номера клеток
def buttons(): 
    """создание поля с кнопками"""
    global root
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

def click(number): 
    """функция клика; принимается номер клетки"""
    global player
    global computer
    process(number)
    player.add(number - 1)
    winner()
    art_intellect(number)
    winner()
        
def process(number):
    """ход игрока"""
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
    

def art_think():
    """Функция, заставляющая компьютер думать. Если у компьютера есть возможность 
    ставить в клетку, лежащую в окрестности двух Х, 
    либо поставить куда-то, что привело бы сразу же к выйгрышному ходу, он использует второй вариант."""
    global f
    f = 0
    if 0 in computer and 1 in computer and 2 not in player:
        button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(2)
        f = 1
    elif 0 in computer and 2 in computer and 1 not in player:
        button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(1)
        f = 1
    elif 0 in computer and 4 in computer and 8 not in player:
        button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(8)
        f = 1
    elif 0 in computer and 8 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 0 in computer and 6 in computer and 3 not in player:
        button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(3)
        f = 1
    elif 0 in computer and 3 in computer and 6 not in player:
        button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(6)
        f = 1
    elif 1 in computer and 4 in computer and 7 not in player:
        button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(7)
        f = 1
    elif 1 in computer and 7 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 2 in computer and 0 in computer and 1 not in player:
        button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(1)
        f = 1
    elif 2 in computer and 1 in computer and 0 not in player:
        button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(0)
        f = 1
    elif 2 in computer and 4 in computer and 6 not in player:
        button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(6)
        f = 1
    elif 2 in computer and 6 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 2 in computer and 5 in computer and 8 not in player:
        button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(8)
        f = 1
    elif 2 in computer and 8 in computer and 5 not in player:
        button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(5)
        f = 1
    elif 3 in computer and 4 in computer and 5 not in player:
        button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(5)
        f = 1
    elif 3 in computer and 5 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 5 in computer and 4 in computer and 3 not in player:
        button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(3)
        f = 1
    elif 5 in computer and 3 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 6 in computer and 3 in computer and 0 not in player:
        button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(0)
        f = 1
    elif 6 in computer and 0 in computer and 3 not in player:
        button[3].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(3)
        f = 1
    elif 6 in computer and 2 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 6 in computer and 4 in computer and 2 not in player:
        button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(2)
        f = 1
    elif 6 in computer and 7 in computer and 8 not in player:
        button[8].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(8)
        f = 1
    elif 6 in computer and 8 in computer and 7 not in player:
        button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(7)
        f = 1
    elif 7 in computer and 1 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 7 in computer and 4 in computer and 1 not in player:
        button[1].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(1)
        f = 1
    elif 8 in computer and 0 in computer and 4 not in player:
        button[4].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(4)
        f = 1
    elif 8 in computer and 4 in computer and 0 not in player:
        button[0].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(0)
        f = 1
    elif 8 in computer and 2 in computer and 5 not in player:
        button[5].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(5)
        f = 1
    elif 8 in computer and 5 in computer and 2 not in player:
        button[2].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(2)
        f = 1
    elif 8 in computer and 6 in computer and 7 not in player:
        button[7].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(7)
        f = 1
    elif 8 in computer and 7 in computer and 6 not in player:
        button[6].config(text = "0", bg = '#FF69B4', state = DISABLED)
        computer.add(6)
        f = 1
    return f

def art_intellect(number):
    """ход компьютера: происходит проверка 
        каждой клетки и стоящих рядом с ней. 
        Делаем так, чтобы компьютер ставил в клетку, где 
        игрок бы следующих ходом выиграл, если же такой 
        клетки нет - ставит рандомно"""
    art_think()
    if f == 0:
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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)
                
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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)

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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)

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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit()

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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)

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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit()

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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)
                
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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)

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
                if len(A) != 0:
                    b = int(random.choice(list(A)))
                    button[b].config(text = "0", bg = '#FF69B4', state = DISABLED)
                    computer.add(b)
                else:
                    sys.exit(0)

def delete_screen(root):
    root.destroy()   


def winner():
    """Функция, проверяющая победителя"""
    if 0 in player and 1 in player and 2 in player:
        delete_screen(root)
        win_X()
    if 0 in player and 3 in player and 6 in player:
        delete_screen(root)
        win_X()
    if 0 in player and 4 in player and 8 in player:
        delete_screen(root)
        win_X()
    if 1 in player and 4 in player and 7 in player:
        delete_screen(root)
        win_X()    
    if 2 in player and 5 in player and 8 in player:
        delete_screen(root)
        win_X()
    if 2 in player and 4 in player and 6 in player:
        delete_screen(root)
        win_X()
    if 3 in player and 4 in player and 5 in player:
        delete_screen(root)
        win_X()
    if 6 in player and 7 in player and 8 in player:
        delete_screen(root)
        win_X()
    
    if 0 in computer and 1 in computer and 2 in computer:
        delete_screen(root)
        win_0()
    if 0 in computer and 3 in computer and 6 in computer:
        delete_screen(root)
        win_0()
    if 0 in computer and 4 in computer and 8 in computer:
        delete_screen(root)
        win_0()
    if 1 in computer and 4 in computer and 7 in computer:
        delete_screen(root)
        win_0()  
    if 2 in computer and 5 in computer and 8 in computer:
        delete_screen(root)
        win_0()
    if 2 in computer and 4 in computer and 6 in computer:
        delete_screen(root)
        win_0()
    if 3 in computer and 4 in computer and 5 in computer:
        delete_screen(root)
        win_0()
    if 6 in computer and 7 in computer and 8 in computer:
        delete_screen(root)
        win_0()


    if 0 in player and 1 in player and 4 in player and 5 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 1 in player and 2 in player and 3 in player and 4 in player and 8 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 3 in player and 4 in player and 5 in player and 7 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 2 in player and 4 in player and 5 in player and 7 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 2 in player and 3 in player and 5 in player and 7 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 2 in player and 7 in player and 5 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 2 in player and 3 in player and 7 in player and 8 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 1 in player and 8 in player and 5 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 1 in player and 2 in player and 3 in player and 8 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 1 in player and 3 in player and 8 in player and 5 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 1 in player and 3 in player and 4 in player and 8 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 1 in player and 8 in player and 4 in player and 5 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 0 in player and 7 in player and 4 in player and 5 in player and 6 in player:
        delete_screen(root)
        drawn()
    if 2 in player and 3 in player and 4 in player and 7 in player and 8 in player:
        delete_screen(root)
        drawn()

def win_0(): 
    """Вывод картинки в случае выигрыша 0"""
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canva = Canvas(root, bg='black')
    canva.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="win_0.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="Game over", width=10, height=2, bg="#18ff95", fg="#ff182e", font="Arial 17")

    def deletescreen(event):
        root.destroy()

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()

def win_X(): 
    """Вывод картинки в случае выигрыша X"""
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canva = Canvas(root, bg='black')
    canva.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="win_X.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="Game over", width=10, height=2, bg="#18ff95", fg="#ff182e", font="Arial 17")
    
    def deletescreen(event):
        root.destroy()
        

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()
    
def drawn(): 
    """Вывод картинки в случае ничьей"""
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canva = Canvas(root, bg='black')
    canva.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="drawn.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="Game over", width=10, height=2, bg="#18ff95", fg="#ff182e", font="Arial 17")

    def deletescreen(event):
        root.destroy()

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()
        
def StartPlay(): 
    """Инициализация начала игры"""
    global player 
    global computer 
    EmptyCells = [] 
    for i in range(9): 
        if ( (i+1 in player) or (i+1 in computer)): 
            EmptyCells.append(i+1) 
            RandomIndex = randint(0, len(EmptyCells)-1) 
            click(EmptyCells[RandomIndex])


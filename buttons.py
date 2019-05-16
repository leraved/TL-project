from tkinter import *
import random
root = Tk()
player = set()
computer = set()
button = []
c = {0, 1, 2, 3, 4, 5, 6, 7, 8} #заменить!
active = 1
def buttons():
    screen_height = root.winfo_screenheight()
    a = screen_height/8
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[0].grid(row = 0, column = 0, sticky = "snew", ipadx = a, ipady = a)
    button[0].config(command = lambda: click(1))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[1].grid(row = 0, column = 1, sticky = "snew", ipadx = a, ipady = a)
    button[1].config(command = lambda: click(2))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[2].grid(row = 0, column = 2, sticky = "snew", ipadx = a, ipady = a)
    button[2].config(command = lambda: click(3))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[3].grid(row = 1, column = 0, sticky = "snew", ipadx = a, ipady = a)
    button[3].config(command = lambda: click(4))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[4].grid(row = 1, column = 1, sticky = "snew", ipadx = a, ipady = a)
    button[4].config(command = lambda: click(5))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[5].grid(row = 1, column = 2, sticky = "snew", ipadx = a, ipady = a)
    button[5].config(command = lambda: click(6))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[6].grid(row = 2, column = 0, sticky = "snew", ipadx = a, ipady = a)
    button[6].config(command = lambda: click(7))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[7].grid(row = 2, column = 1, sticky = "snew", ipadx = a, ipady = a)
    button[7].config(command = lambda: click(8))
    button.append(Button(root, text = "", bg = 'skyblue', activebackground = 'lightgreen'))
    button[8].grid(row = 2, column = 2, sticky = "snew", ipadx = a, ipady = a)
    button[8].config(command = lambda: click(9))

def click(number): #номер клетки
    global active
    global player
    global computer
    if active == 1:
        process(number)
        player.add(number)
        active = 2
    else:
        art_intellect()
        acive = 1

def process(number):
    if number == 1:
        button[0].config(text = "0", bg = '#7B68EE', state = DISABLED)
    elif number == 2:
        button[1].config(text = "0", bg = '#7B68EE', state = DISABLED)  
    elif number == 3:
        button[2].config(text = "0", bg = '#7B68EE', state = DISABLED)
    elif number == 4:
        button[3].config(text = "0", bg = '#7B68EE', state = DISABLED)  
    elif number == 5:
        button[4].config(text = "0", bg = '#7B68EE', state = DISABLED)
    elif number == 6:
        button[5].config(text = "0", bg = '#7B68EE', state = DISABLED)  
    elif number == 7:
        button[6].config(text = "0", bg = '#7B68EE', state = DISABLED)
    elif number == 8:
        button[7].config(text = "0", bg = '#7B68EE', state = DISABLED)  
    elif number == 9:
        button[8].config(text = "0", bg = '#7B68EE', state = DISABLED)

def art_intellect():
    '''if (number not in player) and (number not in computer):
        button[number].config(text = "X", bg = '#FF69B4', state = DISABLED)
    else:'''
    A = c - player - computer
    print(A)
    button[int(random.choice(list(A)))].config(text = "X", bg = '#FF69B4', state = DISABLED)
        
        
        
        
        
        
def AutoPlay(): 
    global player 
    global computer 
    EmplyCells = [] 
    for i in range(9): 
        if ( (i+1 in player) or (i+1 in computer)): 
            EmplyCells.append(i+1) 
            RandomIndex = randint(0, len(EmplyCells)-1) 
            click(EmplyCells[RandomIndex])

buttons()
AutoPlay()
root.mainloop()


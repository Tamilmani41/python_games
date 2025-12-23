from tkinter import *
import random

players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

def next_turn (row,column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons [row][column]["text"] = player
            if check_winner() is False :
                player = players[1]
                label.config(text = players[1]+" turn")
            elif check_winner() is True :
                label.config(text = players[0]+" wins" )
            elif check_winner() == "Tie":
                label.config(text = "Tie")

        else :
            buttons [row][column]["text"] = player
            if check_winner() is False :
                player = players[0]
                label.config(text = players[0]+" turn")
            elif check_winner() is True :
                label.config(text = players[1]+" wins")
            elif check_winner() == "Tie":
                label.config(text = "Tie")

def new_game ():
    global player
    player = random.choice(players)
    label.config(text = player+ " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "",bg = "#F0F0F0")

def empty_spaces():
    spaces = 9
    for row in range (3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -=1
        
    if spaces == 0:
        return False
    else:
        return True

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):   
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True 
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else :
        return False 

window =Tk()
window.title("tic tac toe")
# width = 500
# height = 500

# screen_w = window.winfo_screenwidth()
# screen_h = window.winfo_screenheight()

# x = (screen_w/2) - (width/2)
# y = (screen_h/2) - (height/2)

# window.geometry("{}x{}+{}+{}".format(width,height,x,y))


label = Label(text = player+ " turn :)",font = ("Impact",25))
label.pack(side = TOP)

reset_button = Button(text = "restart",font = ("Impact",25),command = new_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons [row][column] = Button(frame,text = "",font = ('consolas',25),
                                       command = lambda row = row ,column = column:next_turn(row,column),
                                       width = 5,height = 2,padx=5,pady=2,border=5)
        buttons[row][column].grid(row = row,column = column)


window.mainloop()

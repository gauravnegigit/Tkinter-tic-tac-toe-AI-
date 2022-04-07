from tkinter import *
from tkinter import messagebox
import random 
import time 

def button():
    b = Button(root , padx = 1 , bg = "papaya whip" , width = 3 , text = " " , relief = "sunken" , font = ("Arial Black" , 50 , "bold") , bd = 10)
    return b

def change_a():
    global a 
    for i in ['O' , 'X']:
        if not(i == a):
            a = i 
            break 

def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
                    return True 
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()  
        return True  
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
        return True 

def isWinner(bo,le):
	return ((bo[7]==le and bo[8]==le and bo[9]==le) or 
	(bo[4]==le and bo[5]==le and bo[6]==le) or
	(bo[1] ==le and bo[2]==le and bo[3]==le) or
	(bo[1]==le and bo[4]==le and bo[7]== le ) or
 	(bo[2]==le and bo[5]==le and bo[8]== le ) or 
	(bo[3]==le and bo[6]==le and bo[9]== le ) or 
	(bo[1]==le and bo[5]==le and bo[9]== le ) or 
	(bo[3]==le and bo[5]==le and bo[7]==le ))

def reset():
    global a , player 
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    player = a = random.choice(['O','X'])   

def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        if check() == None : 
            change_a()
            label.config(text=a+"'s Chance")
            
            move = compMove() - 1
            print(move)

            i , j = move //3 , move % 3

            b[i][j].config(text=a,state=DISABLED,disabledforeground=colour[a])

            check()
            change_a()
            label.config(text=a+"'s Chance")

def compMove():
    board = [' ']

    for i in range(3):
        for j in range(3):
            board.append(b[i][j]['text'])

    possibleMoves = [x for x,letter in enumerate(board) if letter ==' ' and x!=0]
    move=0

    for let in ['O','X']:
        for i in possibleMoves : 
            boardCopy = board[::]
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i 
                return move 

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen)>0:
        move = random.choice(cornersOpen)
        return move 

    if 5 in possibleMoves:
        move=5
        return 5

    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move = random.choice(edgesOpen)
        return move 

    return move


# Driver's code
root = Tk()
root.title("TIC TAC TOE")
player = a = random.choice(['O' , 'X'])
colour={'O':"deep sky blue",'X':"lawn green"}

b = [[] , [], []]

for i in range(3):
    for j in range(3):
        b[i].append(button())

        
        b[i][j].config(command = lambda row = i , col = j : click(row , col))

        b[i][j].grid(row = i , column = j)


label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()
#hello frands im aditya p
#tic tac toe game
#after you get 3 in a row, click on the X/O tile again to display win message box
#EDIT(17/10/2017): Added scoreboard and resetting of game

#CODE(with partial explanation):

#modules import and variable setup
from tkinter import *
import tkinter as tk
root = tk.Tk()
import tkinter.messagebox
root.title("tic tac toe")
bclick = True
var = 1
Owins = 0
Xwins = 0
draw = 0


#definition of function for making playing area
def board(buttons):
   global bclick
   if buttons["text"] == " " and bclick == True:
       buttons["text"] = "F"
       bclick = False
   elif buttons["text"] == " " and bclick == False:
       buttons["text"] = "P"
       bclick = True
       
#now for win situations
#there are 8 win situations for X or O (see down for grid plot): 123 ; 456 ; 789 ; 147 ; 258 ; 369 ; 159 and 357
#so , the below codes check for any of the situations for X or O
      
#situation if player X wins
   elif (button1["text"] == "P" and button2["text"] == "P" and button3["text"] == "P" or
       button4["text"] == "P" and button5["text"] == "P" and button6["text"] == "P" or
       button7["text"] == "P" and button8["text"] == "P" and button9["text"] == "P" or
       button1["text"] == "P" and button4["text"] == "P" and button7["text"] == "P" or
       button2["text"] == "P" and button5["text"] == "P" and button8["text"] == "P" or
       button3["text"] == "P" and button6["text"] == "P" and button9["text"] == "P" or
       button1["text"] == "P" and button5["text"] == "P" and button9["text"] == "P" or
       button3["text"] == "P" and button5["text"] == "P" and button7["text"] == "P" ):
            tk.messagebox.showinfo("STOP PLAYING BY URSELF", "GO MAKE FRIENDZZZ")
            button1["text"] = " "
            button2["text"] = " "
            button3["text"] = " "
            button4["text"] = " "
            button5["text"] = " "
            button6["text"] = " "
            button7["text"] = " "
            button8["text"] = " "
            button9["text"] = " "
            global Xwins
            Xwins = Xwins + 1
            Xscoreboard["text"] = "P =", Xwins
#situation if player O wins
   elif (button1["text"] == "F" and button2["text"] == "F" and button3["text"] == "F" or
        button4["text"] == "F" and button5["text"] == "F" and button6["text"] == "F" or
        button7["text"] == "F" and button8["text"] == "F" and button9["text"] == "F" or
        button1["text"] == "F" and button4["text"] == "F" and button7["text"] == "F" or
        button2["text"] == "F" and button5["text"] == "F" and button8["text"] == "F" or
        button3["text"] == "F" and button6["text"] == "F" and button9["text"] == "F" or
        button1["text"] == "F" and button5["text"] == "F" and button9["text"] == "F" or
        button3["text"] == "F" and button5["text"] == "F" and button7["text"] == "F" ):
             tk.messagebox.showinfo("BRUH IK U MADE F WIN ON PURPOUSE UGH", "UR PLAYIN' ALONE BRUH")
             button1["text"] = " "
             button2["text"] = " "
             button3["text"] = " "
             button4["text"] = " "
             button5["text"] = " "
             button6["text"] = " "
             button7["text"] = " "
             button8["text"] = " "
             button9["text"] = " "
             global Owins                       
             Owins = Owins + 1
             Oscoreboard["text"] = "F =", Owins
   elif (button1["text"] != "P" or button2["text"] != "P" or button3["text"] != "P" and
       button4["text"] != "P" or button5["text"] != "P" or button6["text"] != "P" and
       button7["text"] != "P" or button8["text"] != "P" or button9["text"] != "P" and
       button1["text"] != "P" or button4["text"] != "P" or button7["text"] != "P" and
       button2["text"] != "P" or button5["text"] != "P" or button8["text"] != "P" and
       button3["text"] != "P" or button6["text"] != "P" or button9["text"] != "P" and
       button1["text"] != "P" or button5["text"] != "P" or button9["text"] != "P" and
       button3["text"] != "P" or button5["text"] != "P" or button7["text"] != "P" and
       button1["text"] != "F" or button2["text"] != "F" or button3["text"] != "F" and
       button4["text"] != "F" or button5["text"] != "F" or button6["text"] != "F" and
       button7["text"] != "F" or button8["text"] != "F" or button9["text"] != "F" and
       button1["text"] != "F" or button4["text"] != "F" or button7["text"] != "F" and
       button2["text"] != "F" or button5["text"] != "F" or button8["text"] != "F" and
       button3["text"] != "F" or button6["text"] != "F" or button9["text"] != "F" and
       button1["text"] != "F" or button5["text"] != "F" or button9["text"] != "F" and
       button3["text"] != "F" or button5["text"] != "F" or button7["text"] != "F" ):
              tk.messagebox.showinfo("SUCH A NOOB...", "ENDED IN A DRAW BY URSELF UGH... STOP PLAYING ALONE GO MAKE FRENDS")
              button1["text"] = " "
              button2["text"] = " "
              button3["text"] = " "
              button4["text"] = " "
              button5["text"] = " "
              button6["text"] = " "
              button7["text"] = " "
              button8["text"] = " "
              button9["text"] = " "
              global draw
              draw =draw + 1
              drawscoreboard["text"] = "Draw =", draw
        
#code to make 3 x 3 grid with 9 buttons
buttons = StringVar()

#button no.1
button1 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

#button no.2
button2 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button2))
button2.grid(row = 2, column = 0, sticky = S+N+E+W)

#button no.3
button3 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button3))
button3.grid(row = 3, column = 0, sticky = S+N+E+W)

#button no.4
button4 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button4))
button4.grid(row = 1, column = 1, sticky = S+N+E+W)

#button no.5
button5 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

#button no.6
button6 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button6))
button6.grid(row = 3, column = 1, sticky = S+N+E+W)

#button no.7
button7 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button7))
button7.grid(row = 1, column = 2, sticky = S+N+E+W)

#button no.8
button8 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button8))
button8.grid(row = 2, column = 2, sticky = S+N+E+W)

#button no.9
button9 = Button(root, text = " ", height = 4, width = 8, command = lambda: board(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

Xscoreboard = Label(root, text = ("X =", Xwins))
Xscoreboard.grid(row = 1, column = 5, sticky = S+N+E+W)

Oscoreboard = Label(root, text = ("O =", Owins))
Oscoreboard.grid(row = 2, column = 5, sticky = S+N+E+W)

drawscoreboard = Label(root, text = ("Draw =", draw))
drawscoreboard.grid(row = 3, column = 5, sticky = S+N+E+W)

#looping the program
root.mainloop()


#Have a good day!
#NOTE:
#the grid is in the form:-
#                             1   2   3
#                             4   5   6
#                             7   8   9





              

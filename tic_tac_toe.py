from tkinter import *

# players click counter
clk=0

#when a player wins,It disables all buttons
def disable_all():
    b1["state"]=DISABLED
    b2["state"]=DISABLED
    b3["state"]=DISABLED
    b4["state"]=DISABLED
    b5["state"]=DISABLED
    b6["state"]=DISABLED
    b7["state"]=DISABLED
    b8["state"]=DISABLED
    b9["state"]=DISABLED
    
# It finds out wich player is winner
def winner():
    if ((b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or
        (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or
        (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or
        (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or
        (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or
        (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O") or
        (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or
        (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O")):
        lb.config(text="Player1 wins!")
        disable_all()
        
                  
    elif((b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or
        (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or
        (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or
        (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or
        (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or
        (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X") or
        (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or
        (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X")):
                  lb.config(text="Player2 wins!")
                  disable_all()

    else:
                  pass

# main function: draw button labels and invoke other functions
def show(btn):
    global clk
    clk+=1
    if clk%2==0:
        lb["text"]="Player1 Move"
    else:
        lb["text"]="player2 Move"
        
    if btn==1:
        if clk%2==0:
            b1.config(text="X", state=DISABLED)
            winner()
        else:
            b1.config(text="O", state=DISABLED)
            winner()

    if btn==2:
        if clk%2==0:
            b2.config(text="X", state=DISABLED)
            winner()
        else:
            b2.config(text="O", state=DISABLED)
            winner()

    if btn==3:
        if clk%2==0:
            b3.config(text="X", state=DISABLED)
            winner()
        else:
            b3.config(text="O", state=DISABLED)
            winner()

    if btn==4:
        if clk%2==0:
            b4.config(text="X", state=DISABLED)
            winner()
        else:
            b4.config(text="O", state=DISABLED)
            winner()

    if btn==5:
        if clk%2==0:
            b5.config(text="X", state=DISABLED)
            winner()
        else:
            b5.config(text="O", state=DISABLED)
            winner()

    if btn==6:
        if clk%2==0:
            b6.config(text="X", state=DISABLED)
            winner()
        else:
            b6.config(text="O", state=DISABLED)
            winner()

    if btn==7:
        if clk%2==0:
            b7.config(text="X", state=DISABLED)
            winner()
        else:
            b7.config(text="O", state=DISABLED)
            winner()

    if btn==8:
        if clk%2==0:
            b8.config(text="X", state=DISABLED)
            winner()
        else:
            b8.config(text="O", state=DISABLED)
            winner()

    if btn==9:
        if clk%2==0:
            b9.config(text="X", state=DISABLED)
            winner()
        else:
            b9.config(text="O", state=DISABLED)
            winner()
        

    


    
# draw game board
top=Tk()
top.geometry("250x300")
b1=Button(top, text="", width=3, height=3, command=lambda: show(1))
b1.place(x=40,y=50)

b2=Button(top, text="", width=3, height=3, command=lambda: show(2))
b2.place(x=100,y=50)

b3=Button(top, text="", width=3, height=3, command=lambda: show(3))
b3.place(x=160,y=50)

b4=Button(top, text="", width=3, height=3, command=lambda: show(4))
b4.place(x=40,y=110)

b5=Button(top, text="", width=3, height=3, command=lambda: show(5))
b5.place(x=100,y=110)

b6=Button(top, text="", width=3, height=3, command=lambda: show(6))
b6.place(x=160,y=110)

b7=Button(top, text="", width=3, height=3, command=lambda: show(7))
b7.place(x=40,y=170)

b8=Button(top, text="", width=3, height=3, command=lambda: show(8))
b8.place(x=100,y=170)

b9=Button(top, text="", width=3, height=3, command=lambda: show(9))
b9.place(x=160,y=170)

lb=Label(top, text="Player1 Move", width=10, height=2)
lb.place(x=80,y=10)        
         
mainloop()

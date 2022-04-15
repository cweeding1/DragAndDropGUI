import tkinter as tk
from tkinter import *
import random, time

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


def drag_end(event):
    widget = event.widget
    widget.endX = event.x
    widget.endY = event.y


window = Tk()
window.geometry("800x480")

def destroy():
    holder = []
    for label in window.children.values():
        #label.destroy()
        holder.append(label)

    for i in holder:
        i.destroy()

    spawn()


def spawn():

    function1 = Label(window, bg="green", width=7, height=3, text="move", borderwidth=2, relief="groove")
    function1.place(x=25, y=25)
    function1.bind("<Button-1>", drag_start)
    function1.bind("<B1-Motion>", drag_motion)

    function2 = Label(window, bg="purple", width=7, height=3, text="turn", borderwidth=2, relief="groove")
    function2.place(x=100, y=25)
    function2.bind("<Button-1>", drag_start)
    function2.bind("<B1-Motion>", drag_motion)

    function3 = Label(window, bg="yellow", width=7, height=3, text="head tilt", borderwidth=2, relief="groove")
    function3.place(x=175, y=25)
    function3.bind("<Button-1>", drag_start)
    function3.bind("<B1-Motion>", drag_motion)

    function4 = Label(window, bg="orange", width=7, height=3, text="head turn", borderwidth=2, relief="groove")
    function4.place(x=250, y=25)
    function4.bind("<Button-1>", drag_start)
    function4.bind("<B1-Motion>", drag_motion)

    function5 = Label(window, bg="blue", width=7, height=3, text="waist", borderwidth=2, relief="groove")
    function5.place(x=325, y=25)
    function5.bind("<Button-1>", drag_start)
    function5.bind("<B1-Motion>", drag_motion)

    function6 = Label(window, bg="red", width=7, height=3, text="speech", borderwidth=2, relief="groove")
    function6.place(x=400, y=25)
    function6.bind("<Button-1>", drag_start)
    function6.bind("<B1-Motion>", drag_motion)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="1")
    slot1.place(x=25, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="2")
    slot1.place(x=100, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="3")
    slot1.place(x=175, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="4")
    slot1.place(x=250, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="5")
    slot1.place(x=325, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="6")
    slot1.place(x=400, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="7")
    slot1.place(x=475, y=200)

    slot1 = Label(window, bg="white", width=7, height=1, borderwidth=2, relief="groove", text="8")
    slot1.place(x=550, y=200)

    execute = Button(window, bg="gray", width=15, height=3, text="execute", activebackground="green", command=getInstructions, borderwidth=2, relief="groove")
    execute.place(x=625, y=400)

    clear = Button(window, bg="gray", width=15, height=3, text="clear", activebackground="red", command=destroy, borderwidth=2, relief="groove")
    clear.place(x=50, y=400)


def createLabel(xCoor,yCoor, funcName, color):
    function = Label(window, bg=color, width=7, height=3, text=funcName, borderwidth=2, relief="groove")
    function.place(x=xCoor, y=yCoor)

    function.bind("<Button-1>", drag_start)
    function.bind("<B1-Motion>", drag_motion)

def getArgs(instructions):
    argInstucions = {}
    #loop through instructions
    for i in instructions:
        #print(i)
        argInstucions.update({i: 0})

    #print(argInstucions)


def getInstructions():

    instructions = [""] * 8
    for label in window.children.values():
        text = label.cget("text")

        # BOX 1 #
        if 13 <= label.winfo_x() <= 89 and 130 < label.winfo_y() <= 199:
            instructions[0] = text
        # BOX 2 #
        elif 90 <= label.winfo_x() <= 166 and 130 < label.winfo_y() <= 199:
            instructions[1] = text
        # BOX 3 #
        elif 167 <= label.winfo_x() <= 242 and 130 < label.winfo_y() <= 199:
            instructions[2] = text
        # BOX 4 #
        elif 243 <= label.winfo_x() <= 318 and 130 < label.winfo_y() <= 199:
            instructions[3] = text
        # BOX 5 #
        elif 319 <= label.winfo_x() <= 394 and 130 < label.winfo_y() <= 199:
            instructions[4] = text
        # BOX 6 #
        elif 395 <= label.winfo_x() <= 470 and 130 < label.winfo_y() <= 199:
            instructions[5] = text
        # BOX 7 #
        elif 471 <= label.winfo_x() <= 546 and 130 < label.winfo_y() <= 199:
            instructions[6] = text
        # BOX 8 #
        elif 547 <= label.winfo_x() <= 622 and 130 < label.winfo_y() <= 199:
            instructions[7] = text


    """
    for label in window.children.values():
        text = label.cget("text")
        if label.winfo_x() > 450 and label.winfo_y() < 400:
            #print(label.cget("text"))
            if text == "move":
                #instructions[0] = text
                move()
            elif text == "turn":
                #instructions[1] = text
                turn()
            elif text == "head tilt":
                head_tilt()
            elif text == "head turn":
                head_turn()
            elif text == "waist turn":
                waist_turn()
            elif text == "speech input":
                speech_input()
    """
    print(instructions)
    for i in instructions:
        if i == "move":
            move()
        elif i == "turn":
            turn()
        elif i == "head tilt":
            head_tilt()
        elif i == "head turn":
            head_turn()
        elif i == "waist":
            waist_turn()
        elif i == "speech":
            speech_input()
        else:
            print("unknown function")
            time.sleep(2)

    #getArgs(instructions)


def move():
    print("move")
    time.sleep(2)
    """
    time = int(input("how long: "))
    if time >= 0:
        print("move forward " + str(time) + " seconds")
    elif time < 0:
        print("move turn " + str(abs(time)) + " seconds")
    """


def turn():
    print("turn")
    time.sleep(2)


def head_tilt():
    print("head tilt")
    time.sleep(2)


def head_turn():
    print("head turn")
    time.sleep(2)


def waist_turn():
    print("waist turn")
    time.sleep(2)

def speech_input():
    print("speech input")
    time.sleep(2)


def callback(event):
    x = event.x
    y = event.y

    #print("X: " + str(x) + " Y: " + str(y))

    if 25 < x < 75 and 25 < y < 100:
        createLabel(25, 25, "move", "green")
    elif 100 < x < 150 and 25 < y < 100:
        createLabel(100, 25, "turn", "purple")
    elif 175 < x < 225 and 25 < y < 100:
        createLabel(175, 25, "head tilt", "yellow")
    elif 250 < x < 300 and 25 < y < 100:
        createLabel(250, 25, "head turn", "orange")
    elif 325 < x < 375 and 25 < y < 100:
        createLabel(325, 25, "waist", "blue")
    elif 400 < x < 450 and 25 < y < 100:
        createLabel(400, 25, "speech", "red")


spawn()

window.bind("<Button-1>", callback)

window.mainloop()

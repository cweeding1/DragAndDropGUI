import tkinter as tk
from Maestro import Controller
import thread, time

MOTORS = 1
TURN = 2
BODY = 0
HEADTURN = 3
HEADTILT = 4

class KeyControl():
    def __init__(self, win):
        self.root = win
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000

############################################

    def moveCommand(self, direction, duration):
        if direction >= 0:
            #this only works for forward
            print("moving forward")
            self.motors -= 700
            #eventually this will be a variable
            time.sleep(duration)
            print("stopping")
            self.motors += 700
        else:
            print("moving backward")
            self.motors += 700
            time.sleep(duration)
            print("stopping")
            self.motors -= 700

    def turnCommand(self, direction, duration):
        if direction >= 0:
            print("turning")
            self.turn += 700
            time.sleep(duration)
            print("stopping")
            self.turn -= 700
        else:
            print("turning")
            self.turn -= 700
            time.sleep(duration)
            print("stopping")
            self.turn += 700

    def headTiltCommand(self, direction):
        if direction > 0:
            self.headTilt -= 400

        elif direction < 0:
            self.headTilt += 400

        elif direction == 0:
            self.headTilt = 6000

    def headTurnCommand(self, direction):
        if direction > 0:
            self.headTurn -= 400

        elif direction < 0:
            self.headTurn += 400

        elif direction == 0:
            self.headTurn = 6000

    def waistCommand(self, direction):
        if direction > 0:
            self.body -= 600

        elif direction < 0:
            self.body += 600

        elif direction == 0:
            self.body = 6000

    def speechCommand(self):
        pass
####################################

    def arrow(self, key):
        print(key.keycode)
        # Motors, foward and backward
        if key.keycode == 111: #up arrow
            if (self.motors == 6000):
                self.motors -= 700
            else:
                self.motors -= 200
                if(self.motors < 4900):
                    self.motors = 4900
            #print(self.motors)
            self.tango.setTarget(MOTORS, self.motors)
        if key.keycode == 116: #down arrow
            if(self.motors == 6000):
                self.motors += 700
            else:
                self.motors += 200
                if(self.motors  > 7100):
                    self.motors = 7100
            #print(self.motors)
            self.tango.setTarget(MOTORS, self.motors)

        # Motors, turn
        if key.keycode == 113: #left arrow
            self.turn += 700
            if(self.turn > 6700):
                self.turn = 6700
            #print(self.turn)
            self.tango.setTarget(TURN, self.turn)
        if key.keycode == 114: #right arrow
            self.turn -= 700
            if(self.turn < 5300):
                self.turn = 5300
            #print(self.turn)
            self.tango.setTarget(TURN, self.turn)

        # Motors, stop
        if key.keycode == 65: #spacebar
            self.motors = 6000
            self.turn = 6000
            print(self.motors)
            self.tango.setTarget(MOTORS, self.motors)
            self.tango.setTarget(TURN, self.turn)

    def waist(self, key):
        print(key.keycode)            
        # Waist, turn
        if key.keycode == 52:
            self.body -= 600
            if(self.body < 3000 ):
                self.body = 3000
            #print(self.body)
            self.tango.setTarget(BODY, self.body)
        if key.keycode == 53:
            self.body = 6000
            self.tango.setTarget(BODY, self.body)
        if key.keycode == 54:
            self.body += 600
            if(self.body > 9000):
                self.body = 9000
            #print(self.body)
            self.tango.setTarget(BODY, self.body)

    def head(self, key):
        print(key.keycode)
        # head turn
        if key.keycode == 38:
            self.headTurn -= 400
            if(self.headTurn < 3000):
                self.headTurn = 3000
            #print(self.headTurn)
            self.tango.setTarget(HEADTURN, self.headTurn)
        if key.keycode == 39:
            self.headTurn = 6000
            self.tango.setTarget(HEADTURN, self.headTurn)
        if key.keycode == 40:
            self.headTurn += 400
            if(self.headTurn > 9000):
                self.headTurn = 9000
            #print(self.headTurn)
            self.tango.setTarget(HEADTURN, self.headTurn)
            
        # head tilt
        if key.keycode == 24:
            self.headTilt -= 400
            if(self.headTilt < 3000):
                self.headTilt = 3000
            #print(self.headTilt)
            self.tango.setTarget(HEADTILT, self.headTilt)
        if key.keycode == 25:
            self.headTilt = 6000
            self.tango.setTarget(HEADTILT, self.headTilt)
        if key.keycode == 26:
            self.headTilt += 400
            if(self.headTilt > 9000):
                self.headTilt = 9000
            #print(self.headTilt)
            self.tango.setTarget(HEADTILT, self.headTilt)

window = Tk()
window.geometry("800x400")
inputs = KeyControl(window)


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
    execute.place(x=625, y=300)

    clear = Button(window, bg="gray", width=15, height=3, text="clear", activebackground="red", command=destroy, borderwidth=2, relief="groove")
    clear.place(x=50, y=300)


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

    print(instructions)
    for i in instructions:
        if i == "move":
            inputs.moveCommand(1, 3)
        elif i == "turn":
            inputs.turnCommand(1, 3)
        elif i == "head tilt":
            inputs.headTiltCommand(1)
        elif i == "head turn":
            inputs.headTurnCommand(1)
        elif i == "waist":
            inputs.waistCommand(1)
        elif i == "speech":
            inputs.speechCommand()
        else:
            print("unknown function")
            time.sleep(1)

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

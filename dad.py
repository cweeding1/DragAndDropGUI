import tkinter as tk
from tkinter import *
from Maestro import Controller
import _thread
import time
import speech_recognition as sr
import vlc
import pyttsx3


MOTORS = 1
TURN = 2
BODY = 0
HEADTURN = 3
HEADTILT = 4


class KeyControl:
    def __init__(self, win):
        self.root = win
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self.headTilt = 6000
        self.motors = 6000
        self.turn = 6000

    ############################################

    def moveCommand(self, speed, duration):
        self.motors = int(speed)
        self.tango.setTarget(MOTORS, self.motors)
        time.sleep(int(duration))
        self.motors = 6000
        self.tango.setTarget(MOTORS, self.motors)
        time.sleep(1)

    def turnCommand(self, direction, duration):
        self.turn = int(direction)
        self.tango.setTarget(TURN, self.turn)
        time.sleep(int(duration))
        self.turn = 6000
        self.tango.setTarget(TURN, self.turn)
        time.sleep(1)

    def headTiltCommand(self, direction):
        self.headTilt = int(direction)
        self.tango.setTarget(HEADTILT, self.headTilt)
        time.sleep(1)

    def headTurnCommand(self, direction):
        self.headTurn = int(direction)
        self.tango.setTarget(HEADTURN, self.headTurn)
        time.sleep(1)

    def waistCommand(self, direction):
        self.body = int(direction)
        self.tango.setTarget(BODY, self.body)
        time.sleep(1)

    def speechCommand(self):
        listening = True
        while listening:
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                r.energy_threshold = 3000
                r.pause_threshold = 0.6
                r.non_speaking_duration = 0.6

                try:
                    print("listening")
                    audio = r.listen(source)
                    print("Got audio")
                    word = r.recognize_google(audio)
                    print(word)
                    if word.lower().find('hello') > -1:
                        listening = False
                except sr.UnknownValueError:
                    print("Don't know that word")

    def tts(self, word):
        engine = pyttsx3.init()
        voice_num = 2
        
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 110)
        engine.setProperty('voice', voices[voice_num].id)
        
        engine.say(word)
        engine.runAndWait()

    ############################################


window = tk.Tk()
window.geometry("800x400")

speedVals = [6000] * 8
durationVals = [1] * 8
ttsVals = ["default"] * 8

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() + event.x
    y = widget.winfo_y() + event.y
    widget.place(x=x, y=y)


def drag_end(event):
    widget = event.widget
    widget.endX = event.x
    widget.endY = event.y


def destroy():
    holder = []
    for label in window.children.values():
        # label.destroy()
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
    
    function7 = Label(window, bg="white", width=7, height=3, text="tts", borderwidth=2, relief="groove")
    function7.place(x=475, y=25)
    function7.bind("<Button-1>", drag_start)
    function7.bind("<B1-Motion>", drag_motion)

    slot1 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="1",command=lambda: getArgs(1))
    slot1.place(x=25, y=200)

    slot2 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="2",command=lambda: getArgs(2))
    slot2.place(x=100, y=200)

    slot3 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="3",command=lambda: getArgs(3))
    slot3.place(x=175, y=200)

    slot4 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="4",command=lambda: getArgs(4))
    slot4.place(x=250, y=200)

    slot5 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="5",command=lambda: getArgs(5))
    slot5.place(x=325, y=200)

    slot6 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="6",command=lambda: getArgs(6))
    slot6.place(x=400, y=200)

    slot7 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="7",command=lambda: getArgs(7))
    slot7.place(x=475, y=200)

    slot8 = Button(window, bg="white", width=7, height=1, borderwidth=2,
                   relief="groove", text="8",command=lambda: getArgs(8))
    slot8.place(x=550, y=200)

    execute = Button(window, bg="gray", width=15, height=3, text="execute",
                     activebackground="green",command=getInstructions, borderwidth=2, relief="groove")
    execute.place(x=625, y=300)

    clear = Button(window, bg="gray", width=15, height=3, text="clear",
                   activebackground="red", command=destroy,borderwidth=2, relief="groove")
    clear.place(x=50, y=300)

def screenSaver():
    #temp = Tk()
    #canvas = Canvas(temp, width=800, height=400)
    #canvas.pack()
    #bg = PhotoImage(master=canvas, file="yungHunter.png")
    #canvas.create_image(0,0, anchor=NW, image=bg)
    #exitButton = Button(temp, width=10, height=5, command=lambda : temp.destroy())
    #exitButton.place(x=5,y=5)
    window.configure(bg="white")
    getInstructions()
    
    #mainloop()

def createLabel(xCoor, yCoor, funcName, color):
    function = Label(window, bg=color, width=7, height=3, text=funcName, borderwidth=2, relief="groove")
    function.place(x=xCoor, y=yCoor)

    function.bind("<Button-1>", drag_start)
    function.bind("<B1-Motion>", drag_motion)


def getArgs(buttonNum):
    argWindow = Tk()
    argWindow.geometry("250x300")

    function1 = Label(argWindow, bg="gray", width=16, height=1, text="Speed/Direction", borderwidth=2, relief="groove")
    function1.place(x=43, y=0)

    function2 = Label(argWindow, bg="gray", width=16, height=1, text="Duration", borderwidth=2, relief="groove")
    function2.place(x=43, y=70)

    function3 = Label(argWindow, bg="gray", width=16, height=1, text="TTS", borderwidth=2, relief="groove")
    function3.place(x=43, y=155)
    
    speed = StringVar(argWindow)
    speed.set(str(speedVals[buttonNum - 1]))
    speedList = [4000, 4600, 5300, 5500, 6000, 6500, 6700, 7400, 8000]
    speed_menu = OptionMenu(argWindow, speed, *speedList)
    speed_menu.configure(width=13, height=2)
    speed_menu.place(x=40, y=20)

    dur = StringVar(argWindow)
    dur.set(str(durationVals[buttonNum - 1]))
    durList = ["1", "2", "3", "4", "5"]
    duration_menu = OptionMenu(argWindow, dur, *durList)
    duration_menu.configure(width=13, height=2)
    duration_menu.place(x=40, y=90)
    
    tts = StringVar(argWindow)
    tts.set(str(ttsVals[buttonNum-1]))
    textVar = Entry(argWindow, bd=5, textvariable=tts)
    textVar.place(x=35, y=180)

    def done():
        speedVals[buttonNum - 1] = speed.get()
        durationVals[buttonNum - 1] = dur.get()
        ttsVals[buttonNum-1] = tts.get()
        argWindow.destroy()

    exitButton = Button(argWindow, bg="gray", width=8, height=2, text="Done", activebackground="red", command=done,
                        borderwidth=2, relief="groove")
    exitButton.place(x=65, y=255)

    argWindow.mainloop()


def getInstructions():
    #window.configure(bg="green")
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
            
    #print(instructions)
    for j, i in enumerate(instructions):
        if i == "move":
            inputs.moveCommand(speedVals[j], durationVals[j])
        elif i == "turn":
            inputs.turnCommand(speedVals[j], durationVals[j])
        elif i == "head tilt":
            inputs.headTiltCommand(speedVals[j])
        elif i == "head turn":
            inputs.headTurnCommand(speedVals[j])
        elif i == "waist":
            inputs.waistCommand(speedVals[j])
        elif i == "speech":
            inputs.speechCommand()
        elif i == "tts":
            inputs.tts(ttsVals[j])
        elif i == "":
            print("unknown function")


def callback(event):
    x = event.x
    y = event.y

    # print("X: " + str(x) + " Y: " + str(y))

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
    elif 475 < x < 525 and 25 < y < 100:
        createLabel(475, 25, "tts", "white")


inputs = KeyControl(window)
spawn()

window.bind("<Button-1>", callback)

window.mainloop()

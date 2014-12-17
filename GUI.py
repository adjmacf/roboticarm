#setup
import Tkinter, tkMessageBox, time, robotarm
top = Tkinter.Tk()
top.geometry("500x600")

#message routine
def completedmsg():
	tkMessageBox.showinfo("function not finished!", "incomplete")
	
#add buttons and stuff

PAP = Tkinter.Button(text="pick and place", command = completedmsg) #replace with pick and place routine

left = Tkinter.Button(text="left")
left.bind("<ButtonPress-1>", robotarm.ArmLeft)     #on button press move arm left
left.bind("<ButtonRelease-1>", robotarm.stopAll)   #on button release stop all movement

right = Tkinter.Button(text="right")
right.bind("<ButtonPress-1>", robotarm.ArmRight)
right.bind("<ButtonRelease-1>", robotarm.stopAll)

tiltup = Tkinter.Button(text="tilt up")
tiltup.bind("<ButtonPress-1>", robotarm.Up)
tiltup.bind("<ButtonRelease-1>", robotarm.stopAll)

tiltdown = Tkinter.Button(text="tilt down")
tiltdown.bind("<ButtonPress-1>", robotarm.Down)
tiltdown.bind("<ButtonRelease-1>", robotarm.stopAll)

mtiltup = Tkinter.Button(text="elbow tilt up")
mtiltup.bind("<ButtonPress-1>", robotarm.MiddleUp)
mtiltup.bind("<ButtonRelease-1>", robotarm.stopAll)

mtiltdown = Tkinter.Button(text="elbow tilt down")
mtiltdown.bind("<ButtonPress-1>", robotarm.MiddleDown)
mtiltdown.bind("<ButtonRelease-1>", robotarm.stopAll)

WristUp = Tkinter.Button(text="wrist up")
WristUp.bind("<ButtonPress-1>", robotarm.WristU) # WristU is the movement command
WristUp.bind("<ButtonRelease-1>", robotarm.stopAll)

WristDown = Tkinter.Button(text="wrist down")
WristDown.bind("<ButtonPress-1>", robotarm.WristD)
WristDown.bind("<ButtonRelease-1>", robotarm.stopAll)

gripclose = Tkinter.Button(text="grip")
gripclose.bind("<ButtonPress-1>", robotarm.grip)
gripclose.bind("<ButtonRelease-1>", robotarm.stopAll)

gripopen = Tkinter.Button(text="ungrip")
gripopen.bind("<ButtonPress-1>", robotarm.OpenGrip)
gripopen.bind("<ButtonRelease-1>", robotarm.stopAll)

lightButton = Tkinter.Button(text="light", command = robotarm.Light)
lightButton.pack()
lightButton.place(width=70, height=30, x=300, y=15)


#pack and place each button where it should go
tiltup.pack()
tiltup.place(width=70, height=30, x=25,y=55)

tiltdown.pack()
tiltdown.place(width=70, height=30, x=25, y=85)

left.pack()
left.place(width=70, height= 30, x=25, y=15)

right.pack()
right.place(width=70, height=30, x=95, y=15)

mtiltup.pack()
mtiltup.place(width=100, height=30, x=25, y=125)

mtiltdown.pack()
mtiltdown.place(width=100, height=30, x=25, y=155)

WristUp.pack()
WristUp.place(width=100, height=30, x=25, y=195)

WristDown.pack()
WristDown.place(width=100, height=30, x=25, y=225)

gripclose.pack()
gripclose.place(width=100, height=30, x=25, y=265)

gripopen.pack()
gripopen.place(width=100, height=30, x=125, y=265)

PAP.pack()
PAP.place(height=30, x=25, y=350)
top.mainloop()

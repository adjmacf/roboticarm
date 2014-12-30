#based on: https://github.com/lizquilty/roboticarm/blob/master/armtrol.py
#dependancies - pyusb


import usb.core, usb.util, time, Tkinter


#locate device and make sure its connected
RobotArm = usb.core.find(idVendor=0x1267, idProduct=0x000)
if RobotArm is None:
	raise ValueError("Arm not found!")


#movement functions
Duration = 1
def ArmMove(Duration, Cmd):
        RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, Cmd, 1000) #send data via usb
        time.sleep(Duration)
        Cmd = [0,0,0]
        RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, Cmd, 1000)
        
 
def stopAll(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [0,0,0], 1000)

def ArmRight(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [0,1,0], 1000)
	
def ArmLeft(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [0,2,0], 1000)
	
def Up(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [64,0,0], 1000)

def Down(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [128,0,0], 1000)

def MiddleUp(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [16,0,0], 1000)

def MiddleDown(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [32,0,0], 1000)

def WristU(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [4,0,0], 1000)

def WristD(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [8,0,0], 1000)

def grip(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [1,0,0], 1000)
	
def OpenGrip(one):
	RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [2,0,0], 1000)

def Light():
	Light.lightState = 1 - Light.lightState                    #inverts the light state
	if Light.lightState:
		RobotArm.ctrl_transfer(0x40, 6, 0x100, 0, [0,0,1], 1000)
	else:
		stopAll(1)
	
Light.lightState = 0

def blink():
	Light()
	time.sleep(0.5)
	Light()
	time.sleep(0.5)

def pickAndPlace():
	ArmRight()
	time.sleep(6)
	stopAll()
	
	MiddleDown()
	time.sleep(3)
	stopAll()
	
	grip()
	time.sleep(1.4)
	stopAll()
	
	MiddleUp()
	time.sleep(3.2)
	stopAll()
	
	ArmLeft()
	time.sleep(9)
	stopAll()
	
	MiddleDown()
	time.sleep(3)
	stopAll()
	
	OpenGrip()
	time.sleep(1.4)
	stopAll()
	
	MiddleUp()
	time.sleep(3.2)
	stopAll()
	
	ArmRight()
	time.sleep(3)
	stopAll()
	
	blink()
	blink()
	blink()
	

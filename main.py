import time
import random
import threading
import tkinter as tk
from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Listener
from PIL import Image,ImageTk

exit = "None"
startStop = "None"
maxCp = 8
minCp = 6
root = tk.Tk()
root.title("A.C")
root.geometry("205x400")
root.resizable(False, False)
bgimage = ImageTk.PhotoImage(Image.open("BGPic.png"))
root.iconphoto(False,bgimage)
background_label = tk.Label(root, image = bgimage).place(x=0, y=0, relwidth=1, relheight=1)



myLabel = tk.Label(root,bg="grey",text="Auto Clicker").grid(row = 0, column = 0)
blank = tk.Label(root,bg="grey").grid(row=1,column=0)
blank = tk.Label(root,bg="grey").grid(row=2,column=0)
def maxCps(var):
	maxCpsLabel = tk.Label(root,text="Max Cps: " + str(maxCps.get()),bg="grey")
	global maxCp
	maxCp = maxCps.get()
	maxCpsLabel.grid(row=7,column=0)
def minCps(var):
	minCpsLabel = tk.Label(root,text="Min Cps: " + str(minCps.get()),bg="grey")
	global minCp
	minCp = minCps.get()
	minCpsLabel.grid(row=3,column=0)
#MinCps Shit
	
minCps = tk.Scale(root,from_=3,to=12,orient=tk.HORIZONTAL,command=minCps, tickinterval=1.0,length= 200,bg="grey")
minCps.set(minCp)
minCps.grid(row=4,column=0)

minCpsLabel = tk.Label(root,text="Min Cps:",bg="grey")
minCpsLabel.grid(row=3,column=0)

blank = tk.Label(root,text="",bg="grey").grid(row=6,column=0)
#Max Cps 
maxCps = tk.Scale(root,from_=3,to=12,orient=tk.HORIZONTAL,command=maxCps, tickinterval=1.0,length = 200,bg="grey")
maxCps.set(maxCp) 
maxCps.grid(row=8,column=0)
maxCpsLabel = tk.Label(root,text="Max Cps:")
maxCpsLabel.grid(row=7,column=0)
#Blank Lines
blank = tk.Label(root,text="",bg="grey").grid(row=9,column=0)
blank = tk.Label(root,text="",bg="grey").grid(row=10,column=0)
#Start/Stop HotKey
def createHotKey():
	def on_press(key):
		try:
			print(' key {0} pressed'.format(key))
			
		except AttributeError:
			print('special key {0} pressed'.format(key))
	def on_release(key):
		global startStop
		startStop = key
		print("Your Hot Key is: " + str(startStop))
		return False
	with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:listener.join()
def updateHotKey():
	#startStopStr.set(startStop)
	startStopKeyLabel = tk.Label(root,text=startStop,font=("Courier", 22),bg="grey").grid(row=13,column=0)
startStopLabel = tk.Label(root,text="Stop/StartKey",bg="grey").grid(row=10,column=0)
startStopButton = tk.Button(root,text="Create HotKey:",command=createHotKey,bg="grey").grid(row=11,column=0)
updateButton = tk.Button(root,text="Update Key:",command=updateHotKey,bg="grey").grid(row=12,column=0)

errorThing = tk.StringVar()
errorThing.set("")
errorMessage = tk.Label(root,textvariable=errorThing,bg="grey").grid(row=5,column=0)
button = Button.left
def lclick():
	global button
	button = Button.left
	leftClick = tk.Button(root, text = "Left Click", command = lclick,bg="green",width = 10).grid(row=1,column=0)
	rightClick =tk.Button(root, text = "Right Click", command = rclick, bg="red",width = 10).grid(row=2,column=0)
def rclick():
	global button
	button = Button.right
	leftClick = tk.Button(root, text = "Left Click", command = lclick,bg="red",width = 10).grid(row=1,column=0)
	rightClick =tk.Button(root, text = "Right Click", command = rclick, bg="green",width = 10).grid(row=2,column=0)

leftClick = tk.Button(root, text = "Left Click", command = lclick,bg="green",width = 10).grid(row=1,column=0)
rightClick =tk.Button(root, text = "Right Click", command = rclick, bg="red",width = 10).grid(row=2,column=0)

#Auto Clicker Part

delay = (1/(random.randint(minCp,maxCp)));
running = False

mouse = Controller()

def start_clicking():
	running = True
	#run()

def stop_clicking():
	running= False

def exit():
	stop_clicking()


def loop():
	#print("Here is Max Cp:" + str(maxCp))
	#print("Here is Min Cp:" + str(minCp))
	if running:
		if(minCp <= maxCp):
			errorThing.set("")
			#print("HEre is max Cp:" + str(1/(maxCp+3)))
			if(minCp == maxCp):
				delay = (1/(maxCp))
			else:
				delay = (1/random.randint((minCp),(maxCp)));
			mouse.press(button)
			time.sleep(delay/2)			
			mouse.release(button)
			time.sleep(delay/2)	
			#print("Random CPS Given: " + str(delay))
			threading.Thread(target=loop).start()
		else:
			print("Min CPs is cant then Max Cps")
			errorThing.set("Error: MinCps > MaxCps")


def on_press2(key):
	global running
	if key == startStop:
		if running == False:
			running = True
			loop()
			print("")
		else:
			running = False
			print("")

#with Listener(on_press=on_press2) as listener:
	#listener.join()
listener = keyboard.Listener(on_press=on_press2)
listener.start()

#root.wm_attributes('-transparentcolor', background_label['bg'])
root.mainloop()

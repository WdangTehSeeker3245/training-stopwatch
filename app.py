from tkinter import *
from tkinter.ttk import *
import os 

sc=0; mn=0; hr=0; stp=0

def start():
	global sc,mn,hr,stp
	sc=sc+1
	if(sc==60):
		mn=mn+1
		sc=0
	if(mn==60):
		hr=hr+1
		mn=0
	if(stp==0):
		label=Label(root,text='%i:%i:%i'%(hr,mn,sc),font=('arial',30,'bold'),foreground='red',background='#424B52',width=10)
		label.after(300,start)
		label.place(x=85,y=230)

def stop():
	global stp
	stp=1

def startnew():
	global sc,mn,hr,stp
	sc=0; mn=0; hr=0; stp=0
	label=Label(root,text='%i:%i:%i'%(hr,mn,sc),font=('arial',30,'bold'),foreground='red',background='#424B52',width=10)
	label.after(300,start)
	label.place(x=85,y=230)

root =Tk(); style=Style()
root.title("Faizal Stopwatch Training")
root.geometry("280x320")
root.resizable(False,False)
root.configure(bg="#424B52")

label2 = Label(root,text="STOPWATCH APP",background='#424B52',foreground='white',font=('arial',12,'bold'))
label2.place(x=70,y=20)

basedir = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(basedir,"izaus-linux.png")
img = PhotoImage(file = icon)
label3 = Label(root,image=img,background='#424B52')
label3.place(x=90,y=55)

style.configure('TButton',font=('arial',8,'bold'),borderwidth='3')
botton1=Button(root,text="Start",command=startnew).place(x=40,y=175)
button2=Button(root,text="Stop",command=stop).place(x=170,y=175)

root.mainloop()

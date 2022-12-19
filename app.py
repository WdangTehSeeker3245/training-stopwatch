from tkinter import *
from tkinter.ttk import *

sc=0; mn=0; hr=0; stp=0

def start():
	global sc,mn,hr
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
		label.place(x=65,y=220)

def stop():
	global stp
	stp=1

root =Tk(); style=Style()
root.title("Faizal Stopwatch Training")
root.geometry("240x300")
root.resizable(False,False)
root.configure(bg="#424B52")

label2 = Label(root,text="STOPWATCH APP",background='#424B52',foreground='white',font=('arial',12,'bold'))
label2.place(x=50,y=20)

img = PhotoImage(file = r"/home/izaus/IzausLab/Project/training-stopwatch/izaus-linux.png")
label3 = Label(root,image=img,background='#424B52')
label3.place(x=70,y=55)

style.configure('TButton',font=('arial',10,'bold'),borderwidth='5')
botton1=Button(root,text="Start",command=start).place(x=20,y=175)
button2=Button(root,text="Stop",command=stop).place(x=140,y=175)

root.mainloop()

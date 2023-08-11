from tkinter import *
import time
from tkinter.messagebox import *
from tkinter import messagebox
import customtkinter as ct
import tkinter as Tkinter
from datetime import datetime
import winsound
import datetime

def f1():
	wc_window.deiconify()
	cl_window.withdraw()
def f2():
	cl_window.deiconify()
	wc_window.withdraw()
def f3():
	sw_window.deiconify()
	cl_window.withdraw()
def f4():
	cl_window.deiconify()
	sw_window.withdraw()
def f5():
	cd_window.deiconify()
	cl_window.withdraw()
def f6():
	cl_window.deiconify()
	cd_window.withdraw()
def f7():
	al_window.deiconify()
	cl_window.withdraw()
def f8():
	cl_window.deiconify()
	al_window.withdraw()




# Clock Window--------------
cl_window = Tk() 
cl_window.title("Digital Clock") 
cl_window.geometry("700x500+100+100") 
cl_window.resizable(0,0)
text_font= ("Boulder", 28, 'bold')

img=PhotoImage(file="Ms.png")
photo_label=ct.CTkLabel(cl_window,text=" ",fg_color="#202630",image=img,width = 30 ,height = 40)
photo_label.place(x=0,y=0)
cl_window.iconphoto(False,img)
cl_window.iconbitmap("Cl.ico")

cl_lab = Label(cl_window,text="Current Time",width=2,height=1,bg="#06283D",fg='White',font='airal 20 bold',anchor='n')
cl_lab.pack(side=TOP,fill=X)
label2 = Label(cl_window, font=text_font,background = "Black",foreground = "cyan") 
label2.pack(pady=20, anchor=CENTER)


bt2 = ct.CTkButton(cl_window,text = "StopWatch",font = text_font ,width = 2,command = f3)
bt2.pack(pady=10,anchor=CENTER)
bt3 = ct.CTkButton(cl_window,text = "CountDown",font = text_font ,width = 2,command = f5)
bt3.pack(pady=10,anchor=CENTER)
bt4 = ct.CTkButton(cl_window,text = "Alarm",font = text_font ,width = 2,command = f7)
bt4.pack(pady=10,anchor=CENTER)
bt5 = ct.CTkButton(cl_window,text = "WorldClock",font = text_font ,width = 2,command = f1)
bt5.pack(pady=10,anchor=CENTER)


def digital_clock(): 
   time_live = time.strftime("%H:%M:%S %p")
   label2.config(text=time_live) 
   label2.after(200, digital_clock)

digital_clock()

# Stopwatch Window -----------

counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
   
            if counter==66600:            
                display="Starting..."
            else:
                tt = datetime.datetime.fromtimestamp(counter)
                string = tt.strftime("%D:%H:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
         
            label.after(1000, count) 
            counter += 1
   
   
    count()     
   

def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
   

def Reset(label):
    global counter
    counter=66600
   
    
    if running==False:      
        reset['state']='disabled'
        label['text']='Welcome!'
   
   
    else:               
        label['text']='Starting...'
   
sw_window = Tkinter.Toplevel(cl_window)
sw_window.title("Stopwatch")
sw_window.resizable(0,0)
  
sw_window.geometry("700x500+100+100") 
img=PhotoImage(file="Ms.png")
photo_label=ct.CTkLabel(sw_window,text=" ",fg_color="#202630",image=img,width = 30 ,height = 40)
photo_label.place(x=0,y=0)
cl_window.iconphoto(False,img)
sw_window.iconbitmap("Cl.ico")

sw_lab = Label(sw_window,text="Stop Watch",width=2,height=1,bg="#06283D",fg='White',font='airal 20 bold',anchor='n')
sw_lab.pack(side=TOP,fill=X)


label = Tkinter.Label(sw_window, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack(pady=70)
f = Tkinter.Frame(sw_window)

start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")


btn1 = Tkinter.Button(sw_window,text ="Back",font=("Boulder", 28, 'bold'),background = "Black" ,foreground = "Cyan",command = f4)
btn1.pack(pady=50)
sw_window.withdraw()


# CountDown -------------

cd_window = Toplevel(cl_window)

cd_window.geometry("700x500+100+100")

cd_window.title("Time Counter")
cd_window.resizable(0,0)
cd_window.title("Time Counter")
img=PhotoImage(file="Ms.png")
photo_label=ct.CTkLabel(cd_window,text=" ",fg_color="#202630",image=img,width = 30 ,height = 40)
photo_label.place(x=0,y=0)
cd_window.iconphoto(False,img)
cd_window.iconbitmap("Cl.ico")

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry= Entry(cd_window, width=3, font=("Arial",18,""),
				textvariable=hour)
hourEntry.place(x=280,y=150)

minuteEntry= Entry(cd_window, width=3, font=("Arial",18,""),
				textvariable=minute)
minuteEntry.place(x=330,y=150)

secondEntry= Entry(cd_window, width=3, font=("Arial",18,""),
				textvariable=second)
secondEntry.place(x=380,y=150)

def submit():
	try:
		temp =  int(minute.get())*60 + int(second.get())


	except:
		print("Please input the right value")
	while temp >-1:
		
		
		mins,secs = divmod(temp,60)

		
		hours=0
		if mins >60:
			
			
			hours, mins = divmod(mins, 60)
		
		
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		
		cd_window.update()
		time.sleep(1)

		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time's up ")
			
		temp -= 1
		
		


cdt = Label(cd_window,text = 'CountDown Timer',font=("Boulder", 28, 'bold'))
cdt.place(x=195,y=50)
btn = Button(cd_window, text='Set Time Countdown',bd=5,fg="Black",bg="#D4AC0D",width = 20,font=(10),command= submit)
btn.place(x = 235,y = 220)
btn1 = Button(cd_window,text ="Back",font=("Boulder", 28, 'bold'),background = "Black" ,foreground = "Cyan",command = f6)
btn1.place(x=289,y=280)
cd_window.withdraw()


# ALARM ---------------

def Alarm(set_alarm_timer):
	while True:
		time.sleep(1)
		actual_time = datetime.datetime.now()
		cur_time = actual_time.strftime("%H:%M:%S")
		cur_date = actual_time.strftime("%d/%m/%Y")
		msg="Current Time: "+str(cur_time)
		print(msg)
		if cur_time == set_alarm_timer:
			winsound.PlaySound("Musicwave.wav",winsound.SND_ASYNC)
			messagebox.showinfo("Alarm", "Time's up ")
			break
	
	
 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
 
al_window = Toplevel(cl_window)
al_window.title("Alarm Clock")
al_window.geometry("700x500+100+100")

img=PhotoImage(file="Ms.png")
photo_label=ct.CTkLabel(al_window,text=" ",fg_color="#202630",image=img,width = 30 ,height = 40)
photo_label.place(x=0,y=0)
al_window.iconphoto(False,img)
al_window.iconbitmap("Cl.ico")

al_window.resizable(width=False,height=False)
 
time_format=Label(al_window, text= "Remember to set time in 24 hour format!", background = "Black" ,foreground = "Cyan",font=("Arial",20)).place(x=100,y=50)
addTime = Label(al_window,text = "Hour     Min     Sec",font=60,background = "Black" ,foreground = "Cyan").place(x = 280,y=90)
setYourAlarm = Label(al_window,text = "Set Time for Alarm: ",background = "Black" ,foreground = "Cyan",relief = "solid",font=("Helevetica",15,"bold")).place(x=70, y=130)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
 
hourTime= Entry(al_window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=280,y=130)
minTime= Entry(al_window,textvariable = min,bg = "#48C9B0",width = 4,font=(20)).place(x=340,y=130)
secTime = Entry(al_window,textvariable = sec,bg = "#48C9B0",width = 4,font=(20)).place(x=400,y=130)
 
submit = Button(al_window,text = "Set Your Alarm",bd=5,fg="Black",bg="#D4AC0D",width = 15,command = get_alarm_time,font=(20)).place(x =280,y=190)

btn1 = Button(al_window,text ="Back",font=("Boulder", 28, 'bold'),background = "Black" ,foreground = "Cyan",command = f8)
btn1.place(x=306,y=280) 
al_window.withdraw()



# WorldClock --------------

import pytz

wc_window = Toplevel(cl_window)
wc_window.geometry("700x500+100+100")
wc_window.resizable(0,0)


img=PhotoImage(file="Ms.png")
photo_label=ct.CTkLabel(wc_window,text=" ",fg_color="#202630",image=img,width = 30 ,height = 40)
photo_label.place(x=0,y=0)
wc_window.iconphoto(False,img)
wc_window.iconbitmap("Cl.ico")

def times():
	home = pytz.timezone('Asia/Kolkata')
	local_time = datetime.datetime.now(home)
	current_time = local_time.strftime("%H:%M:%S")
	clock.config(text=current_time)
	name.config(text="India")
	

	home = pytz.timezone('Australia/Victoria')
	local_time = datetime.datetime.now(home)
	current_time = local_time.strftime("%H:%M:%S")
	clock1.config(text=current_time)
	name1.config(text="Australia")
	
	
	home = pytz.timezone('Africa/Timbuktu')
	local_time = datetime.datetime.now(home)
	current_time = local_time.strftime("%H:%M:%S")
	clock2.config(text=current_time)
	name2.config(text="Africa")
	

	home = pytz.timezone('America/New_york')
	local_time = datetime.datetime.now(home)
	current_time = local_time.strftime("%H:%M:%S")
	clock3.config(text=current_time)
	name3.config(text="America")
	clock.after(200,times)
	


name = Label(wc_window,font=("times",20,"bold"),background = "blue" ,foreground = "white")
name.place(x=150,y=100)
clock = Label(wc_window,font=("times",25,"bold"),background = "black" ,foreground = "red")
clock.place(x=120,y=140)
nota = Label(wc_window,text="Hours mintues seconds",font="times 10 bold",background = "white" ,foreground = "black")
nota.place(x=120,y=185)


name1 = Label(wc_window,font=("times",20,"bold"),background = "blue" ,foreground = "white")
name1.place(x=450,y=100)
clock1 = Label(wc_window,font=("times",25,"bold"),background = "black" ,foreground = "red")
clock1.place(x=440,y=140)
nota1 = Label(wc_window,text="Hours mintues seconds",font="times 10 bold",background = "white" ,foreground = "black")
nota1.place(x=440,y=185)

name2 = Label(wc_window,font=("times",20,"bold"),background = "blue" ,foreground = "white")
name2.place(x=150,y=215)
clock2 = Label(wc_window,font=("times",25,"bold"),background = "black" ,foreground = "red")
clock2.place(x=120,y=250)
nota2 = Label(wc_window,text="Hours mintues seconds",font="times 10 bold",background = "white" ,foreground = "black")
nota2.place(x=120,y=290)


name3 = Label(wc_window,font=("times",20,"bold"),background = "blue" ,foreground = "white")
name3.place(x=450,y=215)
clock3 = Label(wc_window,font=("times",25,"bold"),background = "black" ,foreground = "red")
clock3.place(x=440,y=250)
nota3 = Label(wc_window,text="Hours mintues seconds",font="times 10 bold",background = "white" ,foreground = "black")
nota3.place(x=440,y=290)

btn1 = Button(wc_window,text ="Back",font=("Boulder", 28, 'bold'),background = "Black" ,foreground = "Cyan",command = f2)
btn1.place(x=289,y=350)

times()
wc_window.withdraw()



def on_closing():
	if askyesno("QUIT","Do u want to exit?"):
		cl_window.destroy()

cl_window.protocol("WM_DELETE_WINDOW", on_closing)
sw_window.protocol("WM_DELETE_WINDOW", on_closing)
cd_window.protocol("WM_DELETE_WINDOW", on_closing)
al_window.protocol("WM_DELETE_WINDOW", on_closing)
wc_window.protocol("WM_DELETE_WINDOW", on_closing)


cl_window.mainloop()
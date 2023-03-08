from tkinter import *
import datetime
import time
import winsound
clock = Tk()
clock.configure(background="#3C2A21")

def alarm(alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date is :", date)
        print("the current time is",now)
        if now == alarm_timer:
            print("its time to wake upp!!!!!!")
            winsound.PlaySound("bird.wav", winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
clock.title("Welcome to Alarm Clock")
clock.geometry("400x300")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="#1A120B",font="Arial").place(x=70,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60 , fg="white", bg="#3C2A21").place(x = 110)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime = Entry(clock,textvariable = hour,bg = "#1A120B",insertbackground="white",width = 15, fg ="white").place(x=110,y=30)
minTime = Entry(clock,textvariable = min, bg = "#1A120B",insertbackground="white", width = 15,fg ="white").place(x = 150,y= 30)
secTime = Entry(clock,textvariable = sec,bg = "#1A120B",insertbackground="white", width = 15,fg ="white").place(x=190,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="#F94A29",width = 10,command = actual_time).place(x =160,y=70)
clock.mainloop()

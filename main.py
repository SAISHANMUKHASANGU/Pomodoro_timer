from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    for i in range(0,10):
        if count_sec==i:
            count_sec=f"{0}{i}"

    canvas.itemconfig(text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start()
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Timer")
window.config(padx=50,pady=50,bg=GREEN)

label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=RED,background=GREEN)
label.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,background=GREEN,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")

canvas.grid(row=1,column=1)

def start():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    reps=reps+1
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break")

        reps=0
    elif reps%2==0:
        count_down(short_break_sec)
        label.config(text="Short Break")
        reps=reps+1
    else:
        count_down(work_sec)
        label.config(text="Work")


start_button=Button(text="Start",command=start)
start_button.grid(row=2,column=0)

def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(text,text="00:00")
    label.config(text="timer")
    check_mark.config(text="")
    reps=0

reset_button=Button(text="Reset",command=reset)
reset_button.grid(row=2,column=2)

check_mark=Label(fg=RED,background=GREEN)
check_mark.grid(row=3,column=1)

window.mainloop()
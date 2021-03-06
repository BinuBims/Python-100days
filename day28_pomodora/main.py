
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

from os import startfile
from tkinter import *
import math

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    timer_label.config(text="Timer")
    check_label.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    reps = 0  

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    
    if count_sec<10:
        count_sec=f"{0}{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000,count_down,count-1)
    else:
        if reps % 2 == 0:
            check_label.config(text=int(reps/2)*"✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg = GREEN, background=YELLOW)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomoto_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

star_button = Button(text="start", command=start_timer)
star_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

check_label = Label(font=(FONT_NAME, 25), fg=GREEN, background=YELLOW)
check_label.grid(column=1,row=3)










window.mainloop()




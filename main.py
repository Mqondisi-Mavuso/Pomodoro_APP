# day 28 of 100 days of python bootcamp
# Pomodoro app

from tkinter import *
import math
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
timer_reset = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer_reset
    window.after_cancel(timer_reset)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_box.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 0:                       # meaning it is odd
        count_down(short_break)
        title_label.config(text="Break", fg=PINK)

    elif reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED)

    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"                                                    # dynamic typing
    elif count_sec < 10 and count_sec % 10 != 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")           # for changing the count on GUI
    if count > 0:
        global timer_reset
        timer_reset = window.after(1000, count_down, count - 1)       # Count down every second

    else:                                           # This is triggered whenever the count has reached zero
        start_timer()
        if reps % 2 == 0:                           # for every two reps there should be one marker
            check_box_maker = ""
            ticks = int(reps/2)                     # here we are checking how many ticks should be printed
            for _ in range(ticks):                  # since we can't use float in range(), ticks had to be type casting
                check_box_maker += "✔"
            check_box.config(text=check_box_maker)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=("Times New Roman", 24, "bold"))
title_label.config(bg=YELLOW)
title_label.grid(row=0, column=1)


check_box = Label(font=("Times New Roman", 24, "bold"))
check_box.config(bg=YELLOW)
check_box.config(fg=GREEN)
check_box.grid(row=3, column=1)                # This allows the label to be shown on the screen


start_button = Button(text="Start", command=start_timer, highlightthickness=0)     # listens to click from user, click()
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)     # listens to click from user
reset_button.grid(row=2, column=2)



window.mainloop()

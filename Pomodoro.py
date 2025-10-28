# Pomodoro Technique App using Python

from tkinter import *
import math

#  CONSTANTS
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

# Timer Reset


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# Timer Mechanism


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_label.config(
            text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED
        )
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(
            text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK
        )
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(
            text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN
        )
        count_down(WORK_MIN * 60)


# CountDown Mechanism


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


# UI Setup

# Window

window = Tk()
window.title("Pomodoro")
window.minsize(400, 290)
window.config(padx=100, pady=50, bg=YELLOW)

# Label

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

check_mark = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3, padx=5, pady=5)

# Canvas Img

canvas = Canvas(width=200, height=224, bg=YELLOW)
img = PhotoImage(file="28thDay/Tomato.png")
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(
    102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(column=1, row=1)

# Buttons

button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2, padx=5, pady=5)

button2 = Button(text="Restart", command=reset_timer)
button2.grid(column=2, row=2, padx=5, pady=5)

window.mainloop()

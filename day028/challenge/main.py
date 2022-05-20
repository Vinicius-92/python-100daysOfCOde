import math
from tkinter import *
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


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time_set, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    if reps % 8 == 0:
        header.config(text="Long break", fg=RED)
        count_down(long_sec)
    elif reps % 2 == 0:
        header.config(text="Short break", fg=PINK)
        count_down(short_sec)
    else:
        header.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_set, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Label
header = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
header.grid(column=1, row=0)
# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_set = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# Buttons
start = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)
# Concluded
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()

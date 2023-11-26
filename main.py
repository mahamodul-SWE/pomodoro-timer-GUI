from tkinter import *
import math
# ---------------------------- CONSTANTS and Global variable ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # to check repetition of timer
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)  # for cancel windowloop
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0  # reset the reps


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brk_sec = SHORT_BREAK_MIN * 60
    long_brk_sec = LONG_BREAK_MIN * 60

    # to check status of timer
    if reps % 8 == 0:
        count_down(long_brk_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brk_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # showing countdown

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # reducing countdown
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)

        for i in range(work_session):
            marks = "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Making Main Window
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


# Title Label
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, "25", "bold"))
title_label.grid(column=1, row=0)

# canvas UI
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)


# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

# Checkmark for completion of every work session
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# mainloop for looping the whole GUI
window.mainloop()

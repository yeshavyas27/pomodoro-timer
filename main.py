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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    #change time to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #reset text to timer
    title_label.config(text="Timer")
    #reset checkmarks to none
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    #if 2,4,6 rep--break
    if reps % 2 == 0 and reps < 7:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
    #for 1,3,5,7 reps--work
    else:
        title_label.config(text="CODE", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec_remaining = count % 60
    if count_sec_remaining < 10:
        count_sec_remaining = f"0{count_sec_remaining}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec_remaining}")

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        checks = ""
        work_session = range(math.floor(reps/2))
        for _ in work_session:
            checks += "✔"
        checkmark.config(text=checks)

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)



tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)



reset_buttton = Button(text="Reset", command=reset_timer)
reset_buttton.grid(column=2, row=2)


checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()
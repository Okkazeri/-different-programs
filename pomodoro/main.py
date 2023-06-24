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
REPS = 0
DATA = ""
timer = None

if __name__ == "__main__":
    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer():
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        Timer_label.config(text="Timer", fg=GREEN)
        checkmark.config(text="")


    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer():
        global REPS
        REPS += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if REPS == 8:
            Timer_label.config(text="Break", fg=RED)
            countdown(long_break_sec)
        elif REPS % 2 == 0:
            Timer_label.config(text="Break", fg=PINK)
            countdown(short_break_sec)
        else:
            Timer_label.config(text="Work", fg=GREEN)
            countdown(work_sec)


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def countdown(count):
        global REPS
        global DATA
        count_minutes = math.floor(count / 60)
        count_sec = count % 60

        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_sec}")
        if count > 0:
            global timer
            timer = window.after(1000, countdown, count - 1)
        else:
            start_timer()
            if REPS > 1 and REPS % 2 == 1:
                DATA += "✔"
                checkmark.config(text=DATA)


    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 132, text='00:00', fill="white", font=("Arial", 20))
    canvas.grid(column=1, row=1)

    Timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34, 'bold'), bg=YELLOW)
    Timer_label.grid(column=1, row=0)
    # ✔

    Start_button = Button(text="Start", highlightthickness=0, command=start_timer)
    Start_button.grid(column=0, row=2)

    Reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
    Reset_button.grid(column=2, row=2)

    checkmark = Label(fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
    checkmark.grid(column=1, row=3)

    window.mainloop()

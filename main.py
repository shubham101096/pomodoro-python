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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global timer
    window.after_cancel(timer)
    check_mark.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Long break", fg=PINK)
        count_down(60*LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="Short break", fg=RED)
        count_down((60*SHORT_BREAK_MIN))
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(60*WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    min = int(count/60)
    sec = count%60
    if sec < 10:
        sec = "0"+str(sec)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        start_timer()
        if reps%2 == 0:
            check_string = ""
            for _ in range(int(reps/2)):
                check_string += "✅"
            check_mark.config(text=check_string)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
timer_label.grid(row=0, column=1)


start_btn = Button(text="Start", font=(FONT_NAME, 20, "bold"), command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", font=(FONT_NAME, 20, "bold"), command=reset)
reset_btn.grid(row=2, column=2)

check_mark = Label(text="",bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
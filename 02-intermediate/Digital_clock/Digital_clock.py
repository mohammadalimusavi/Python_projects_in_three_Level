import tkinter as tk
import datetime

# ---------------------------
# make a screen
# ---------------------------

root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Digital Clock")

# ---------------------------
# Clock Frame
# ---------------------------

frame = tk.Frame(root)

label_hour = tk.Label(
    frame,
    fg="white",
    bg="black",
    font=("Arial", 20, "bold"),
    width=5,
    height=1
)

label_minute = tk.Label(
    frame,
    fg="white",
    bg="black",
    font=("Arial", 20, "bold"),
    width=5,
    height=1
)

label_second = tk.Label(
    frame,
    fg="white",
    bg="black",
    font=("Arial", 20, "bold"),
    width=5,
    height=1
)


label_second.grid(padx=5, pady=5, row=0, column=2)
label_minute.grid(padx=5, pady=5, row=0, column=1)
label_hour.grid(padx=5, pady=5, row=0, column=0)

frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------------------------
# Update Clock
# ---------------------------

def update_clock():

    now = datetime.datetime.now()

    label_hour.config(text=f"{now.hour:02}")
    label_minute.config(text=f"{now.minute:02}")
    label_second.config(text=f"{now.second:02}")

    root.after(1000, update_clock)

update_clock()

root.mainloop()
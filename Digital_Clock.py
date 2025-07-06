import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")

def time():
    string = strftime('%H:%M:%S %p \n %d %B %Y, %A')
    label.config(text=string)
    label.after(1000,time)

box = tk.Frame(root, bg="#F57F7F", bd=25, relief=tk.RIDGE)
box.place(relx=0.5, rely=0.5, anchor='center', relheight=1, relwidth=1)

tk.Label(box, text="DIGITAL CLOCK", bg="#000000", font=("consolas", 30), fg="white").pack(pady=10, fill="x")

label = tk.Label(box, font=('ariel',75,'bold'), background='black', foreground='white', width=20, height=5)
label.pack(anchor='center', expand=True)

time()

root.mainloop()
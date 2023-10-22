import tkinter as tk
from time import strftime

def time():
    string = strftime('%Y/%m/%d %A\n%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title("Big Clock")

label = tk.Label(root, font=('calibri', 80, 'bold'), background='black', foreground='green')
label.pack(anchor='center')

time()

root.mainloop()

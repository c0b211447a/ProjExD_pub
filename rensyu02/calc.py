
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    num = button["text"]
    entry.insert(tk.END, num)

root = tk.Tk()
root.geometry("300x450")

entry = tk.Entry(root, 
                justify="right", 
                width=10,
                font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=4)

r , c = 1, 1
for i,num in enumerate(range(9,-1,-1), 1):
    button = tk.Button(root, text=num, font=("Times New Roman", 30))
    button.grid(row=r, column = c, padx=10, pady=10)
    button.bind("<1>", button_click)
    if i%3 == 0:
        r += 1
        c = 0
    c += 1
    button.grid()



root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("300x450")

r , c = 0, 1
for i,num in enumerate(range(9,-1,-1), 1):
    button = tk.Button(root, text=num, font=("Times New Roman", 30))
    button.grid(row=r, column = c, padx=10, pady=10)
    if i%3 == 0:
        r += 1
        c = 0
    c+=1
    button.grid()

root.mainloop()
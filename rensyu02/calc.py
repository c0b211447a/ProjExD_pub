
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    num = button["text"]
    entry.insert(tk.END, num)

def equal_click(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END,str(res))

root = tk.Tk()
root.geometry("300x450")

entry = tk.Entry(root, 
                justify="right", 
                width=10,
                font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=4)

r , c = 1, 1
for i,num in enumerate([7,8,9,4,5,6,1,2,3,"+",0], 1):
    button = tk.Button(root, text=num, font=("Times New Roman", 30))
    button.grid(row=r, column = c, padx=10, pady=10)
    button.bind("<1>", button_click)
    if i%3 == 0:
        r += 1
        c = 0
    c += 1
    
button = tk.Button(root, 
                  text="=", 
                  font=("Times New Roman", 30)
                  )
button.grid(row=r, column = c, padx=10, pady=10)
button.bind("<1>", equal_click)

root.mainloop()
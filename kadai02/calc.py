import tkinter as tk
from  tkinter import messagebox as tkm
import tkinter

calc =  tk.Tk()
calc.geometry("300x450")
calc.title = ("電卓")

entry = tk.Entry(justify = "right", width = 10, font = ("Times New Roman",40))
entry.grid(row = 0, columnspan = 10)

def button_click(event):
    btn = event.widget
    #button["bg"]="gray"
    txt = btn["text"]
    if txt=="−":
        entry.insert(tk.END,"-")
    elif txt=="×":
        entry.insert(tk.END,"*")
    else:
        entry.insert(tk.END, txt)
    #tkm.showinfo(txt, f"[{txt}]ボタンがクリックされました")

def equal(event):
    siki = entry.get()
    entry.delete(0, tk.END)
    kotae = eval(siki)
    entry.insert(tk.END, kotae)
    
def delete(event):
    entry.delete(0, tk.END)
   
fonts = ("Times New Roman", 20)
fonts2=("Times New Roman", 10)
x = 0
list = [[7,1],[6,2],[6,1],[6,0],[5,2],[5,1],[5,0],[4,2],[4,1],[4,0]]
for i in list:
    button = tk.Button(text= x,font=fonts,width = 4, height = 1)
    button.bind("<1>", button_click)
    button.grid(row = i[0],column = i[1],padx=2,pady = 4)
    x += 1

    
buttonequal = tk.Button(text='=',font=fonts,width = 4, height = 1,background = "gray")
buttonequal.bind("<1>", equal)
buttonequal.grid(row = 7,column = 4,padx=2,pady = 4)

buttonDel = tk.Button(text='AC',font=fonts,width = 4, height = 1,background = "gray")
buttonDel.bind("<1>", delete)
buttonDel.grid(row = 2,column = 4,padx=2,pady = 4)


list1 = [["+"],['−'],['×'],['/']]
y = 3
for i in list1:
    button = tk.Button(text= i,font=fonts,width = 4, height = 1,background = "gray")
    button.bind("<1>", button_click)
    button.grid(row = y,column = 4,padx=2,pady = 4)
    y += 1

list1 = [['('],[')'],["C"]]
y = 0
for i in list1:
    button = tk.Button(text= i,font=fonts,width = 4, height = 1,background = "gray")
    if y==2:
        button.bind("<1>", button_delete2)
    else:
        button.bind("<1>", button_click)
    button.grid(row = 3,column = y,padx=2,pady = 4)
    y += 1
def button_delete2(event):
    entry.delete(len(entry.get())-1,tk.END)
calc.mainloop()

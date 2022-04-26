import tkinter as tk
import tkinter.messagebox as tkm
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x450')
    button_list = []
    r=5
    c=3
    def button_click(event):
        btn = event.widget
        entry.insert(tk.END, btn['text'])
    def evel(event):
        lit = entry.get()
        ans = 0
        if '+' in lit:
            nums = lit.split('+')
            for i in nums:
                ans += int(i)

        if '-' in lit:
            nums = lit.split('-')
            for i in nums:
                ans -= int(i)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(ans))


    def b_clear(event):
        new = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, new[:-1])

    def b_aclear(event):
        entry.delete(0, tk.END)   

    entry = tk.Entry(width=10,
                    justify='right',
                    font=('Times New Roman', 40)
                    )
    entry.grid(column=0, row=0, columnspan=4, rowspan=1)
    for i in range(10):
        button = tk.Button(root, text=i,
                            font=('Times New Roman', 30)
                            )
        
        if r == 5:
            c = 0
            button.grid(row = r, column=c, padx=0, pady=0)
            button_list.append(button)
            r -= 1
            c = 2
            continue
        if c == 0:
            button.grid(row = r, column=c, padx=0, pady=0)
            button_list.append(button)
            r -= 1
            c = 2
            continue
        
        button.grid(row=r, column=c, padx=0, pady=0)
        button_list.append(button)
        c -= 1
    
    for i in button_list:
        i.bind('<1>', button_click)
    
    button_plus = tk.Button(root, text='+',
                            font=('Times New Roman', 30)
                            )
    button_plus.bind('<1>', button_click)
    
    button_plus.grid(row=5, column=1, padx=0, pady=0)
    button_equal = tk.Button(root, text='=',
                            font=('Times New Roman', 30)
                            )
    button_equal.bind('<1>', evel)
    button_equal.grid(row=5, column=2)

    button_clear = tk.Button(root, text='C',
                            font=('Times New Roman', 30)
                            )
    button_clear.bind('<1>', b_clear)
    button_clear.grid(row=5, column=3)

    button_aclear = tk.Button(root, text='AC',
                            font=('Times New Roman', 30)
                            )
    button_aclear.bind('<1>', b_aclear)
    button_aclear.grid(row=4, column=3)

    root.mainloop() 
0 comments on commit 85b78e4

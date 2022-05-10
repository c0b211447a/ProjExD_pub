import tkinter as tk
import maze_maker as mm

index = 0

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key =""
#clickボタン関数
def btn_click():
	global index
	index=(index+1) % len(photos)
	canvas.delete('tori')	
	canvas.create_image(cx,cy,image=photos[index],tag='tori')
#こうかとんの壁判定
def main_proc():
    global cx, cy, mx, my, key
    delta = {
            'Up': [0, -1],
            'Down':[0, +1] ,
            'Left':[-1 , 0] ,
            'Right':[+1, 0] ,
            }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            mx += delta[key][0]
            my += delta[key][1]
    except:
        pass
    cx, cy = 100*mx+50, 100*my+50
    canvas.coords('tori', cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15, 9) #壁:1床:0の二次元リストを表す
    mm.show_maze(canvas, maze_bg)#迷路を表示

    photos=[
        tk.PhotoImage(file="fig/0.png"),
        tk.PhotoImage(file="fig/1.png"),
        tk.PhotoImage(file="fig/2.png"),
        tk.PhotoImage(file="fig/3.png"),
        tk.PhotoImage(file="fig/4.png"),
        tk.PhotoImage(file="fig/5.png"),
        tk.PhotoImage(file="fig/6.png"),
        tk.PhotoImage(file="fig/7.png"),
        tk.PhotoImage(file="fig/8.png"),
        tk.PhotoImage(file="fig/9.png"),
        ]

    mx, my = 1, 1
    cx, cy = 100*mx + 50, 100*my + 50#初期位置を設定
    canvas.create_image(cx, cy, image=photos[index], tag="tori")#こうかとんを表示
    btn=tk.Button(text ="Click",command=btn_click)
    btn.pack(ipadx=10,ipady=5)

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.after(100, main_proc)
    root.mainloop()


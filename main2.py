def klava(e):

    if e.keysym == "Up":
        canvas.move(oval,0,-50)
    if e.keysym == "Down":
        canvas.move(oval, 0, 50)
import tkinter as tk
win = tk.Tk()
canvas = tk.Canvas(win,bg ="white", height=400, width=400)
pula=canvas.create_oval((500,500),(500,500),fill="yellow")
oval=    canvas.create_oval((0,0),(50,50),fill="red")
canvas.pack()
win.bind("<KeyPress>",klava)
canvas.mainloop()

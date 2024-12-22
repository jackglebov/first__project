import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win,bg ="white", height=400, width=400)
for i in range(50,400,50):
    canvas.create_line((0,i), (400,i))
    canvas.create_line((i, 0), (i, 400))
for t in range(50, 400, 100):
    canvas.create_oval((t,0),(t-50,50),fill="red")
    for t in range(50, 400, 100):
        canvas.create_oval((t, 50), (t +50, 100), fill="red")
    for t in range(50, 400, 100):
        canvas.create_oval((t, 100), (t -50, 150), fill="red")
    for t in range(50, 400, 100):
        canvas.create_oval((t, 300), (t +50, 250), fill="blue")
    for t in range(50, 400, 100):
        canvas.create_oval((t, 350), (t - 50, 300), fill="blue")
    for t in range(50, 400, 100):
        canvas.create_oval((t, 400), (t+ 50, 350), fill="blue")
    canvas.pack()
canvas.mainloop()

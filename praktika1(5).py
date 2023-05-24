import tkinter as tk
win = tk.Tk()
#photo = tk.PhotoImage(file='icon.png')
#win.iconphoto(False, photo)
win.title("Мое первое приложение")
win.geometry("500x600")
win.minsize(300,400)
win.maxsize(600,500)
win.config(bg = '#43BDB1')

lb = tk.Label(win, text='Hello Arzygul',
              bg = 'yellow')
lb.pack()
win.mainloop()

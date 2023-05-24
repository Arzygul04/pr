from tkinter import*
window = Tk()
window.title('Размещение виджетов')
window.geometry('300x300')
#kn1 = Button(text='1')
#kn1.pack(side='left')
#kn2 = Button(text='2')
#kn2.pack(side='left')
#kn3 = Button(text='3')
#kn3.pack()
#kn4 = Button(text='4')
#kn4.pack()


kn5 = Button(window,text='11')
kn5.grid(row = 0, column = 0)
kn6 = Button(window,text='12')
kn6.grid(row = 0, column = 1)
kn7 = Button(window,text='13')
kn7.grid(row = 1, column = 0)
kn8 = Button(window,text='14')
kn8.grid(row = 1, column = 1)

window.mainloop()



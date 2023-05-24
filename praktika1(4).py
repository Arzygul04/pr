from tkinter import*
window = Tk()
window.title('Размещение виджетов')
window.geometry('300x300')



ramka1 = Frame(window, width = 200, height = 200, bg = 'grey', bd = 2)
kn = Button(ramka1, text = 'Семь цветов радуги', bg = 'white')
kn.grid(column = 0, row = 0)

kn2 = Button(ramka1,width=800, bg = 'red')
kn2.grid(column = 0, row = 1)
kn3 = Button(ramka1,width=800, bg = 'orange')
kn3.grid(column = 0, row = 2)
kn4 = Button(ramka1,width=800, bg = 'yellow')
kn4.grid(column = 0, row = 3)
kn5 = Button(ramka1,width=800, bg = 'green')
kn5.grid(column = 0, row = 4)
kn6 = Button(ramka1,width=800, bg = 'blue')
kn6.grid(column = 0, row = 5)
kn7 = Button(ramka1,width=800, bg = 'indigo')
kn7.grid(column = 0, row = 6)
kn8 = Button(ramka1,width=800, bg = 'violet')
kn8.grid(column = 0, row = 7)


ramka1.pack()


from tkinter import*
window = Tk()
window.title('Здраствуйте программисты!')
window.geometry('400x400')

btn = Button(text = 'группа - 1Р-20')
btn.grid(column = 0, row = 0)

lb = Label(text = 'Мой первый виджет')
lb.grid(column = 0, row = 1)

pol = Entry(window, width = 13)
pol.grid(column = 0, row = 2)

lb1 = Label(text = 'Я выбираю')
lb1.grid(column = 2, row = 3)
kn1 = Checkbutton(window, text = 'Python', onvalue = 1, offvalue = 0)
kn2 = Checkbutton(window, text = 'Java', onvalue = 1, offvalue = 0)
kn1.grid(column = 2, row = 4)
kn2.grid(column = 2, row = 5)


lb2 = Label(text = 'Я выбираю:')
lb2.grid(column = 2, row = 6)
kn3 = Radiobutton(window, text = 'PHP', value = 1)
kn4 = Radiobutton(window, text = 'C#', value = 2)
kn3.grid(column = 2, row = 7)
kn4.grid(column = 2, row = 8)


window.mainloop()

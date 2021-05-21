#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Напишите программу, в которой на главном окне находятся холст и кнопка
# "Добавить фигуру". Кнопка открывает второе окно, включающее четыре поля для ввода
# координат и две радиокнопки для выбора, рисовать ли на холсте прямоугольник или овал.
# Здесь же находится кнопка "Нарисовать", при клике на которую соответствующая фигура
# добавляется на холст, а второе окно закрывается. Проверку корректности ввода в поля
# можно опустить.


from tkinter import *

root = Tk()
root.title('Прямовал')


def addFigure():
    fig = Toplevel()
    fig.title('Фигура')
    fig.resizable(0, 0)

    frame1 = Frame(fig)
    frame1.pack(padx=10, pady=10)
    Label(frame1, text='x1').pack(side=LEFT)
    x1 = Entry(frame1, width=3)
    x1.pack(side=LEFT)
    Label(frame1, text='y1').pack(side=LEFT)
    y1 = Entry(frame1, width=3)
    y1.pack(side=LEFT)

    frame2 = Frame(fig)
    frame2.pack()
    Label(frame2, text='x2').pack(side=LEFT)
    x2 = Entry(frame2, width=3)
    x2.pack(side=LEFT)
    Label(frame2, text='y2').pack(side=LEFT)
    y2 = Entry(frame2, width=3)
    y2.pack(side=LEFT)

    frame3 = Frame(fig)
    frame3.pack(padx=10, pady=10)
    v = IntVar()
    v.set(1)
    Radiobutton(frame3, text='Прямоугольник', variable=v,
                value=1).pack(anchor=W)
    Radiobutton(frame3, text='Овал', variable=v,
                value=0).pack(anchor=W)

    def paint():
        x = int(x1.get())
        y = int(y1.get())
        xx = int(x2.get())
        yy = int(y2.get())
        if v.get() == 0:
            c.create_oval(x, y, xx, yy, width=2)
        elif v.get() == 1:
            c.create_rectangle(x, y, xx, yy, width=2)
        fig.destroy()

    Button(fig, text='Нарисовать', command=paint).pack(pady=10)


c = Canvas(width=300, height=300, bg='white')
c.pack()
Button(text='Добавить фигуру', command=addFigure).pack()

root.mainloop()

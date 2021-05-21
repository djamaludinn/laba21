#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import logging

#   Напишите программу, в которой на главном окне находятся холст и кнопка "Добавить фигуру".
#   Кнопка открывает второе окно, включающее четыре поля для ввода координат и две радиокнопки для выбора:
#   рисовать ли на холсте прямоугольник или овал.
#   Здесь же находится кнопка "Нарисовать", при клике на которую соответствующая фигура
#   добавляется на холст, а второе окно закрывается. Проверку корректности ввода в поля
#   можно опустить.


def setting():

    # Создаем графический интерфейс
    a = Toplevel()
    a.title('Фигура')
    a.geometry('200x200')
    a.resizable(False, False)

    # Устанавливаем окно справа от главного окна
    width = a.winfo_screenwidth()
    height = a.winfo_screenheight()
    width = (width // 2) + 200
    height = (height // 2) - 200

    # Создаем текстовые пометки
    Label(a, text="x1", font=12).grid(row=1, column=1, pady=10, padx=5)
    Label(a, text="x2", font=12).grid(row=2, column=1, pady=10, padx=5)
    Label(a, text="y1", font=12).grid(row=1, column=3, pady=10, padx=5)
    Label(a, text="y2", font=12).grid(row=2, column=3, pady=10, padx=5)

    # Создаем формы для ввода значений
    x1 = Entry(a, width=4, font=36, justify=CENTER)
    x1.grid(row=1, column=2)
    y1 = Entry(a, width=4, font=36, justify=CENTER)
    y1.grid(row=1, column=4)
    x2 = Entry(a, width=4, font=36, justify=CENTER)
    x2.grid(row=2, column=2)
    y2 = Entry(a, width=4, font=36, justify=CENTER)
    y2.grid(row=2, column=4)

    # Создаем радиокнопки
    r_var = IntVar()
    r_var.set(0)
    r1 = Radiobutton(a, text='Прямоугольник', variable=r_var, value=0)
    r1.grid(row=3, column=0, columnspan=4, sticky=W)
    r2 = Radiobutton(a, text='Овал', variable=r_var, value=1)
    r2.grid(row=4, column=0, columnspan=4, sticky=W)

    def display():
        x = int(x1.get())
        y = int(y1.get())
        xx = int(x2.get())
        yy = int(y2.get())

        if r_var.get() == 0:
            c.create_rectangle(x, y, xx, yy, width=2)
        elif r_var.get() == 1:
            c.create_oval(x, y, xx, yy, width=2)
        a.destroy()

    # Создаем кнопку
    button_first = Button(a, height=1, width=15, text='Добавить фигуру', command=display)
    button_first.grid(row=5, column=0, columnspan=5, pady=10, sticky=N+S+W+E)

    return a.geometry('200x200+{}+{}'.format(width, height))


if __name__ == '__main__':
    logging.basicConfig(
        filename='check.log',
        level=logging.INFO
    )
    # Создаем графический интерфейс
    root = Tk()
    root.title('Title')
    root.resizable(False, False)

    # Устанавливаем окно по центру экрана
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 200
    h = h - 200
    root.geometry('400x400+{}+{}'.format(w, h))

    # Создаем формы для ввода значений
    c = Canvas(root, width=400, height=370, bg="white")
    c.grid(row=0, column=1, columnspan=2)

    # Создаем кнопки для выполнений определенных команд
    button = Button(height=1, width=15, text='Добавить фигуру', command=setting).grid(row=1, column=1, columnspan=2)

    # Запуск программы
    root.mainloop()

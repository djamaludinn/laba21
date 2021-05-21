#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from random import random

# Решите задачу: за рамками данного курса было оставлено несколько классов пакета tkinter.
# Среди них PhotoImage , позволяющий использовать в программе внешние изображения форматов GIF и PGM.
# Экземпляры PhotoImage можно размещать на различных виджетах через опцию image.
# Напишите программу, состоящую из главного окна и кнопки, на которой изображен смайлик.
# При клике на кнопку она должна оказываться в новом случайном месте окна. Размер окна
# может меняться.


def move():
    x = random()
    y = random()

    b.place(relx=x, rely=y)


if __name__ == '__main__':
    # Создаем графический интерфейс
    root = Tk()
    root['bg'] = 'white'
    root.geometry('800x800')

    # Загружаем фото
    img = PhotoImage(file='amogus.png')

    # Создаем `кнопку`
    b = Button(image=img, command=move, borderwidth=0, bg='white', activebackground='white')
    b.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Запускаем программу
    root.mainloop()

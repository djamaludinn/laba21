#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog as fd

# Решите задачу: измените программу из п. 9 так, чтобы открытие и сохранение файлов
# выполнялось не через экземпляры Button , а через Menu . Команду очистки текстового поля
# поместите в контекстное меню.


def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()


def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


def clear_text():
    text.delete(1.0, END)


root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)
root.resizable(False, False)

text = Text(width=50, height=25)
text.grid(columnspan=2)

text.bind("<Button-3>", popup)
menu = Menu(tearoff=0)

menu.add_command(label="Очистить", command=clear_text)
mainmenu.add_command(label='Открыть', command=insert_text)
mainmenu.add_command(label='Сохранить', command=extract_text)

root.mainloop()

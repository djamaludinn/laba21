#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module as mm
from tkinter import *


def commads(event):
    while True:
        try:
            command = entry.get()

            if command == 'exit':
                sys.exit()

            elif command == 'add':
                def but_action():
                    name = ent1.get()
                    phone_number = ent2.get()
                    birthday = ent3.get()

                    staff.add(name, phone_number, birthday)

                a = Toplevel()
                a.geometry('265x150+400+300')
                Label(a, text="Введите имя и фамилию: ").grid(row=0, column=1)
                ent1 = Entry(a, width=20)
                ent1.grid(row=1, column=1)

                Label(a, text="Введите номер телефона: ").grid(row=2, column=1)
                ent2 = Entry(a, width=20)
                ent2.grid(row=3, column=1)

                Label(a, text="Введите дату рождения в формате - дд.мм.гггг: ").grid(row=4, column=1)
                ent3 = Entry(a, width=20)
                ent3.grid(row=5, column=1)

                but1_1 = Button(a, text='Подтвердить', command=but_action)
                but1_1.grid(row=6, column=1)
                break

            elif command == 'list':

                lb2["width"] = 80
                lb2["text"] = staff

                break

            elif command.startswith('select '):

                parts = command.split(' ', maxsplit=2)
                numbers = parts[1]

                selected = staff.select(parts[1])

                if selected:
                    for c, people in enumerate(selected, 1):
                        lb2["text"] = f'Имя и фамилия: {people.name}\n' \
                                      f'Номер мобильного: {people.phone_number}\n\n' \
                                      f'Дата рождения: {people.birthday}'

                    break

                else:
                    lb2["text"] = f"Людей с такой датой рождения не найдено."

                    break

            elif command == 'help':
                lb2["text"] = f'Список команд:\n\n' \
                              f'add - добавить операцию;\n' \
                              f'list - вывести список операций;\n' \
                              f'select <счет плательщика> - \n' \
                              f'запросить информацию о выбранной операции;\n' \
                              f'help - отобразить справку;\n' \
                              f'exit - завершить работу с программой.'
                break
            else:
                lb2["text"] = 'Неизвестная команда!'
                break
        except Exception as exc:
            print(exc, file=sys.stderr)


if __name__ == '__main__':

    root = Tk()

    staff = mm.Man()
    root.title('Данные о людях')
    root.resizable(False, False)

    lb2 = Label(root, width=60, height=15)
    lb2.grid(row=3, column=1)

    lb = Label(text='Введите "help", чтобы отобразить справку.')
    lb.grid(row=1, column=1)
    entry = Entry(width=20, justify='center', font='30')
    entry.grid(row=2, column=1, ipady=5)
    entry.bind('<Return>', commads)

    root.mainloop()

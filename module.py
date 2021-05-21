#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import List


class IllegalMarksError(Exception):

    def __init__(self, birthday, message="Illegal year number"):
        self.birthday = birthday
        self.message = message
        super(IllegalMarksError, self).__init__(message)

    def __str__(self):
        return f"{self.birthday} -> {self.message}"


# Класс пользовательского исключения в случае, если введенная
# команда является недопустимой.
class UnknownCommandError(Exception):

    def __init__(self, command, message="Неизвестная команда."):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


@dataclass(frozen=True)
class People:
    name: str
    phone_number: int
    birthday: List[int]


@dataclass
class Man:
    soul: List[People] = field(default_factory=lambda: [])

    def add(self, name, phone_number, birthday):
        self.soul.append(
            People(
                name=name,
                phone_number=phone_number,
                birthday=birthday
            )
        )
        self.soul.sort(key=lambda people: people.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 28,
            '-' * 28,
            '-' * 28
        )
        table.append(line)
        table.append(
            ' {:^6}  {:^30}  {:^34}  {:^28} '.format(
                "№",
                "Фамилия и имя чел.",
                "Мобильный телефон",
                "День рождения челов."
            )
        )
        table.append(line)

        # Вывести данные о всех оценках ученика.
        for idx, people in enumerate(self.soul, 1):
            table.append(
                ' {:<1}  {:>33}  {:>25}  {:>61} '.format(
                    idx,
                    people.name,
                    people.phone_number,
                    people.birthday
                )
            )
        table.append(line)

        return '\n'.join(table)

    def __repr__(self):
        return self.__str__()

    def select(self, period):

        result = []
        count = 0
        for people in self.soul:
            if people.birthday:
                if people.birthday[1] == period:
                    count += 1
                    result.append(people)
        return result

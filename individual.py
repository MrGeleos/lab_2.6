#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    trains = []
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select - запросить поезда с одним пунктом;")
    print("exit - завершить работу с программой.")

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            destination = input("Пункт назначения? ")
            number = input("Номер поезда? ")
            time = input("Время отправления (ЧЧ:ММ)? ")

            train = {
                'destination': destination,
                'number': number,
                'time': time,
            }

            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('time', ''))

        elif command == 'list':
            line = "+-{}-+-{}-+-{}-+-{}-+".format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "№",
                    "Пункт",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        train.get('destination', ''),
                        train.get('number', ''),
                        train.get('time', 0)
                    )
                )
            print(line)

        elif command.startswith('select'):

            destination1 = input('Введите название пункта: ')

            count = 0

            for train in trains:
                if train.get('destination', '') == destination1:
                    print(
                        '{:>1} {}'.format('Пункт: ', train.get('destination', '')),
                        '{:>1} {}'.format('Номер поезда: ', train.get('number', '')),
                        '{:>1} {}'.format('Время отправления: ', train.get('time', 0))
                    )
                    count += 1

            if count == 0:
                print("Поезд с таким пунктом не найден.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

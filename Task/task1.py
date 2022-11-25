#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1a': 20,
        '2b': 24,
        '6a': 15,
        '7a': 10
    }
    print("Начальный вид классов и учеников:", '\n', school)
    school['2b'] = 26
    school['1b'] = 16
    del school['7a']
    S = sum(school.values())
    print('\n', school, '\n', "Общее количество учеников в школе:", S)
    
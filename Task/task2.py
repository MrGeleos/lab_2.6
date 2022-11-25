#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sir = {
        1: 'I',
        2: 'II',
        3: 'III'
    }
    print(sir)
    print({v: k for k, v in sir.items()})

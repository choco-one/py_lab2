#!/usr/bin/python

import my_pkg
import sys

while True:
    num = input('Select menu: 1) conversion 2) union/intersection 3) exit? ')
    num = int(num)

    if num == 1:
        my_pkg.conv()
    elif num == 2:
        my_pkg.uni_inter()
    elif num == 3:
        print('exit the program...')
        sys.exit()
    else:
        print('you enter wrong number...!')
        continue

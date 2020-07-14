#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
text = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
counter = 0
while counter != m:
    for i in matrix:
        text += i[counter]
    counter += 1
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", text))




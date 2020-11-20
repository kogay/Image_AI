#!usr/bin/env python3
# coding: utf-8

def step(x):
    if x >= 0:
        return 1
    else:
        return 0

def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7
    x = w1*x1 + w2*x2 + b
    return step(x)

if __name__ == '__main':
    print("This is prc_and.py")

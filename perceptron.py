#!/usr/bin/env python
# coding: utf-8
import numpy as np

def step(x):
    if x >= 0:
        return 1
    else:
        return 0

def AND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    b = -0.7
    X_W = np.dot(X, W)
    return step(X_W + b)

def OR(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    b = -0.2
    X_W = np.dot(X, W)
    return step(X_W + b)

def NAND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([-0.5, -0.5])
    b = 0.7
    X_W = np.dot(X, W)
    return step(X_W + b)

def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    print("This is perceptron.py")

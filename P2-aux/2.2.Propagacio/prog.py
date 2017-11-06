#!/usr/bin/python3
import sys
import os

sys.path.insert(0,"AES-Python")

from aes import AES

def number_bits_change(a,b):
    c = a ^ b
    return bin(c).count("1")

def change_i_bit(n,i):
    masc = 1 << i
    return n ^ masc

def ex1(M = 0x3243f6a8885a308d313198a2e0370734, K = 0x2b7e151628aed2a6abf7158809cf4f3c):
    a = AES(K)
    C = a.encrypt(M)
    l = []
    for i in range(128):
        Mi = change_i_bit(M,i)
        Ci = a.encrypt(Mi)
        changes = number_bits_change(C,Ci)
        l.append(changes)
    return l



l = ex1()
f = open('data1', 'w')
for i in range(len(l)):
    g = str(i) + "," + str(l[i]) + "\n"
    f.write(g)
f.close()

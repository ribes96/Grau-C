#!/usr/bin/python3
import sys
import os

sys.path.insert(0,"AES-Python")

from aes import AES

def change_i_bit(n,i):
    masc = 1 << i
    return n ^ masc

def ex1(m,i,j,key = 0x2b7e151628aed2a6abf7158809cf4f3c):
    normal = AES(key, customByteSub = False)
    change = AES(key, customByteSub = True)
    mi = change_i_bit(m,i)
    mj = change_i_bit(m,j)
    mij = change_i_bit(mi,j)

    c = normal.encrypt(m)
    ci = normal.encrypt(mi)
    cj = normal.encrypt(mj)
    cij = normal.encrypt(mij)

    c2 = change.encrypt(m)
    ci2 = change.encrypt(mi)
    cj2 = change.encrypt(mj)
    cij2 = change.encrypt(mij)

    if c == ci ^ cj ^ cij:
        print("With normal it DO happen")
    else:
        print("With normal it do NOT happen")

    if c2 == ci2 ^ cj2 ^ cij2:
        print("With the change it DO happen")
    else:
        print("With the change it do NOT happen")

def ex2(m,i,j,key = 0x2b7e151628aed2a6abf7158809cf4f3c):
    normal = AES(key, customShiftRows = False)
    change = AES(key, customShiftRows = True)
    mi = change_i_bit(m,i)

    c = normal.encrypt(m)
    ci = normal.encrypt(mi)

    c2 = change.encrypt(m)
    ci2 = change.encrypt(mi)

    print("m, mi")
    print(m,",",mi)
    print("----------------")
    print("c, ci")
    print(c,",",ci)

def ex3(m,i,j,key = 0x2b7e151628aed2a6abf7158809cf4f3c):
    normal = AES(key, customMixColumns = False)
    change = AES(key, customMixColumns = True)
    mi = change_i_bit(m,i)

    c = normal.encrypt(m)
    ci = normal.encrypt(mi)

    c2 = change.encrypt(m)
    ci2 = change.encrypt(mi)

    print("m, mi")
    print(m,",",mi)
    print("----------------")
    print("c, ci")
    print(c,",",ci)


print("Esto ha empezado")
master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
# a = AES(master_key, False)

plaintext = 0x3243f6a8885a308d313198a2e0370734

ex3(plaintext, 4,7)
# ex2(plaintext, 4,7)
# encrypted = a.encrypt(plaintext)
# encrypted2 = a.encrypt(plaintext)
# decrypted = a.decrypt(encrypted)
#
# print("Texto plano:",plaintext)
# print("Texto cifrado:",encrypted)
# print("Texto cifrado2:",encrypted2)
# print("Texto descifrado:",decrypted)
# print("¿Son iguales?:", plaintext == decrypted)

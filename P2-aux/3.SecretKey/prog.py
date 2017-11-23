#!/usr/bin/python3.6
import sys
import os
from hashlib import sha256
from subprocess import call

sys.path.insert(0,"/home/hobber/git/CryptTools/tools")
sys.path.insert(0, "/home/hobber/git/CryptTools/lib")
from aes import AES

def decrypt(m):
    IV = m[0:16]
    # print(type(IV))
    for kiv in range(2**2):
        KS = sha256(IV + (kiv).to_bytes(2, byteorder = "big"))
        call(["./aes", "-t", m, "-k", KS])


f = open("2017_09_26_13_22_33_albert.ribes.marza.puerta_trasera.enc", "rb")
st = f.read()
# print(type(st))
decrypt(st)

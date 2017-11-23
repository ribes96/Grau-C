#!/usr/bin/python3


from os import listdir
from os.path import isfile, join

from Crypto.PublicKey import RSA
import fractions



mypath = "/home/hobber/Downloads/clavesC/pems"
miN = 13883564478855369906484485454184038270497003202052494098604697319212549591029829230700001597479504789032931295242015286932254426742588105107486509065584647123511688340081903152167823286168609306599636677775544506080893206218696765728385372891018283918529570398644229104126706781596839106635407280120492004966826027059771188307280814710580762484959162922829327125223862094417926683638631342959146651539093052789262774346160814294285902219581491935291074945116267040230555596298781939261249389955870273713988762923733293159385434415536514574878849224579390013439041844109572697914870592137097391149463732879558042682513

miFichero = "albert.ribes.marza_pubkeyRSA_RW.pem"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for pemfile in onlyfiles:
    if pemfile == miFichero:
        # pem = "pems/" + pemfile
        # f = open(pem,'r')
        # key = RSA.importKey(f.read())
        # pub = key.p
        # print(pub)
        continue

    pem = "pems/" + pemfile
    f = open(pem,'r')
    key = RSA.importKey(f.read())
    n = key.n
    gcd = fractions.gcd(miN, n)
    if gcd == 1: continue
    print("El fichero",pemfile,"tiene como factor comun:")
    print(gcd)
    print("----------------------")

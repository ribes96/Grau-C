#!/usr/bin/python3
import subprocess

import Crypto.PublicKey.RSA
modstr = "0a:e7:f2:4f:2b:e7:b5:ee:e5:37:71:9b:9e:02:0b:\
73:0e:88:04:69:ca:33:27:3e:ef:8b:7e:bb:9e:53:\
7d:38:bf:95:3a:4b:cf:f6:97:2c:82:22:29:76:a8:\
a3:ea:5c:10:03:8e:26:03:14:85:fb:b0:84:db:cd:\
13:84:d0:5b:26:83:5a:27:0c:40:36:a6:8b:59:78:\
c8:48:b5:3c:2d:a1:e2:1a:42:3a:d3:de:f8:18:58:\
84:25:0d:c4:e8:59:48:6d:48:9f:aa:13:1e:ba:51:\
7c:ce:bf:2f:12:a7:dc:f6:13:33:bd:bd:03:6e:0d:\
7c:c7:69:9c:bf:fb:93:fe:14:ef:db:27:cc:61:74:\
6b:f4:cc:86:cb:9f:93:70:41:24:a1:52:4c:82:3f:\
da:1f:d7:e3:86:28:76:53:06:f2:ff:58:47:65:d8:\
6a:78:ee:89:16:ca:4e:08:59:f0:84:9f:79:c7:3a:\
40:7a:0b:35:56:c8:ee:6b:bd:b5:a3:65:11:f0:f0:\
36:99:8c:ca:69:14:34:c3:45:be:31:b9:0f:1d:73:\
cf:46:6a:1b:22:22:ad:50:92:68:a0:00:1f:8a:a9:\
8c:eb:65:8f:88:9c:be:69:b4:fb:51:78:21:18:51:\
6d:d4:f6:f5:73:37:ae:fb:d0:b8:ab:c3:26:80:b2:\
a1"

n = int("".join(modstr.split(":")),16)
e = 65537
d=117080684019271509433966527002489501514693923697916038671274126971758958550181191155906973232240577169628017753890743649150929549713308567915465293914312839021257888533161512985723618020644718544012995504799948533262941767682371870537429020693021007759652501968260203327623812102561035433202513355008745592564130867803523300596347125626073325259891468781563158648104791390951450385787049128790906371547794157526747233828787079006602964845215541017087094283104484449761893088723006072807881267836888543278670243994332426631211985076954899799773047537337645990060740234876186746039450025285398620419155662419276205442283989036010607356870581326368037270361922748439818600871383380963443837761539758051655048578620230246683750995480732275474514337815053258779350904742022312987483297310819851098827726430693710545889785476101985545333175354842178262504804463755588300212028425367181878396998820051200074808355553904657106369017969014904223349655745889530162824250072272271441030546710251861494606388694951480736068815421070724291553916906387720651597865552226774722119253466584142588429171722996706865441046527844103546159150010127747535917257789209143419994634892766075727873

p = 16359227226926065513**16
q = 291629676500338103131306380296634053939**8


obj = Crypto.PublicKey.RSA.construct((n,e,d,p,q))
st = obj.exportKey(format='PEM')
f = open("prob1.PEM", "wb")
f.write(st)
f.close()
cmd = "openssl rsautl -decrypt -inkey prob1.PEM -in albert.ribes.marza_RSA_pseudo.enc -out respuesta"
cmdlist = cmd.split()
subprocess.run(cmdlist, stdout=subprocess.PIPE)
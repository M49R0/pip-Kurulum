#!usr/bin/env python3
# -*- coding:utf-8 -*- 

import os

os.system("apt install figlet")
os.system("apt install wget")
os.system("clear")
os.system("figlet MAKRO")

print("""

pip Kurulum Aracına Hoşgeldiniz
""")

kur = input("Pip Aracı Kurulsunmu [E/h] ")



if kur=="e" or kur=="E":
	os.system("apt install wget -y")
	os.system("wget https://bootstrap.pypa.io/get-pip.py")
	os.system("python get-pip.py")
	soru = input("pip Aracını kuran python dosyası silinsin mi? [E/h]: ")
	if soru=="e" or soru=="E":
		os.system("rm -rf get-pip.py")
	
	elif soru=="H" soru=="h":
		print("""
	
	Güle Güle""")
		print("Yanlış seçim")
elif(kur=="n"):
	print("""
	
Güle Güle

	""")

#!usr/bin/env python
# -*- coding:utf-8 -*- 

import os

os.system("apt install figlet")
os.system("apt install wget")
os.system("clear")
os.system("figlet MAKRO")

print("""

pip Kurulum Aracına Hoşgeldiniz

""")

kur = input("Pip Aracı Kurulsunmu [Y/n] ")



if(kur=="y"):
	os.system("apt install wget -y")
	os.system("wget https://bootstrap.pypa.io/get-pip.py")
	os.system("python get-pip.py")
	soru = input("pip Aracını kuran python dosyası silinsin mi? y/n: ")
	if(soru=="y"):
		os.system("rm -rf get-pip.py")
	
	elif(soru=="n"):
		print("""
	
	Güle Güle""")
		print("Yanlış seçim")
elif(kur=="n"):
	print("""
	
Güle Güle

	""")
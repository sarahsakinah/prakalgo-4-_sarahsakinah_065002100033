# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:36:33 2021

@author: HP
"""

print("@@@@ @@@ @@@@ @@@  @ @")
print("@    @ @ @  @ @ @  @ @")
print("@    @@@ @@@@ @@@  @ @")
print("@@@@ @@@ @@   @ @  @@@")
print("   @ @ @ @ @  @ @  @ @")
print("   @ @ @ @  @ @ @  @ @")
print("@@@@ @ @ @   @@ @  @ @")
import sys
sarah=0
while sarah ==0:
    print("=== PROGRAM KONVERSI BILANGAN===")
    print("1.Desimal ke Biner")
    print("2.Biner ke Desimal")
    print("3.Keluar")
    sarah1=int(input("silahkan Pilih Menu: "))
    if sarah1==1:
        desimal = int(input("masukkan Desimal: "))
        if desimal == 0:
            print(0)
        else:
            print("hasil bagi sisa biner")
            bitsring=""
        while desimal > 0:
            sisa= desimal %2 
            desimal = desimal //2
            bitstring = str(sisa) + bitsring
            
            print("Binernya adalah: ",bitsring)
    elif sarah1==2:
        bit=input("Masukkan str biner: ")
        desimal=0
        eks = len(bit)-1
        for digit in bit:
            desimal += int(digit)*2**eks
            eks-= 1
        print ("Nilai Desimal adalah :",desimal)
    elif sarah1==3:
        sys.exit(0)
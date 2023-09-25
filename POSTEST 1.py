print("""
=====
MASUK
===== """)

print()
#memasukkan nama dan nim sebagai data
print("Masukkan Nama dan NIM!")
nama = input("Nama: ")
nim = input("NIM: ")

print()
#memasukkan username dan password sesuai data
print("Masuk ke Akun Menggunakan Nama dan NIM!")
while True:
    a = input("Masukkan Username (Nama): ")
    b = input("Masukkan Password (NIM): ")

    if a == nama and b == nim:
        print("""
        ====================
        Anda Berhasil Masuk!
        ====================""")
        break
    else: 
        a != nama and b != nim
    print("Username atau Password yang Anda Masukkan Salah!")
    
print("""
====================================
Menghitung Rumus Segitiga Pythagoras
====================================""")

import math
#fungsi untuk menentukan menu yang dipilih
def menu_awal():
    sisi_yang_dihitung = int(input("""
1. Alas
2. Sisi tegak 
3. Sisi miring
4. Keluar
Pilih sisi yang akan dihitung = """))
    if sisi_yang_dihitung == 1:
        menghitung_alas()                 #masuk ke fungsi menghitung alas

    elif sisi_yang_dihitung == 2:
        menghitung_sisi_tegak()           #masuk ke fungsi menghitung sisi tegak

    elif sisi_yang_dihitung == 3:
        menghitung_sisi_miring()          #masuk ke fungsi menghitung sisi miring

    else: 
        keluar()                          #untuk keluar dari program

#fungsi untuk menghitung alas
def menghitung_alas():
    c = float(input("Masukkan panjang sisi miring = "))
    b = float(input("Masukkan panjang sisi tegak = "))
    a = float(math.sqrt(c**2 - b**2))
    print("Panjang alas segitiga adalah = ", a)
    menu_awal()
    #kembali ke menu awal

#fungsi untuk menghitung sisi tegak
def menghitung_sisi_tegak():
    c = float(input("Masukkan panjang sisi miring = "))
    a = float(input("Masukkan panjang alas = "))
    b = float(math.sqrt(c**2 - a**2))
    print("Panjang sisi tegak segitiga = ", b)
    menu_awal()
    #kembali ke menu awal

#fungsi untuk menghitung sisi miring    
def menghitung_sisi_miring():
    a = float(input("Masukkan panjang alas = "))
    b = float(input("Masukkan panjang sisi tegak = "))
    c = float(math.sqrt(a**2 + b**2))
    print("Panjang sisi miring segitiga =", c)
    menu_awal()
    #kembali ke menu awal

#fungsi untuk keluar program
def keluar():
    print("Anda Keluar dari Akun !")

#fungsi untuk memulai program
menu_awal()

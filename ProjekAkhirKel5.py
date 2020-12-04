import os
from time import sleep

S = int (50000)
M = int (55000)
L = int (60000)
XL = int (65000)

def size_s() :
    print ("\nHarga Baju Ukuran s adalah : " ,S)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli : "))
            if jumlah_baju <3 :
                b = jumlah_baju * 50000
                print("\nAnda memesan {0} baju dengan ukuran S" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\nRincian Harga : {0} baju x Rp.50000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 50000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran S" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.50000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 50000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran S" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.50000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
        except ValueError:
            print("\nMasukkan Kembali Jumlah Yang Benar ( Hanya Angka ) ")

def size_m() :
    print ("\nHarga Baju Ukuran M adalah : " ,M)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli = "))
            if jumlah_baju <3 :
                b = jumlah_baju * 55000
                print("\nAnda memesan {0} baju dengan ukuran M" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\n Rincian Harga : {0} baju x Rp.55000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 55000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran M" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\n{0} baju x Rp.55000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 55000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran M" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.55000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
        except ValueError:
            print("\nMasukkan Kembali Jumlah Yang Benar ( Hanya Angka ) ")

def size_l() :
    print ("\nHarga Baju Ukuran L adalah : " ,L)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli = "))
            if jumlah_baju <3 :
                b = jumlah_baju * 60000
                print("\nAnda memesan {0} baju dengan ukuran L" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\nRincian Harga : {0} baju x Rp.60000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 60000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran L" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\n{0} baju x Rp.60000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 60000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran L" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.60000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
        except ValueError:
            print("\nMasukkan Kembali Jumlah Yang Benar ( Hanya Angka ) ")
    
def size_xl() :
    print ("\nHarga Baju Ukuran XL adalah : " ,XL)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli = "))
            if jumlah_baju <3 :
                b = jumlah_baju * 65000
                print("\nAnda memesan {0} baju dengan ukuran XL" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\nRincian Harga : {0} baju x Rp.65000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami")
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 65000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran XL" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.65000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami",user)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 65000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran XL" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.65000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami")
                eror=False
        except ValueError:
            print("\nMasukkan Kembali Jumlah Yang Benar ( Hanya Angka ) ")

kerjakan = True
while(kerjakan):
    user = ""
    while (user == ""):
        user = input("\nSilahkan Masukkan Nama Anda Untuk Melanjutkan Pembelian  :    ")
    print("\n\t\tSelamat datang Di toko Kami, {}".format(str.capitalize(user)))
    print("\t\t++===================================================++")
    print("\t\t||                                                   ||")
    print("\t\t||               PROGRAM BELANJA BUSANA              ||")
    print("\t\t||                                                   ||")
    print("\t\t||               DIBUAT OLEH KELOMPOK 5              ||")
    print("\t\t||                                                   ||")
    print("\t\t++===================================================++")

    EROR = True
    while (EROR):
        try:
            jenis_kelamin = (input)("\n\nSilahkan Pilih Jenis Kelamin Anda, pria atau wanita ? : ")
            if (str.upper(jenis_kelamin) == "PRIA"):
                EROR = False
                print("\n\nBaik, Selamat Datang Bapak",str.capitalize(user))
            elif (str.upper(jenis_kelamin) == "WANITA"):
                EROR = False
                print("\n\nBaik, Selamat Datang Nyonya",str.capitalize(user))
            else:
                print("\n\nSilahkan Masukkan Jenis Kelamin Anda Dengan Benar! Pria / Wanita ? : ")
        except ValueError:
            print("\n\nSilahkan Masukkan Jenis Kelamin Anda Dengan Benar! Pria / Wanita ? : ")

    print("\t\t\t\t Selamat! Kami sedang mengadakan promo.")
    print("\t\t================================================================")
    print("\t\tJika anda membeli 3 Sampai 5 Baju kami akan memberi   diskon 10%")
    print("\t\tJika anda membeli 6 Baju atau lebih kami akan memberi diskon 15%")
    print("\t\t================================================================")
    
    EROR = True
    while (EROR): 
        try:
            indeks = input("\nPilihlah Ukuran Baju Anda  s, m, l, xl ? = ")
            if (str.upper(indeks) == "S" or str.upper(indeks) == "M" or str.upper(indeks) == "L" or str.upper(indeks) == "XL"):
                EROR = False
            else:
                print("Silahkan Pilih Kembali Antara ukuran s , m , l, xl")
                continue
        except ValueError:
            print("Ukuran Yang Anda Pilih Salah! (Silahkan Pilih Kembali Antara ukuran s , m , l, xl")
            
    if (str.upper(indeks) == "S"):
        size_s()
    
    elif (str.upper(indeks) == "M"):
        size_m()
    
    elif (str.upper(indeks) == "L"):
        size_l()
    
    elif (str.upper(indeks) == "XL"):
        size_xl()
    
    else:
        print("\nUkuran Yang Anda Pilih Salah! (Silahkan Pilih Kembali Antara ukuran s , m , l, xl)")

#ULANGI
    EROR = True
    while (EROR):
        ulangi = input("\n\nUlangi?  (YA / TIDAK)!:   ")

        if (str.upper(ulangi) == "YA"): #YA
            while(EROR):
                clr = input("\nApakah Anda ingin Membersihkan layar? (YA / TIDAK):    ")
                if (str.upper(clr) == "YA"):
                    print("\nSedang Membersihkan Layar ...")
                    sleep(1)
                    os.system('cls')
                    EROR = False
                elif (str.upper(clr) == "TIDAK"):
                    EROR = False
                else:
                    print("Input Anda Salah!!!")

        elif (str.upper(ulangi) == "TIDAK"): #TIDAK
                print("\nTerima Kasih!\n\n")
                EROR = False
                kerjakan = False        
        else:
            print("Input anda salah!!!")

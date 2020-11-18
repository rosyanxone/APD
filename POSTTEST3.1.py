#Start
print("Selamat Datang di Toko Kue Sule!\n")
print("1. Kue Keju: Rp.6000/kue")
print("2. Kue Cokelat: Rp.3500/kue")
print("Ingin memesan kue apa?")
kue = str(input("(masukkan angka 1/2) :"))
#KueKeju
if kue == "1":
    print("Anda memesan kue Keju.")
    print("\nSelamat! Kami sedang mengadakan promo.")
    print("Jika anda memesan 4 kue keju atau lebih, kami beri diskon 10%")
    print("Jika anda memesan 16 kue keju atau lebih, kami beri diskon 15%")
    print("(kue terbatas tidak lebih dari 25)")
#Pesanan1
    kue1 = int(input("\nBerapa kue keju yang ingin di pesan? :"))
    if kue1 < 4:
        c = kue1 * 6000
        print("Anda memesan {0} kue keju, total harga: Rp.{1}".format(kue1, c))
    elif kue1 >= 4 and kue1 <= 15:
        c = kue1 * 6000 * 10 / 100
        print("Anda memesan {0} kue keju, total harga: Rp.{1} dengan diskon 10%.".format(kue1, c))
    elif kue1 >= 16 and kue1 <= 25:
        c = kue1 * 6000 * 15 / 100
        print("Anda memesan {0} kue keju, total harga: Rp.{1} dengan diskon 15%.".format(kue1, c))
    else:
        print("Kue tidak tersedia lebih dari 25.")
#KueCokelat
elif kue == "2":
    print("Anda memesan kue Cokelat.")
    print("\nSelamat! Kami sedang mengadakan promo.")
    print("Jika anda memesan 5 kue cokelat atau lebih, kami beri diskon 7%")
    print("Jika anda memesan 21 kue cokelat atau lebih, kami beri diskon 12%")
    print("(kue terbatas tidak lebih dari 35)")
#Pesanan2
    kue2 = int(input("\nBerapa kue cokelat? :"))
    if kue2 < 5:
        c = kue2 * 3500
        print("Anda memesan {0} kue cokelat, total harga: Rp.{1}".format(kue2, c))
    elif kue2 >= 5 and kue2 <= 20:
        c = kue2 * 3500 * 7 / 100
        print("Anda memesan {0} kue cokelat, total harga: Rp.{1} dengan diskon 7%.".format(kue2, c))
    elif kue2 >= 21 and kue2 <= 35:
        c = kue2 * 3500 * 12 / 100
        print("Anda memesan {0} kue cokelat, total harga: Rp.{1} dengan diskon 12%.".format(kue2, c))
    else:
        print("Kue tidak tersedia lebih dari 35.")
#InvalidInput
else:
    print("\nInput yang anda masukkan salah!")
#End

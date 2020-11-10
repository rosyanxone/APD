#Start
print(str("\nMenghitung Luas Bangun Datar\n"))
print("1.Persegi")
print("2.Jajar Genjang")
print("3.Belah Ketupat")
print("4.Trapesium")
print("5.Layang-layang")
print("6.Segitiga")
print("7.Lingkaran")
#1stInput
nomer = input("Masukkan pilihan 1 ~ 7:")
#1.Persegi
if nomer == '1':
    s = int(input("\nMasukkan Sisi Persegi:"))
    c = s * s
    print(str("Luas Persegi, SxS adalah: {0}x{1} = {2}".format(s, s, c)))
    print("'Operasi Selesai' ")
#2.Jajargenjang  
elif nomer == '2':
    a = int(input("\nMasukkan Alas Jajargenjang:"))
    t = int(input("Masukkan Tinggi Jajargenjang:"))
    c = a * t
    print(str("Luas Jajargenjang, AxT adalah: {0}x{1} = {2}".format(a, t, c)))
    print("'Operasi Selesai' ")
#3.Belah Ketupat  
elif nomer == '3':
    d1 = int(input("\nMasukkan Diagonal1:"))
    d2 = int(input("Masukkan Diagonal2:"))
    c = d1*d2*.5
    print(str("Luas Belah Ketupat adalah: {0}x{1}:2 = {2}".format(d1, d2, c)))
    print("'Operasi Selesai' ")
#4.Trapesium   
elif nomer == '4':
    a = int(input("\nMasukkan Alas Trapesium:"))
    b = int(input("Masukkan Sisi Atas Trapesium:"))
    t = int(input("Masukkan Tinggi Trapesium:"))
    c = .5*(a + b)*t
    print(str("Luas Trapesium adalah: ({0}+{1}):2x{2} = {3}".format(a, b, t, c)))
    print("'Operasi Selesai' ")
#5.Layang-layang 
elif nomer == '5':
    d1 = int(input("\nMasukkan Diagonal1:"))
    d2 = int(input("Masukkan Diagonal2:"))
    c = d1*d2*.5
    print(str("Luas Layang-layang adalah: ({0}x{1}):2 = {2}".format(d1, d2, c)))
    print("'Operasi Selesai' ")
#6.Segitiga
elif nomer == '6':
    a = int(input("\nMasukkan Alas Segitiga:"))
    t = int(input("Masukkan Tinggi Segitiga:"))
    c = a*t*.5
    print(str("Luas Segitiga adalah: ({0}x{1}):2 = {2}".format(a, t, c)))
    print("'Operasi Selesai' ")
#7.Lingkaran
elif nomer == '7':
    pi = 3.14
    r = float(input("\nMasukkan Jari-jari Lingkaran:"))
    c = pi*r*r
    print(str("Luas Lingkaran, πr2 adalah: {0}x{1}^2 = {2}".format(pi, r, c)))
    print("'Operasi Selesai' ")
#InvalidInput
else:
    print(str("\n'Input Tidak Valid'"))

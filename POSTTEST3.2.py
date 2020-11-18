#Start
angka = int(input("Masukkan 3 digit NIM terakhir + 10 :"))
a = 1
b = 1
#Process
while (a <= angka):
    print (b)
    b+=1
    if (b == 10):
        b -= 9
    a += 1
#End

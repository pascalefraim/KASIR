total = 0
total1 = 0
porsi1 = 0
jenis1 = " " 
total2 = 0
porsi2 = 0
jenis2 = " "
total3 = 0
porsi3 = 0
jenis3 = " "
total4 = 0
porsi4 = 0
jenis4 = " "
total5 = 0
porsi5 = 0
jenis5 = " "
total6 = 0
porsi6 = 0
jenis6 = " "

print("=============PROGRAM KASIR RESTORAN=============")
print("======RESTORAN MURAH MERIAH PAS DI KANTONG======")
print("================================================")
nama = input("Nama Konsumen : ")
print("Nama Konsumen: ", nama)
menu = [
       ["101", "Nasi Goreng ", "10000"],
       ["102", "Mi Goreng   ", "6000"],
       ["103", "Mi Rebus    ", "7000"],
       ["104", "Es Teh      ", "2000"],
       ["105", "Es Jeruk    ", "3000"],
       ["106", "Es Milo     ", "5000"],
       ]
print("Daftar Menu : ")
print("Kode\t Menu\t\t Harga")
for i in range (0,len(menu)):
    print(menu[i][0], '\t', menu [i][1], menu [i][2])
    i += 1
 
def pilihan (i) :
    switcher = {
            101 : 'Nasi Goreng 10000',
            102 : 'Mi Goreng 6000',
            103 : 'Mi Rebus 7000',
            104 : 'Es Teh 2000',
            105 : 'Es Jeruk 3000',
            106 : 'Es Milo 5000',
            }
    return switcher.get(i, "Menu yang Dipesan")
    
nomor = int(input("Menu yang Dipesan: "))
menu = pilihan (nomor)
print(menu)

if nomor==101:
    porsi1 = int(input("Jumlah: "))
    total1 = total1 + porsi1*10000
    print(total1)
    jenis1 = ("Nasi Goreng")
elif nomor==102:
    porsi1 = int(input("Jumlah: "))
    total1 = total1 + porsi1*6000
    print(total1)
    jenis1 = ("Mi Goreng")
elif nomor== 103:
    porsi1 = int(input("Jumlah: "))
    total1 = total1 + porsi1*7000
    print(total1)
    jenis1 = ("Mi Rebus")
elif nomor == 104:
    porsi1 = int(input("Jumlah: "))
    total1 = total1 + porsi1*2000
    print(total1)
    jenis1 = ("Es Teh")
elif nomor == 105:
    porsi1 = int(input("Jumlah: "))
    total1 = total1 + porsi1*3000
    print(total1)
    jenis1 = ("Es Jeruk")
elif nomor == 106:
    porsi1 = int(input("Jumlah: "))
    total1 = total1 + porsi1*5000
    print(total1)
    jenis1 = ("Es Milo")
else:
    salah = int(input("""
      MENU TIDAK TERSEDIA!
SILAKAN MASUKKAN PESANAN ANDA : """))
    if salah==101:
        porsi1 = int(input("Jumlah: "))
        total1 = total1 + porsi1*10000
        print (total1)
        jenis1 = ("Nasi Goreng")
    elif salah==102:
        porsi1 = int(input("Jumlah: "))
        total1 = total1 + porsi1*6000
        print (total1)
        jenis1 = ("Mi Goreng")
    elif salah == 103:
        porsi1 = int(input("Jumlah: "))
        total1 = total1 + porsi1*7000
        print (total1)
        jenis1 = ("Mi Rebus")
    elif salah == 104:
        porsi1 = int(input("Jumlah: "))
        total1 = total1 + porsi1*2000
        print (total1)
        jenis1 = ("Es teh")
    elif salah == 105:
        porsi1 = int(input("Jumlah: "))
        total1 = total1 + porsi1*3000
        print (total1)
        jenis1 = ("Es jeruk")
    elif salah == 106:
        porsi1 = int(input("Jumlah: "))
        total1 = total1 + porsi1*5000
        print (total1)
        jenis1 = ("Es Milo")
        
print("""
        Apakah ada tambahan pesanan?
        Ya (a)
        Tidak (b)
      """)
jawaban = input(" ")
if jawaban == ("a"):
    print("Masukkan Menu Pilihan ke-2!")
    nomor = int(input("Menu yang Dipesan: "))
    menu = pilihan(nomor)
    print (menu)
    
    if nomor==101:
        porsi2 = int(input("Jumlah: "))
        total2 = total2 + porsi2*10000
        print (total2)
        jenis2 = ("Nasi Goreng")
    elif nomor==102:
        porsi2 = int(input("Jumlah: "))
        total2 = total2 + porsi2*6000
        print (total2)
        jenis2 = ("Mi Goreng")
    elif nomor == 103:
        porsi2 = int(input("Jumlah: "))
        total2 = total2 + porsi2*7000
        print (total2)
        jenis2 = ("Mi Rebus")
    elif nomor == 104:
        porsi2 = int(input("Jumlah: "))
        total2 = total2 + porsi2*2000
        print (total2)
        jenis2 = ("Es teh")
    elif nomor == 105:
        porsi2 = int(input("Jumlah: "))
        total2 = total2 + porsi2*3000
        print (total2)
        jenis2 = ("Es jeruk")
    elif nomor==106 :
        porsi2 = int(input("Jumlah: "))
        total2 = total2 + porsi2*5000
        print (total2)
        jenis2 = ("Es Milo")
    else:
        salah = int(input("""
      MENU TIDAK TERSEDIA!
SILAKAN MASUKKAN PESANAN ANDA : """))
        if salah==101:
            porsi2 = int(input("Jumlah: "))
            total2 = total2 + porsi2*10000
            print (total2)
            jenis2 = ("Nasi Goreng")
        elif salah==102:
            porsi2 = int(input("Jumlah: "))
            total2 = total2 + porsi2*6000
            print (total2)
            jenis2 = ("Mi Goreng")
        elif salah == 103:
            porsi2 = int(input("Jumlah: "))
            total2 = total2 + porsi2*7000
            print (total2)
            jenis2 = ("Mi Rebus")
        elif salah == 104:
            porsi2 = int(input("Jumlah: "))
            total2 = total2 + porsi2*2000
            print (total2)
            jenis2 = ("Es teh")
        elif salah == 105:
            porsi2 = int(input("Jumlah: "))
            total2 = total2 + porsi2*3000
            print (total2)
            jenis2 = ("Es jeruk")
        else:
            porsi2 = int(input("Jumlah: "))
            total2 = total2 + porsi2*5000
            print (total2)
            jenis2 = ("Es Milo")
        
    print("""
        Apakah ada tambahan makanan?
        Ya (a)
        Tidak (b)
          """)
    jawaban = input(" ")
    if jawaban == ("a"):
        print("Masukkan Menu Pilihan ke-3!")
        nomor = int(input("Menu yang Dipesan: "))
        menu = pilihan(nomor)
        print (menu)
        if nomor==101:
            porsi3= int(input("Jumlah: "))
            total3 = total3 + porsi3*10000
            print (total3)
            jenis3 = ("Nasi Goreng")
        elif nomor==102:
            porsi3 = int(input("Jumlah: "))
            total3 = total3 + porsi3*6000
            print (total3)
            jenis3 = ("Mi Goreng")
        elif nomor == 103:
            porsi3 = int(input("Jumlah: "))
            total3 = total3 + porsi3*7000
            print (total3)
            jenis3 = ("Mi Rebus")
        elif nomor == 104:
            porsi3 = int(input("Jumlah: "))
            total3 = total3 + porsi3*2000
            print (total3)
            jenis3 = ("Es teh")
        elif nomor == 105:
            porsi3 = int(input("Jumlah: "))
            total3 = total3 + porsi3*3000
            print (total3)
            jenis3 = ("Es jeruk")
        elif nomor==106:
            porsi3 = int(input("Jumlah: "))
            total3 = total3 + porsi3*5000
            print (total3)
            jenis3 = ("Es Milo")
        else:
             salah = int(input("""
      MENU TIDAK TERSEDIA!
SILAKAN MASUKKAN PESANAN ANDA : """))
             if salah==101:
                porsi3 = int(input("Jumlah: "))
                total3 = total3 + porsi3*10000
                print (total3)
                jenis3 = ("Nasi Goreng")
             elif salah==102:
                porsi3 = int(input("Jumlah: "))
                total3 = total3 + porsi3*6000
                print (total3)
                jenis3 = ("Mi Goreng")
             elif salah == 103:
                porsi3 = int(input("Jumlah: "))
                total3 = total3 + porsi3*7000
                print (total3)
                jenis3 = ("Mi Rebus")
             elif salah == 104:
                porsi3 = int(input("Jumlah: "))
                total3 = total3 + porsi3*2000
                print (total3)
                jenis3 = ("Es teh")
             elif salah == 105:
                porsi3 = int(input("Jumlah: "))
                total3 = total3 + porsi3*3000
                print (total3)
                jenis3 = ("Es jeruk")
             else:
                porsi3 = int(input("Jumlah: "))
                total3 = total3 + porsi3*5000
                print (total3)
                jenis3 = ("Es Milo")
        print("""
        Apakah ada tambahan makanan?
        Ya (a)
        Tidak (b)
              """)
        jawaban = input(" ")
        if jawaban == ("a"):
            print("Masukkan Menu Pilihan ke-4!")
            nomor = int(input("Menu yang Dipesan: "))
            menu = pilihan(nomor)
            print (menu)
            if nomor==101:
                porsi4= int(input("Jumlah: "))
                total4 = total4 + porsi4*10000
                print (total4)
                jenis4 = ("Nasi Goreng")
            elif nomor==102:
                porsi4 = int(input("Jumlah: "))
                total4 = total4 + porsi4*6000
                print (total4)
                jenis4 = ("Mi Goreng")
            elif nomor == 103:
                porsi4= int(input("Jumlah: "))
                total4 = total4 + porsi4*7000
                print (total4)
                jenis4 = ("Mi Rebus")
            elif nomor == 104:
                porsi4 = int(input("Jumlah: "))
                total4 = total4 + porsi4*2000
                print (total4)
                jenis4 = ("Es teh")
            elif nomor == 105:
                porsi4 = int(input("Jumlah: "))
                total4 = total4 + porsi4*3000
                print (total4)
                jenis4 = ("Es jeruk")
            elif nomor==106 :
                porsi4= int(input("Jumlah: "))
                total4 = total4 + porsi4*5000
                print (total4)
                jenis4 = ("Es Milo")
            else:
                salah = int(input("""
      MENU TIDAK TERSEDIA!
SILAKAN MASUKKAN PESANAN ANDA : """))
                if salah==101:
                    porsi4 = int(input("Jumlah: "))
                    total4 = total4 + porsi4*10000
                    print (total4)
                    jenis4 = ("Nasi Goreng")
                elif salah==102:
                    porsi4 = int(input("Jumlah: "))
                    total4 = total4 + porsi4*6000
                    print (total4)
                    jenis4 = ("Mi Goreng")
                elif salah == 103:
                    porsi4 = int(input("Jumlah: "))
                    total4 = total4 + porsi4*7000
                    print (total4)
                    jenis4 = ("Mi Rebus")
                elif salah == 104:
                    porsi4 = int(input("Jumlah: "))
                    total4 = total4 + porsi4*2000
                    print (total4)
                    jenis4 = ("Es teh")
                elif salah == 105:
                    porsi4 = int(input("Jumlah: "))
                    total4 = total4 + porsi4*3000
                    print (total4)
                    jenis4 = ("Es jeruk")
                else:
                    porsi4 = int(input("Jumlah: "))
                    total4 = total4 + porsi4*5000
                    print (total4)
                    jenis4 = ("Es Milo")
            print("""
        Apakah ada tambahan makanan?
        Ya (a)
        Tidak (b)
                  """)
            jawaban = input(" ")
            if jawaban == ("a"):
                print("Masukkan Menu Pilihan ke-5!")
                nomor = int(input("Menu yang Dipesan: "))
                menu = pilihan(nomor)
                print (menu)
                if nomor==101:
                    porsi5= int(input("Jumlah: "))
                    total5 = total5 + porsi5*10000
                    print (total5)
                    jenis5 = ("Nasi Goreng")
                elif nomor==102:
                    porsi5 = int(input("Jumlah: "))
                    total5 = total5 + porsi5*6000
                    print (total5)
                    jenis5 = ("Mi Goreng")
                elif nomor == 103:
                    porsi5= int(input("Jumlah: "))
                    total5 = total5 + porsi5*7000
                    print (total5)
                    jenis5 = ("Mi Rebus")
                elif nomor == 104:
                    porsi5 = int(input("Jumlah: "))
                    total5 = total5 + porsi5*2000
                    print (total5)
                    jenis5 = ("Es teh")
                elif nomor == 105:
                    porsi5 = int(input("Jumlah: "))
                    total5 = total5 + porsi5*3000
                    print (total5)
                    jenis5 = ("Es jeruk")
                elif nomor==106 :
                    porsi5= int(input("Jumlah: "))
                    total5 = total5 + porsi5*5000
                    print (total5)
                    jenis5 = ("Es Milo")
                else:
                    salah = int(input("""
      MENU TIDAK TERSEDIA!
SILAKAN MASUKKAN PESANAN ANDA : """))
                    if salah==101:
                        porsi5 = int(input("Jumlah: "))
                        total5 = total5 + porsi5*10000
                        print (total5)
                        jenis5 = ("Nasi Goreng")
                    elif salah==102:
                        porsi5 = int(input("Jumlah: "))
                        total5 = total5 + porsi5*6000
                        print (total5)
                        jenis5 = ("Mi Goreng")
                    elif salah == 103:
                        porsi5 = int(input("Jumlah: "))
                        total5 = total5 + porsi5*7000
                        print (total5)
                        jenis5 = ("Mi Rebus")
                    elif salah == 104:
                        porsi5 = int(input("Jumlah: "))
                        total5 = total5 + porsi5*2000
                        print (total5)
                        jenis5 = ("Es teh")
                    elif salah == 105:
                        porsi5 = int(input("Jumlah: "))
                        total5 = total5 + porsi5*3000
                        print (total5)
                        jenis5 = ("Es jeruk")
                    else:
                        porsi5 = int(input("Jumlah: "))
                        total5 = total5 + porsi5*5000
                        print (total5)
                        jenis5 = ("Es Milo")
                print("""
        Apakah ada tambahan makanan?
        Ya (a)
        Tidak (b)
                      """)
                jawaban = input(" ")
                if jawaban == ("a"):
                    print("Masukkan Menu Pilihan ke-6!")
                    nomor = int(input("Menu yang Dipesan: "))
                    menu = pilihan(nomor)
                    print (menu)
                    if nomor==101:
                        porsi6= int(input("Jumlah: "))
                        total6 = total6 + porsi6*10000
                        print (total6)
                        jenis6 = ("Nasi Goreng")
                        total = total1 + total2 + total3 + total4 + total5+ total6
                        print ("Total Harga: ",total)
                        uang = int(input("\nUang Tunai: Rp "))
                        print("\n===================================")
                        print("===============N O T A=============")
                        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                        print("===================================")
                        print("Nama      : ", nama)
                        print("Pembelian : ", porsi1, jenis1)
                        print("          : ", porsi2, jenis2)
                        print("          : ", porsi3, jenis3)
                        print("          : ", porsi4, jenis4)
                        print("          : ", porsi5, jenis5)
                        print("          : ", porsi6, jenis6)
                        print("Total     : Rp ", total)
                        print("Uang      : Rp ", uang)
                        akhir = int(uang-total)
                        print("Kembalian : Rp ",akhir)
                        print("-Kami tunggu kedatangannya kembali-")
                        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                                            
                    elif nomor==102:
                        porsi6 = int(input("Jumlah: "))
                        total6 = total6 + porsi6*6000
                        print (total6)
                        jenis6= ("Mi Goreng")
                        total = total1 + total2 + total3 + total4 + total5+ total6
                        print ("Total Harga: ",total)
                        uang = int(input("\nUang Tunai: Rp "))
                        print("\n===================================")
                        print("===============N O T A=============")
                        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                        print("===================================")
                        print("Nama      : ", nama)
                        print("Pembelian : ", porsi1, jenis1)
                        print("          : ", porsi2, jenis2)
                        print("          : ", porsi3, jenis3)
                        print("          : ", porsi4, jenis4)
                        print("          : ", porsi5, jenis5)
                        print("          : ", porsi6, jenis6)
                        print("Total     : Rp ", total)
                        print("Uang      : Rp ", uang)
                        akhir = int(uang-total)
                        print("Kembalian : Rp ",akhir)
                        print("-Kami tunggu kedatangannya kembali-")
                        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                        
                    elif nomor == 103:
                        porsi6= int(input("Jumlah: "))
                        total6 = total6 + porsi6*7000
                        print (total6)
                        jenis6 = ("Mi Rebus")
                        total = total1 + total2 + total3 + total4 + total5+ total6
                        print ("Total Harga: ",total)
                        uang = int(input("\nUang Tunai: Rp "))
                        print("\n===================================")
                        print("===============N O T A=============")
                        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                        print("===================================")
                        print("Nama      : ", nama)
                        print("Pembelian : ", porsi1, jenis1)
                        print("          : ", porsi2, jenis2)
                        print("          : ", porsi3, jenis3)
                        print("          : ", porsi4, jenis4)
                        print("          : ", porsi5, jenis5)
                        print("          : ", porsi6, jenis6)
                        print("Total     : Rp ", total)
                        print("Uang      : Rp ", uang)
                        akhir = int(uang-total)
                        print("Kembalian : Rp ",akhir)
                        print("-Kami tunggu kedatangannya kembali-")
                        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                        
                    elif nomor == 104:
                        porsi6 = int(input("Jumlah: "))
                        total6 = total6 + porsi6*2000
                        print (total6)
                        jenis6 = ("Es teh")
                        total = total1 + total2 + total3 + total4 + total5+ total6
                        print ("Total Harga: ",total)
                        uang = int(input("\nUang Tunai: Rp "))
                        print("\n===================================")
                        print("===============N O T A=============")
                        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                        print("===================================")
                        print("Nama      : ", nama)
                        print("Pembelian : ", porsi1, jenis1)
                        print("          : ", porsi2, jenis2)
                        print("          : ", porsi3, jenis3)
                        print("          : ", porsi4, jenis4)
                        print("          : ", porsi5, jenis5)
                        print("          : ", porsi6, jenis6)
                        print("Total     : Rp ", total)
                        print("Uang      : Rp ", uang)
                        akhir = int(uang-total)
                        print("Kembalian : Rp ",akhir)
                        print("-Kami tunggu kedatangannya kembali-")
                        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")   
                        
                    elif nomor == 105:
                        porsi6 = int(input("Jumlah: "))
                        total6 = total6 + porsi6*3000
                        print (total6)
                        jenis6 = ("Es jeruk")
                        total = total1 + total2 + total3 + total4 + total5+ total6
                        print ("Total Harga: ",total)
                        uang = int(input("\nUang Tunai: Rp "))
                        print("\n===================================")
                        print("===============N O T A=============")
                        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                        print("===================================")
                        print("Nama      : ", nama)
                        print("Pembelian : ", porsi1, jenis1)
                        print("          : ", porsi2, jenis2)
                        print("          : ", porsi3, jenis3)
                        print("          : ", porsi4, jenis4)
                        print("          : ", porsi5, jenis5)
                        print("          : ", porsi6, jenis6)
                        print("Total     : Rp ", total)
                        print("Uang      : Rp ", uang)
                        akhir = int(uang-total)
                        print("Kembalian : Rp ",akhir)
                        print("-Kami tunggu kedatangannya kembali-")
                        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                        
                    else :
                        porsi6= int(input("Jumlah: "))
                        total6 = total6 + porsi6*5000
                        print (total6)
                        jenis6 = ("Es Milo")
                        total = total1 + total2 + total3 + total4 + total5+ total6
                        print ("Total Harga: ",total)
                        uang = int(input("\nUang Tunai: Rp "))
                        print("\n===================================")
                        print("===============N O T A=============")
                        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                        print("===================================")
                        print("Nama      : ", nama)
                        print("Pembelian : ", porsi1, jenis1)
                        print("          : ", porsi2, jenis2)
                        print("          : ", porsi3, jenis3)
                        print("          : ", porsi4, jenis4)
                        print("          : ", porsi5, jenis5)
                        print("          : ", porsi6, jenis6)
                        print("Total     : Rp ", total)
                        print("Uang      : Rp ", uang)
                        akhir = int(uang-total)
                        print("Kembalian : Rp ",akhir)
                        print("-Kami tunggu kedatangannya kembali-")
                        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")

                elif jawaban == "b": 
                    total = total1 + total2 + total3 + total4 + total5
                    print ("Total Harga: ",total)
                    uang = int(input("\nUang Tunai: Rp "))
                    print("\n===================================")
                    print("===============N O T A=============")
                    print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                    print("===================================")
                    print("Nama      : ", nama)
                    print("Pembelian : ", porsi1, jenis1)
                    print("          : ", porsi2, jenis2)
                    print("          : ", porsi3, jenis3)
                    print("          : ", porsi4, jenis4)
                    print("          : ", porsi5, jenis5)
                    print("Total     : Rp ", total)
                    print("Uang      : Rp ", uang)
                    akhir = int(uang-total)
                    print("Kembalian : Rp ",akhir)
                    print("-Kami tunggu kedatangannya kembali-")
                    print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                else :
                    print("ERROR! Silakan ulangi")
            elif jawaban == "b" :
                total = total1 + total2 + total3 + total4
                print ("Total Harga: ",total)
                uang = int(input("\nUang Tunai: Rp "))
                print("\n===================================")
                print("===============N O T A=============")
                print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                print("===================================")
                print("Nama      : ", nama)
                print("Pembelian : ", porsi1, jenis1)
                print("          : ", porsi2, jenis2)
                print("          : ", porsi3, jenis3)
                print("          : ", porsi4, jenis4)
                print("Total     : Rp ", total)
                print("Uang      : Rp ", uang)
                akhir = int(uang-total)
                print("Kembalian : Rp ",akhir)
                print("-Kami tunggu kedatangannya kembali-")
                print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
            else :
                    print ("ERROR! Silakan ulangi")
        elif jawaban == "b":
                total = total1 + total2 + total3
                print ("Total Harga: ",total)
                uang = int(input("\nUang Tunai: Rp "))
                print("\n===================================")
                print("===============N O T A=============")
                print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
                print("===================================")
                print("Nama      : ", nama)
                print("Pembelian : ", porsi1, jenis1)
                print("          : ", porsi2, jenis2)
                print("          : ", porsi3, jenis3)
                print("Total     : Rp ", total)
                print("Uang      : Rp ", uang)
                akhir = int(uang-total)
                print("Kembalian : Rp ",akhir)
                print("-Kami tunggu kedatangannya kembali-")
                print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")   
        else :
                print("ERROR! Silakan ulangi")
    elif jawaban == "b":
        total = total1 + total2
        print ("Total Harga: ",total)
        uang = int(input("\nUang Tunai: Rp "))
        print("\n===================================")
        print("===============N O T A=============")
        print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
        print("===================================")
        print("Nama      : ", nama)
        print("Pembelian : ", porsi1, jenis1)
        print("          : ", porsi2, jenis2)
        print("Total     : Rp ", total)
        print("Uang      : Rp ", uang)
        akhir = int(uang-total)
        print("Kembalian : Rp ",akhir)
        print("-Kami tunggu kedatangannya kembali-")
        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
    else :
        print ("ERROR! Silakan ulangi")
elif jawaban == "b" :
    total = total1
    print ("Total Harga: ",total)
    uang = int(input("\nUang Tunai: Rp "))
    print("\n=====================================")
    print("===============N O T A===============")
    print("=RESTORAN MURAH MERIAH PAS DI KANTONG=")
    print("=====================================")
    print("Nama      : ", nama)
    print("Pembelian : ", porsi1, jenis1)
    print("Total     : Rp ", total)
    print("Uang      : Rp ", uang)
    akhir = int(uang-total)
    print("Kembalian : Rp ",akhir)
    print("-Kami tunggu kedatangannya kembali-")
    print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")   
else :
    print ("ERROR! Silakan ulangi")
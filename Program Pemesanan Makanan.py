import sys

def menuawal():
    print("""
    ================SELAMAT DATANG==================
                      L'appetito
    Jl Kebangkitan No. 49, Kec. Laweyan, Kota Surakarta
                  Telp. (0271) 844425""")
menuawal()

def makanan():
    global list_makanan
    global list_jumlah_makanan
    global list_total_makanan
    list_makanan = []
    list_jumlah_makanan = []
    list_total_makanan = []
    n = "baka"
    print("""
    ==================MENU MAKANAN==================

    1.  Fettucinne Carbonara            :  Rp 35.000
    2.  Lasagna                         :  Rp 10.000
    3.	Spaghetti Bolognese             :  Rp 30.000
    4.	Mac n cheese                    :  Rp 35.000
    5.	Pasta Chicken alfredo           :  Rp 30.000
    6.	Garlic bread                    :  Rp 20.000
    7.	Pizza cheese chicken alfredo    :  Rp 60.000
    8.	Pizza super supreme             :  Rp 55.000
    9.	Pizza tuna melt                 :  Rp 53.500
    10.	Pizza meat lover                :  Rp 55.000
    11.	Bruschetta                      :  Rp 25.000
    12.	Cheezy chicken quesadillas      :  Rp 33.000
    13.	Fish n chips                    :  Rp 32.000
    14.	Chicken parmigiana              :  Rp 35.000
    15.	Italian meatballs               :  Rp 33.000
    Tekan ENTER untuk lanjut ke menu selanjutnya
    """)
    while n != 6:
        print("Pilih Menu Makanan (1-15)")
        x = input(">> ")
        if x == "1":
            jenis = "Fettucinne Carbonara"
            harga = "Rp 35.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 35000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "2":
            jenis = "Lasagna"
            harga = "Rp 10.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 10000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "3":
            jenis = "Spaghetti Bolognese"
            harga = "Rp 30.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 30000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "4":
            jenis = "Mac n cheese"
            harga = "Rp 35.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 35000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "5":
            jenis = "Pasta Chicken alfredo"
            harga = "Rp 30.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 30000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "6":
            jenis = "Garlic bread"
            harga = "Rp 20.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 20000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "7":
            jenis = "Pizza cheese chicken alfredo"
            harga = "Rp 60.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 60000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "8":
            jenis = "Pizza super supreme"
            harga = "Rp 55.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 55000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "9":
            jenis = "Pizza tuna melt"
            harga = "Rp 53.500"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 53500 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "10":
            jenis = "Pizza meat lover"
            harga = "Rp 55.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 55000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "11":
            jenis = "Bruschetta"
            harga = "Rp 25.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 25000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "12":
            jenis = "Cheezy chicken quesadillas"
            harga = "Rp 33.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 33000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "13":
            jenis = "Fish n chips"
            harga = "Rp 32.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 32000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "14":
            jenis = "Chicken parmigiana"
            harga = "Rp 35.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 35000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "15":
            jenis = "Italian meatballs"
            harga = "Rp 33.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_makanan.append(jenis)
            list_jumlah_makanan.append(jumlah)
            total_makanan = 33000 * jumlah
            list_total_makanan.append(total_makanan)
            print("Total harga : ", total_makanan)
            print()
        elif x == "":
            print("Mohon Tunggu ...")
            print()
            n = 6
        else:
            print("TIDAK VALID. SILAHKAN COBA LAGI.")
            print()
            makanan()
            sys.exit()
    print("Total Harga Makanan : ", sum(list_total_makanan))
    print()
makanan()

def minuman():
    global list_minuman
    global list_jumlah_minuman
    global list_total_minuman
    list_minuman = []
    list_jumlah_minuman = []
    list_total_minuman = []
    n = "baka"
    print("""
    ==================MENU MINUMAN==================
    1.	Squash delight      =   Rp 15.000
    2.	Blue ocean          =   Rp 15.000
    3.	Orange soda         =   Rp 15.000
    4.	Yakult mojito       =   Rp 17.000
    5.	Fruit punch         =   Rp 17.000
    6.	Strawberry mojito   =   Rp 17.000
    7.	Fizzy drink         =   Rp 15.000
    8.	Lemon float         =   Rp 17.000
    9.	Melon soda float    =   Rp 18.000
    10.	Mango float         =   Rp 18.000
    Tekan ENTER untuk lanjut ke menu selanjutnya
    """)
    while n != 6:
        print("Pilih Menu Minuman (1-10)")
        x = input(">> ")
        if x == "1":
            jenis = "Squash delight"
            harga = "Rp 15.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 15000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "2":
            jenis = "Blue ocean"
            harga = "Rp 15.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 15000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "3":
            jenis = "Orange soda"
            harga = "Rp 15.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 15000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "4":
            jenis = "Yakult mojito"
            harga = "Rp 17.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 17000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "5":
            jenis = "Fruit punch"
            harga = "Rp 17.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 17000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "6":
            jenis = "Strawberry mojito"
            harga = "Rp 17.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 17000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "7":
            jenis = "Fizzy drink"
            harga = "Rp 15.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 15000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "8":
            jenis = "Lemon float"
            harga = "Rp 17.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 17000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "9":
            jenis = "Melon soda float"
            harga = "Rp 18.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 18000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "10":
            jenis = "Mango float"
            harga = "Rp 18.000"
            print(jenis)
            print(harga)
            jumlah = int(input("Jumlah : "))
            list_minuman.append(jenis)
            list_jumlah_minuman.append(jumlah)
            total_minuman = 18000 * jumlah
            list_total_minuman.append(total_minuman)
            print("Total harga : ", total_minuman)
            print()
        elif x == "":
            print("Mohon Tunggu ...")
            print()
            n = 6
        else:
            print("TIDAK VALID. SILAHKAN COBA LAGI.")
            print()
            minuman()
            sys.exit()
    print("Total Harga Minuman : ", sum(list_total_minuman))
    print()
minuman()
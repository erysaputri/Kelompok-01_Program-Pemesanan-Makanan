import datetime
import time
import random


def menuawal():
    print("""
    ================SELAMAT DATANG==================
                      L'appetito
    Jl Kebangkitan No. 49, Kec. Laweyan, Kota Surakarta
                  Telp. (0271) 844425""")


menuawal()


# noinspection PyGlobalUndefined
def makanan():
    global list_makanan
    global list_jumlah_makanan
    global list_total_makanan
    list_makanan = []
    list_jumlah_makanan = []
    list_total_makanan = []
    n = "baka"
    print("""
====================MENU MAKANAN====================

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
        # Pengguna menginput nomor menu makanan yang dipesan
        x = input(">> ")
        if x == "1":
            jenis = "Fettucinne Carbonara"
            harga = "Rp 35.000"
            print(jenis)
            print(harga)
            # Pengguna menginput jumlah makanan yang di pesan
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
    print("Total Harga Makanan : ", sum(list_total_makanan))
    print()


makanan()


# noinspection PyGlobalUndefined
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
    1.	Squash delight      :   Rp 15.000
    2.	Blue ocean          :   Rp 15.000
    3.	Orange soda         :   Rp 15.000
    4.	Yakult mojito       :   Rp 17.000
    5.	Fruit punch         :   Rp 17.000
    6.	Strawberry mojito   :   Rp 17.000
    7.	Fizzy drink         :   Rp 15.000
    8.	Lemon float         :   Rp 17.000
    9.	Melon soda float    :   Rp 18.000
    10.	Mango float         :   Rp 18.000
    Tekan ENTER untuk lanjut ke menu selanjutnya
    """)
    while n != 6:
        print("Pilih Menu Minuman (1-10)")
        # Pengguna menginput menu minuman yang dipesan
        x = input(">> ")
        if x == "1":
            jenis = "Squash delight"
            harga = "Rp 15.000"
            print(jenis)
            print(harga)
            # Pengguna menginput jumlah minuman yang dipesan
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
    print("Total Harga Minuman : ", sum(list_total_minuman))
    print()


minuman()


# noinspection PyGlobalUndefined
def total_sementara():
    global total_harga
    total_harga = sum(list_total_makanan) + sum(list_total_minuman)
    print("Total Harga : Rp", total_harga)


total_sementara()


def cek_pesanan():
    print()
    print("Apakah anda sudah yakin (Y/N)")
    # Pengguna menginput Y jika sudah yakin dengan pesan dan N jika belum yakin
    cek1 = input(">> ")
    if cek1 == "Y":
        print()
        print("Mohon Tunggu ...")
    elif cek1 == "N":
        makanan()
        minuman()
        total_sementara()
        cek_pesanan()
    else:
        print("TIDAK VALID. SILAHKAN COBA LAGI.")
        cek_pesanan()


cek_pesanan()


# noinspection PyGlobalUndefined
def dine_in():
    global nama_pemesan
    global no_meja
    global ongkos_kirim
    print("Anda memilih Dine In")
    # Pengguna menginput nama pembeli
    nama_pemesan = input("Nama : ")
    no_meja = random.randint(1, 20)
    ongkos_kirim = 0
    print("No Meja : ", no_meja)


# noinspection PyGlobalUndefined
def take_away():
    global nama_pengambil
    global no_antrian
    global ongkos_kirim
    print("Anda memilih Take Away")
    # Pengguna menginput nama pengambil pesanan
    nama_pengambil = input("Nama Pengambil : ")
    no_antrian = random.randint(1, 30)
    ongkos_kirim = 0
    print("No Antrian : ", no_antrian)


# noinspection PyGlobalUndefined
def delivery():
    global nama_penerima
    global no_telfon
    global alamat
    global kecamatan
    global ongkos_kirim
    print("Anda memilih Delivery (Khusus Kota Solo)")
    # Pengguna menginput identitas
    nama_penerima = input("Nama Penerima : ")
    no_telfon = int(input("No Telfon : "))
    alamat = input("Alamat : ")
    kecamatan = input("Kecamatan : ")
    if kecamatan == "Laweyan":
        ongkos_kirim = 6000
        print("Total Ongkos Kirim : ", ongkos_kirim)
    elif kecamatan == "Pasar Kliwon":
        ongkos_kirim = 7000
        print("Total Ongkos Kirim : ", ongkos_kirim)
    elif kecamatan == "Jebres":
        ongkos_kirim = 8000
        print("Total Ongkos Kirim : ", ongkos_kirim)
    elif kecamatan == "Banjarsari":
        ongkos_kirim = 9000
        print("Total Ongkos Kirim : ", ongkos_kirim)
    elif kecamatan == "Serengan":
        ongkos_kirim = 10000
        print("Total Ongkos Kirim : ", ongkos_kirim)
    else:
        print("TIDAK VALID. SILAHKAN COBA LAGI.")
        delivery()


# noinspection PyGlobalUndefined
def menu_2():
    global menu
    global pesanan
    print("""
===============MENU PILIHAN===============

1. Dine In
2. Take Away
3. Delivery (Khusus Kota Solo)
""")
    menu = "baka"
    while menu != "s":
        # Pengguna menginput menu pilihan sesuai keinginan
        menu = input(">> ")
        print()
        if menu == "1" or menu == "2" or menu == "3":
            if menu == "1":
                pesanan = "1"
                menu = "s"
                dine_in()
            elif menu == "2":
                take_away()
                pesanan = "2"
                menu = "s"
            elif menu == "3":
                pesanan = "3"
                menu = "s"
                delivery()
        else:
            print("TIDAK VALID. SILAHKAN COBA LAGI.")
            menu_2()


menu_2()


# noinspection PyGlobalUndefined
def total_bayar():
    global total_bayar
    total_bayar = total_harga + ongkos_kirim
    print("Total yang harus dibayarkan : ", total_bayar)


total_bayar()


def detail_pembelian():
    print()
    print("Detail Pembelian :")
    print()
    if pesanan == "1":
        t = time.localtime()
        jam_sekarang = time.strftime("%H:%M:%S", t)
        print("Tanggal pesan  : ", datetime.date.today())
        print("Jam pesan      : ", jam_sekarang)
        print("Nama           : ", nama_pemesan)
        print("No meja        : ", no_meja)
    elif pesanan == "2":
        t = time.localtime()
        jam_sekarang = time.strftime("%H:%M:%S", t)
        print("Tanggal pesan  : ", datetime.date.today())
        print("Jam pesan      : ", jam_sekarang)
        print("Nama           : ", nama_pengambil)
        print("No antrian     : ", no_antrian)
        print("Note           :  Pesanan dapat diambil setelah 30 menit")
    else:
        t = time.localtime()
        jam_sekarang = time.strftime("%H:%M:%S", t)
        print("Tanggal pesan  : ", datetime.date.today())
        print("Jam pesan      : ", jam_sekarang)
        print("Nama           : ", nama_penerima)
        print("Alamat         : ", alamat)
        print("Ongkos Kirim   :  Rp ", ongkos_kirim)
    print()


detail_pembelian()


def detail_pesanan():
    print("Pesanan :")
    print("Makanan              : ", list_makanan)
    print("Jumlah               : ", list_jumlah_makanan)
    print("Harga Makanan        : ", list_total_makanan)
    print("Total Harga Makanan  :  Rp ", sum(list_total_makanan))
    print("Minuman              : ", list_minuman)
    print("Jumlah               : ", list_jumlah_minuman)
    print("Harga Minuman        : ", list_total_minuman)
    print("Total Harga Minuman  :  Rp ", sum(list_total_minuman))
    print("Total                :  Rp ", sum(list_total_makanan) + sum(list_total_minuman) + ongkos_kirim)
    print()


detail_pesanan()


def cek():
    print("Apakah anda sudah yakin? (Y/N)")
    # Memastikan pelanggan sudah yakin dengan pesanan
    yakin = input(">> ")
    print()
    if yakin == "Y":
        print("Mohon Tunggu ...")
    elif yakin == "N":
        makanan()
        minuman()
        total_sementara()
        cek_pesanan()
        menu_2()
        total_bayar()
        detail_pembelian()
        detail_pesanan()
        cek()
    else:
        print("TIDAK VALID. SILAHKAN COBA LAGI.")
        cek()


cek()


# noinspection PyGlobalUndefined
def cashless():
    global no_dana
    print("Masukkan Nomor DANA")
    # Pengguna menginput nomer akun DANA
    no_dana = int(input(">> "))
    print("Total Pembayaran : Rp", total_bayar)
    print()
    print("Apakah anda yakin ingin melanjutkan? (Y/N)")
    cek_cashless = input(">> ")
    print()
    if cek_cashless == "N":
        cashless()
    else:
        print("Pembayaran Telah Terkonfirmasi")


def cash():
    print("Anda memilih pembayaran cash")


def rekening():
    print("Silahkan Melakukan Transfer ke Rekening 741248083624 a.n. Bastian Arya\n")
    print("Apakah anda sudah melakukan pembayaran? (Y/N)")
    cek_rekening = input(">> ")
    # Mengkonfirmasi bahwa pelanggan sudah transfer
    if cek_rekening == "Y":
        t = 5
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print()
        print("Pembayaran Telah Terkonfirmasi")
    elif cek_rekening == "N":
        rekening()
    else:
        print("TIDAK VALID. SILAHKAN COBA LAGI.")


# noinspection PyGlobalUndefined
def pembayaran():
    global bayar
    print("""
================MENU PEMBAYARAN================

    1.	Cash
    2.	DANA
    3.  Transfer Bank
    """)
    bayar = "baka"
    while bayar != "s":
        # Pengguna menginput metode pembayaran
        bayar = input(">> ")
        print()
        if bayar == "1" or bayar == "2" or bayar == "3":
            if bayar == "1":
                bayar = "s"
                cash()
            elif bayar == "2":
                bayar = "s"
                cashless()
            elif bayar == "3":
                bayar = "s"
                rekening()
        else:
            print("TIDAK VALID. SILAHKAN COBA LAGI.")
            pembayaran()


pembayaran()


def menu_akhir():
    print()
    print("Terima kasih telah memesan di restoran kami. Pesanan Anda sedang kami proses.")


menu_akhir()

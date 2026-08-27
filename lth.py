#case1
def cek_stok(jumlah):
    if jumlah > 100:
        print("Peringatan: Stok kurang, maksimal ambil 100!")
    else:
        print("Aman, barang siap dikirim!")

#case2
def potong_pesan(pesan):
    layar = len(pesan)
    if layar > 10:
        print(pesan[:10] + "...")
    else:
        print(pesan)

def bagi_harta(total_gold, jumlah_tim):
    try:
        hasil = total_gold / jumlah_tim
        print(hasil)
    except:
        print("Gagal: Anggota tim nggak boleh nol!")

bagi_harta(5000, 0)
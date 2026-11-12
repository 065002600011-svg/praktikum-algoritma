#065002600012
#Ghilman Ilmi Setiawan
def jumlahkan(n, i=1):
    if i > n:
        return 0
    angka = int(input(f"Masukkan bilangan ke-{i}: "))
    return angka + jumlahkan(n, i + 1)

jumlah = int(input("Masukkan Jumlah: "))
hasil = jumlahkan(jumlah)
print("Hasil dari penjumlahan adalah:", hasil)

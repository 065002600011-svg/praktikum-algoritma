#065002600011
#Ghilman Ilmi setiawan
def hitung_faktor(n):
    """Menghitung jumlah faktor (pembagi) dari bilangan n."""
    jumlah = 0
    for i in range(1, n + 1):
        if n % i == 0:
            jumlah += 1
    return jumlah


def cek_prima(angka):
    """Mengembalikan True jika angka adalah bilangan prima."""
    if angka < 2:
        return False
    return hitung_faktor(angka) == 2


# Program utama (perulangan)
while True:
    try:
        angka = int(input("Masukkan angka: "))
    except ValueError:
        print("Input tidak valid, masukkan bilangan bulat!\n")
        continue

    if cek_prima(angka):
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")

    lagi = input("Coba lagi? (y/n): ").lower()
    if lagi != "y":
        print("Terima kasih, program selesai.")
        break
    print()

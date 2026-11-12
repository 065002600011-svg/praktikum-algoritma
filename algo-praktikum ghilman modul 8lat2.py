#065002600011
#Ghilman Ilmi Setiawan
def pangkat(base, power):
    if power == 0:
        return 1
    if power < 0:
        return 1 / pangkat(base, -power)
    return base * pangkat(base, power - 1)

def program():
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    angka = input("Masukkan Angka: ")
    if angka == "":
        print("Program Selesai")
        return
    power = int(input("Masukkan Pangkatnya: "))
    hasil = pangkat(float(angka), power)
    if hasil == int(hasil):
        hasil = int(hasil)
    print("Hasilnya adalah:", hasil)
    print()
    program()

program()

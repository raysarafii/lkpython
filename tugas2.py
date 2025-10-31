def input_angka():
    data = input("Masukkan daftar angka (pisahkan dengan koma): ")
    try:
        angka = [float(x.strip()) for x in data.split(",")]
        return angka
    except ValueError:
        print("Input tidak valid. Pastikan hanya angka yang dipisahkan dengan koma.")
        return None

def hitung_rata_rata(angka):
    return sum(angka) / len(angka)

def hitung_genap_ganjil(angka):
    genap = sum(1 for x in angka if x % 2 == 0)
    ganjil = len(angka) - genap
    return genap, ganjil

def tampilkan_hasil(angka):
    print(f"Rata-rata: {hitung_rata_rata(angka):.2f}")
    print(f"Maksimum: {max(angka)}")
    print(f"Minimum: {min(angka)}")
    print(f"Jumlah angka: {len(angka)}")
    genap, ganjil = hitung_genap_ganjil(angka)
    print(f"Angka genap: {genap}")
    print(f"Angka ganjil: {ganjil}")

def main():
    angka = input_angka()
    if angka:
        tampilkan_hasil(angka)

if __name__ == "__main__":
    main()

def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa berdasarkan NIM")
    print("4. Hapus Mahasiswa berdasarkan NIM")
    print("5. Keluar")

def tambah_mahasiswa(data_mahasiswa):
    nim = input("Masukkan NIM: ").strip()
    if nim in data_mahasiswa:
        print("Gagal! NIM sudah terdaftar.")
        return
    nama = input("Masukkan Nama: ").strip()
    prodi = input("Masukkan Program Studi: ").strip()
    try:
        ipk = float(input("Masukkan IPK: "))
        if ipk < 0 or ipk > 4:
            print("IPK harus antara 0.00 - 4.00")
            return
    except ValueError:
        print("IPK harus berupa angka desimal.")
        return
    data_mahasiswa[nim] = {"nama": nama, "prodi": prodi, "ipk": ipk}
    print("Mahasiswa berhasil ditambahkan.")

def tampilkan_semua(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    print("\n=== Daftar Mahasiswa ===")
    for nim, info in data_mahasiswa.items():
        print(f"NIM: {nim}")
        print(f"Nama: {info['nama']}")
        print(f"Prodi: {info['prodi']}")
        print(f"IPK: {info['ipk']:.2f}")
        print("-" * 30)

def cari_mahasiswa(data_mahasiswa):
    nim = input("Masukkan NIM yang dicari: ").strip()
    if nim not in data_mahasiswa:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
        return
    info = data_mahasiswa[nim]
    print("\n=== Data Mahasiswa Ditemukan ===")
    print(f"NIM   : {nim}")
    print(f"Nama  : {info['nama']}")
    print(f"Prodi : {info['prodi']}")
    print(f"IPK   : {info['ipk']:.2f}")

def hapus_mahasiswa(data_mahasiswa):
    nim = input("Masukkan NIM yang akan dihapus: ").strip()
    if nim not in data_mahasiswa:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
        return
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus data {nim}? (y/n): ").lower()
    if konfirmasi == 'y':
        del data_mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def main():
    data_mahasiswa = {}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tambah_mahasiswa(data_mahasiswa)
        elif pilihan == "2":
            tampilkan_semua(data_mahasiswa)
        elif pilihan == "3":
            cari_mahasiswa(data_mahasiswa)
        elif pilihan == "4":
            hapus_mahasiswa(data_mahasiswa)
        elif pilihan == "5":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()

# Header
print("")
print("="*50)
judul = "Soal 1 : Fungsi strings"
center = judul.center(50)
print(center)
print("="*50)
print("")

print("\t\t\tProgram pemeriksa pergantian kelas mahasiswa fakultas teknik")

Nama = input("Silahkan masukkan nama Anda: ")
Nama1 = Nama.upper()
print(Nama1)
Prodi = input("Silahkan masukkan prodi Anda:")
Prodi1 = Prodi.capitalize()
print(Prodi1)
Waktu = input("Silahkan pilih waktu kelas:(Pukul 08.15/Pukul 10.05/Pukul 11.40/Pukul 14.15/Pukul 16.45)")
print(Waktu)
Kelas = input("Silahkan masukkan kelas Anda:(A/B/C)").upper()
print("Kelas A berganti dengan= ", Kelas.replace("A", "C"))
print("Kelas B berganti dengan= ", Kelas.replace("B", "A"))
print("Kelas C berganti dengan= ", Kelas.replace("C", "B"))

# Footer
print("")
print("="*50)
penutup = "Program Selesai"
center = penutup.center(50)
print(center)
print("="*50)
print("")

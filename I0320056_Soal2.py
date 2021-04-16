# Header
print("")
print("="*50)
judul = "Soal 1 : Fungsi numerik"
center = judul.center(50)
print(center)
print("="*50)
print("")

import math
print("\t\t\tProgram pemeriksa nilai mahasiswa")
nilai = input("Silahkan masukkan nilai mahasiswa (dipisahkan dengan spasi) : ").split()

for i in range(len(nilai)):
    nilai[i] = int(nilai[i])
rata_rata = sum(nilai)/len(nilai)
print("Nilai yang diinput : ", nilai)
print('\n')
print("Nilai tertinggi adalah ", max(nilai))
print("Nilai terendah adalah ", min(nilai))
print("Rata-rata nilai mahasiswa adalah ", rata_rata)
print("Rata-rata nilai dengan pembulatan ke atas adalah ", math.ceil(rata_rata))
print("Rata-rata nilai dengan pembulatan ke bawah adalah ", math.floor(rata_rata))

# Footer
print("")
print("="*50)
penutup = "Program Selesai"
center = penutup.center(50)
print(center)
print("="*50)
print("")

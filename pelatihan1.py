Nama_saya = "Nama saya Mahrus"
print(Nama_saya,"bertipe", type(Nama_saya))
Umur_saya = 19
print(Umur_saya, "bertipe", type(Umur_saya))
IPK = 4.00
print(IPK, "bertipe", type(IPK))
Menikah = False
print(Menikah, "bertipe", type(Menikah))
Matkul_yang_diambil1 = ["Alpro", "SIG"]
print("Matkul", Matkul_yang_diambil1, "bertipe", type(Matkul_yang_diambil1))
Matkul_yang_diambil2 = ("PTIK", "LE")
print("Matkul lain : ", Matkul_yang_diambil2, "bertipe", type(Matkul_yang_diambil2))
Matkul_yang_diambil3 = {"SO", "Etika Profesi"}
print("Matkul lainnya : ", Matkul_yang_diambil3, "bertipe", type(Matkul_yang_diambil3))

print()

print(33 + 5)
print(33 - 5)
print(33 * 5)
print(33 / 5)
print(33 // 5)
print(33 % 5)


print()

Nama_saya = str(input("Masukkan Nama = " ))
Umur_saya = int(input("Masukkan Umur = "))
IPK = float(input("Masukkan IPK = "))
Menikah = bool(input("Masukkan Menikah = "))
Matkul_yang_diambil = list(input("Masukkan Matkul1 = "))
Matkul_yang_diambil = tuple(input("Masukkan Matkul2 = "))
Matkul_yang_diambil = set(input("Masukkan Matkul3 = "))
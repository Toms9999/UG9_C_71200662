kecepatan = int(input ("Masukan kecepatan tempuh :"))
waktu = int(input ("Masukan waktu yang diperlukan :"))

bensin = kecepatan*waktu/10
biaya = bensin*15000
print("Teman Anda mengisi bensin sebanyak", bensin,"liter")
print("Biaya yang dikeluarkan untuk mengisi bensin adalah Rp.",biaya)

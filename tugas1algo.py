totaldetik = int(input("Masukkan totaldetik: "))

hari = totaldetik // 86400
sisahari = totaldetik % 86400

jam = sisahari // 86400
sisajam = sisahari % 3600

menit = sisajam // 60
detik = sisajam % 60

print("Hasil Konversi :", totaldetik, "Detik Adalah", hari, "hari", jam, "jam", menit, "menit", detik, "Detik")
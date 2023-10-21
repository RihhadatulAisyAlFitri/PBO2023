print ("Menghitung Luas & Volume Kerucut")

# variabel
jari_jari = 2
tinggi = 4

# rumus
luas = 3.14 * jari_jari * (jari_jari + ((tinggi **2) + (jari_jari **2)) ** 0.5)
volume = 1/3 * 3.14 * jari_jari** 2 * tinggi

# output
print ("Luas = ", luas)
print("Volume = ", volume) 

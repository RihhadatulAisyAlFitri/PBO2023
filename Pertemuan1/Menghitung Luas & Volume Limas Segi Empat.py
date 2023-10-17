print("Menghitung Luas & Volume Limas Segi Empat")

# variabel
panjang_alas = 4
lebar_alas = 2
tinggi_alas = 5
tinggi_limas = 1

# rumus 
luas = (panjang_alas * lebar_alas) + 2 * ((panjang_alas * tinggi_limas/2) + (lebar_alas * tinggi_limas / 2))
volume = (panjang_alas * lebar_alas * tinggi_alas * tinggi_limas) / 3

# output
print(" Luas = ", luas)
print("Volume = ", volume ) 
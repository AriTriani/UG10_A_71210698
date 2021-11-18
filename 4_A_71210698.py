X = input("Masukkan Artikel yang Ingin Dipindai: ")
Y = input("Masukkan nama klub favorit anda: ")
Z = input("Masukkan skor yang ingin dicari: ")

if Y+X and Z+X:
    print("Hasil pencarian ditemukan")
elif Y+X:
    print("Hanya",Y,"yang ditemukan pada artikel ini")
elif Z+X:
    print("Hanya skor",Z,"yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",Y,"dan",Z,"tidak ditemukan")
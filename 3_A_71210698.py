X = input("Mendatar/Menurun?: ")
if X == "Mendatar":
    Y = int(input("Masukkan kolom: "))
    print("#"*Y)
elif X == "Menurun":
    Y = int(input("Masukkan baris: "))
    print("*\n"*Y)
else:
    print("Pola tidak dikenali")
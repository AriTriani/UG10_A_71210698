print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

X = int(input("masukkan menu yang anda pilih: "))
if X == 1:
    h = int(input("Masukkan bilangan yang ingin dibagi: "))
    i = int(input("Masukkan bilangan pembagi: "))
    j = int(h%i)
    print("Sisa hasil bagi",float(h),"dibagi dengan",float(i),"adalah",float(j))
elif X==2:
    h = int(input("Masukkan bilangan yang ingin dibagi: "))
    i = int(input("Masukkan bilangan pembagi: "))
    j = int(round(h/i,1))
    print("Hasil pembagian",float(h),"dibagi dengan",float(i),"dibulatkan kebawah adalah",float(j))
elif X==3:
    h = int(input("Masukkan bilangan yang ingin dicari akar kubiknya"))
    i = int(x**(1/3))
    print("Akar kubik dari",float(h),"adalah",float(i))
else: 
    print("Menu yang anda pilih tidak tersedia")


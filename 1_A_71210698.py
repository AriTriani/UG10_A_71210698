N1 = float(input("Masukkan nilai rata-rata UG anda: "))
N2 = float(input("Masukkan nilai TTS anda: "))
N3 = float(input("Masukkan nilai TAS anda: "))
print ("========================")

A = N1*70/100
B = N2*15/100
C = N3*15/100
Hasil = float(A+B+C)
print("Nilai anda: ", Hasil)
if Hasil >= 85:
    print("Nilai huruf anda: A")
elif Hasil >= 80:
    print("Nilai huruf anda: A-")
elif Hasil >= 75:
    print("Nilai huruf anda: B+")
elif Hasil >= 70:
    print("Nilai huruf anda: B")
elif Hasil >= 65:
    print("Nilai huruf anda: B-")
elif Hasil >= 60:
    print("Nilai huruf anda: C+")
elif Hasil >= 55:
    print("Nilai huruf anda: C")
elif Hasil >= 45:
    print("Nilai huruf anda: D")
else:
    print("Nilai huruf anda: E")
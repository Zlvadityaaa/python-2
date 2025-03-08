# 2. Menghitung nilai rata-rata seorang siswa dari 5 mata pelajaran (IPA, IPS, MTK, English, Indonesia)
ipa = int(input("masukan nilai IPA :"))
ips = int(input("masukan nilai IPS :"))
mtk = int(input("masukan nilai MTK :"))
english = int(input("masukan nilai English :"))
indonesia = int(input("masukan nilai Indonesia :"))

rata_rata_1 = (ipa + ips + mtk + english + indonesia) / 5

nilai = [ipa, ips, mtk, english, indonesia]

print(f"Rata-rata nilai seorang siswa dari 5 mata pelajaran adalah {rata_rata_1}")

# 3. Mengecek nilai Lulus atau Tidak Lulus dengan Kriteria
# - Dinyatakan Lulus, jika rata-rata dari semuanya lebih dari 75, atau
# - Dinyatakan Lulus, jika hanya 2 mata pelajaran yang nilainya dibawah 50, atau
# - Mendapatkan nilai sempurna (100) dari salah satu mata pelajaran

nilai_di_bawah_50 = 0

if (ipa < 50):
    nilai_di_bawah_50 += 1
if (ips < 50):
    nilai_di_bawah_50 += 1
if (mtk < 50):
    nilai_di_bawah_50 += 1
if (english < 50):
    nilai_di_bawah_50 += 1
if (indonesia < 50):
    nilai_di_bawah_50 += 1

if (rata_rata_1 > 75):
    print("Lulus, karna rata-rata nilai lebih dari 75")
elif (nilai.count(100) > 0):
    print("Lulus, karna mendapatkan nilai sempurna dari salah satu mata pelajaran")
elif (nilai_di_bawah_50 == 2):
    print("Lulus, karna hanya 2 mata pelajaran yang nilainya dibawah 50")
else:
    print("Tidak Lulus")

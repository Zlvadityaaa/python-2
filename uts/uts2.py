nama = "NUGRAHA"
if len (nama) < 7:
    print("minimal 7 karakter, kalo tidak ada boleh ditambah yang lain")
else:
    for i in range(len(nama)):
    
        print(nama[:i + 1] + '*' * (7 - (i + 1) ))



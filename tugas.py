nama = str(input("masukan nama : "))
usia = int(input("masukan usia : "))
ipk = float(input("masukan ipk contoh (3.5) : "))
fc_ijazah = str(input ("fc ijazah(sudah / belum) : "))
skl = str(input("surat keterangan sehat(sudah / belum) : "))
if(nama and usia>= 24 and ipk>=2.7 and fc_ijazah=="sudah" and skl=="sudah"):
    print("Selamat",nama,"dengan usia", usia,"dengan skl",skl," diterima menjadi PNS")
else:
    print("Maaf anda belum diterima menjadi PNS")
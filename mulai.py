import os
os.system("clear")

domain = input("Masukan Domain: ")

#os.system("cd")
#os.system("cd storage/downloads/scanws/scanws")
os.system(f"python findthesub.py -d {domain} -o xyz.txt")

#scan ws dan ping
import os

print("\n\nGANTI PAKET DATA DULU\n.")

# Menampilkan konfirmasi "Sudah Ganti Paket Data?"
confirmation = input("Sudah Ganti Paket Data? (y/n): ")

# Jalankan perintah hanya jika pengguna mengkonfirmasi dengan "y" atau "Y"
if confirmation.lower() == "y":
    # Jalankan perintah scanws.py
    os.system("python scanws.py -f xyz.txt -o x1.txt")

    # Jalankan perintah ping.py
    os.system("python ping.py")
else:
    print("Paket Data belum diganti.")
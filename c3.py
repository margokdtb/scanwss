# Membuka file hasil3.txt
with open("hasil3.txt", "r") as file:
    lines = file.readlines()

# Menghapus tanda kutip tunggal ('), tulisan 'Status', dan tanda koma (,) dari setiap baris
cleaned_lines = []
for line in lines:
    # Mengganti tanda kutip tunggal ('), tulisan 'Status', dan tanda koma (,) dengan string kosong
    cleaned_line = line.replace("'", "").replace("Status", "").replace(",", "").strip()
    cleaned_lines.append(cleaned_line)

# Menyimpan hasil ke file hasil4.txt
with open("hasil4.txt", "w") as file:
    for line in cleaned_lines:
        file.write(line + "\n")

print("Pemrosesan selesai. Hasil disimpan di file hasil4.txt")
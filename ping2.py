import subprocess
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

ip_addresses = []

# Baca alamat IP dari file txt
with open('hasil2.txt', 'r') as file:
    ip_addresses = file.read().splitlines()

results = []

# Fungsi untuk menjalankan perintah ping pada setiap alamat IP
def ping(ip):
    output = subprocess.check_output(['ping', '-c', '3', ip]).decode('utf-8')
    match = re.search(r'rtt min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+) ms', output)
    if match:
        result = {
            'IP Address': ip,
            'Average': match.group(2)
        }
        return result

# Menggunakan ThreadPoolExecutor untuk menjalankan fungsi ping secara paralel
with ThreadPoolExecutor() as executor:
    # Submit proses ping untuk setiap alamat IP
    futures = [executor.submit(ping, ip) for ip in ip_addresses]

    # Mengambil hasil secara berurutan seiring dengan selesainya proses ping
    for future in as_completed(futures):
        result = future.result()
        if result:
            results.append(result)

# Cetak tabel
print("IP Address\tAverage")
for result in results:
    print(f"{result['IP Address']}\t{result['Average']}")
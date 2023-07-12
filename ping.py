import subprocess
import re

ip_addresses = []

# Baca alamat IP dari file txt
with open('xyz.txt', 'r') as file:
    ip_addresses = file.read().splitlines()

results = []

# Jalankan perintah ping untuk setiap alamat IP
for ip in ip_addresses:
    output = subprocess.check_output(['ping', '-c', '3', ip]).decode('utf-8')
    match = re.search(r'rtt min/avg/max/mdev = ([\d.]+)/([\d.]+)/([\d.]+)/([\d.]+) ms', output)
    if match:
        result = {
            'IP Address': ip,
            'Average': match.group(2)
        }
        results.append(result)

# Cetak tabel
print("IP Address\tAverage")
for result in results:
    print(f"{result['IP Address']}\t{result['Average']}")
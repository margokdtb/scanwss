#ambil host saja
bug_hosts = []

with open('hasil.txt', 'r') as file:
    for line in file:
        data = eval(line)
        host = data.get('Host')
        if host:
            bug_hosts.append(host)

bug_hosts_sorted = sorted(bug_hosts)

with open('hasil2.txt', 'w') as output_file:
    for host in bug_hosts_sorted:
        output_file.write(host + '\n')

#menambah ping        
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

# Menyimpan hasil ke dalam file hasil3.txt
with open('hasil3.txt', 'w') as output_file:
    # Menulis header
    output_file.write("IP Address\tAverage\n")
    
    # Menulis hasil untuk setiap alamat IP
    for result in results:
        output_file.write(f"{result['IP Address']}\t{result['Average']}\n")

# Menampilkan hasil
print("IP Address\tAverage")
for result in results:
    print(f"{result['IP Address']}\t{result['Average']}")
    
print("DISIMPAN hasil4.txt")
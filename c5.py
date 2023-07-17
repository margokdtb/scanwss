import socket
import threading
import time

def tcping(host, port):
    try:
        start_time = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host, port))
        end_time = time.time()
        elapsed_time = end_time - start_time
        sock.close()
        return round(elapsed_time, 2)
    except socket.error:
        return None
        
def ping_host(host):
    response_time_80 = tcping(host, 80)
    response_time_443 = tcping(host, 443)
    if response_time_80 is not None:
        print(f"{host} - 80 - {response_time_80*100:.2f}")
    else:
        print(f"Host: {host} - 80 - Tidak dapat dijangkau")
    if response_time_443 is not None:
        print(f"{host} - 443 - {response_time_443*100:.2f}")
    else:
        print(f"Host: {host} - 443 - Tidak dapat dijangkau")
    result_list.append((host, 80, response_time_80))
    result_list.append((host, 443, response_time_443))

host_list = []
# Baca sumber dari file hasil2.txt
with open("x2.txt", "r") as file:
    for line in file:
        host_list.append(line.strip())

# Lakukan ping secara multithread
threads = []
result_list = []

for host in host_list:
    t = threading.Thread(target=ping_host, args=(host,))
    t.start()
    threads.append(t)

# Tunggu semua thread selesai
for t in threads:
    t.join()
    
# Urutkan hasil berdasarkan response_time secara ascending
result_list.sort(key=lambda x: x[2])

# Simpan hasil ping ke dalam file ping-hasil.txt
with open("ping-hasil.txt", "w") as file:
    for result in result_list:
        host, port, response_time = result
        if response_time is not None:
            file.write(f"{host} - {response_time*100:.2f} - {port} \n")
        else:
            file.write(f"{host} - {port} - Tidak dapat dijangkau\n")


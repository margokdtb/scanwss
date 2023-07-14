import socket
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

host_list = []

# Baca sumber dari file xyz3.txt
with open("hasil4.txt", "r") as file:
    for line in file:
        host_list.append(line.strip())

port = 80

# Lakukan ping ke setiap host dan simpan hasilnya di file xyz6.txt
with open("ping-hasil.txt", "w") as file:
    for host in host_list:
        response_time = tcping(host, port)
        if response_time is not None:
            file.write(f"{host} -  {response_time:.3f}\n")
        else:
            file.write(f"Host: {host} - Tidak dapat dijangkau\n")
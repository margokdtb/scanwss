import threading

def process_line(line):
    data = eval(line)
    if 'Host' in data:
        return data['Host']
    return None

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    hosts = []
    # Membuat loker (mutex) untuk mengakses list hosts
    lock = threading.Lock()

    def process_line_thread(line):
        host = process_line(line)
        if host:
            with lock:
                hosts.append(host)

    threads = []
    for line in lines:
        # Membuat thread untuk memproses setiap baris
        thread = threading.Thread(target=process_line_thread, args=(line,))
        thread.start()
        threads.append(thread)

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

    with open(output_file, 'w') as file:
        for host in hosts:
            file.write(host + '\n')

# Proses file 'hasil.txt' menggunakan multithreading
process_file('x1.txt', 'x2.txt')
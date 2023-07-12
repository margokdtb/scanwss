# Author: HanzHhe X Misploit

import argparse, time, websocket
from concurrent import futures
from os import system

switchproto = []
gagal = []
not101 = []
r, g, y, w = "\033[6;31m", "\033[6;32m", "\033[1;33m", "\033[m"

def main(rhost, total):
    global switchproto, gagal, not101
    t1 = time.time()
    scanning = 0
    executor = futures.ThreadPoolExecutor(max_workers=len(rhost))
    for get in executor.map(websocket.gethttp, rhost):
         scanning += 1
         print(f"[{g}INFO{w}] Scanning {scanning} Dari {total}")
         if not "Error:" in get:
            if '101' in get['Status'] or '200' in get['Status']:
               switchproto.append(get)
            else:
                not101.append(get)
         else:
            gagal.append(get)
    t2 = time.time()
    return t2 - t1

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('-f', '--file', required=True, help="FILE Containing List Of Host")
   parser.add_argument('-o', '--output', help="Save Hasil Ke File")
   arg = parser.parse_args()
   output = arg.output
   file = open(arg.file, 'r')
   system('clear')
   rhost = file.read().splitlines()
   print(f"[{g}INFO{w}] Total Host Yg Akan Di Scan: {len(rhost)}")
   rtime = main(rhost, len(rhost))
   if not output:
      output = "hasilws.txt"
   outfile = open(output, 'w+')
   for ok in switchproto:
      outfile.write(str(ok) + "\n")
   outfile.close()
   fr = open(output, "r")
   if fr.read() != "":
      print(f"[{g}INFO{w}] Hasil Ok Disimpan Ke -> {output}")
   outfile = open(f"bedarespon{output}", "w+")
   for notok in not101:
      outfile.write(str(notok) + "\n")
   outfile.close()
   fr = open(f"bedarespon{output}", "r")
   if fr.read() != "":
      print(f"[{g}INFO{w}] Hasil Beda Respon Disimpan Ke -> bedarespon{output}")
   print(f"[{g}INFO{w}] OK: {g}{len(switchproto)}{w} | BEDA RESPON: {y}{len(not101)}{w} | GAGAL: {r}{len(gagal)}{w}\n[{g}INFO{w}] Total Waktu Untuk Scanning {rtime}")

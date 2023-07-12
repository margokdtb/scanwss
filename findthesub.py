# Author: HanzHhe
# Follow Facebook: https://www.facebook.com/hanzstaygoth666
# Note: Recode Boleh Asal Cantumkan Nama Author Asli
# Thanks To Rapiddns

import requests, re, argparse

index1 = []
index2 = []
r, g, y, w = "\033[6;31m", "\033[6;32m", "\033[6;33m", "\033[m"

def main(domain, output):
    print(f"[{g}INFO{w}] Scanning Subdomain")
    try:
      get = requests.get(f'https://rapiddns.io/subdomain/{domain}?full=1#result')
    except Exception as e:
      print(f"{r}Uknown Error:\n{w}{e}")
    patternsubdomain = f"<td>.*?{domain}</td>"
    patternsameip = 'website">.*?</a>'
    subdomain = re.findall(patternsubdomain, get.text)
    sameip = re.findall(patternsameip, get.text)
    global index1, index2

    if output:
       outfile = open(output, "w+")
       sameoutfile = open(f"sameip{output}", "w+")
    count = []
    print(f"[{g}INFO{w}] Subdomain Ditemukan:")
    for subd in set(subdomain):
        subd = subd.split("<td>")[1].split("</td>")[0]
        count.append(subd)
        print(subd)
        if output:
           outfile.write(subd + "\n")
    if output:
       print(f"[{g}INFO{w}] Hasil Dari Subdomain Disimpan Ke > {output}")
       outfile.close()
    print(f"[{g}INFO{w}] IP Yang Sama Dengan SubDomain:")
    countsame = []

    for same in set(sameip):
        if '.</a>' in same:
           same = same.split('website">')[1].split('.</a>')[0]
        else:
           same = same.split('website">')[1].split('</a>')[0]
        countsame.append(same)
        if output:
           sameoutfile.write(same + "\n")
        print(same)
    if output:
       print(f"[{g}INFO{w}] Hasil Dari IP Yg Sama Disimpan Ke > sameip{output}")
       sameoutfile.close()
    print(f"[{g}SUKSES{w}] Total Subdomain Ditemukan: {len(count)}\n[{g}SUKSES{w}] IP Yang Sama: {len(countsame)}")

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('-d', '--domain', required=True, help='Domain Asli Yg Akan DiScan')
   parser.add_argument('-o', '--output', required=False, help='Save Hasil Ke File')
   arg = parser.parse_args()
   main(arg.domain, arg.output)

import os

domain = input("Masukan Domain: ")

#os.system("cd")
#os.system("cd storage/downloads/scanws/scanws")
os.system(f"python findthesub.py -d {domain} -o xyz.txt")
os.system("python scanws.py -f xyz.txt -o x1.txt")
os.system("python ping.py")
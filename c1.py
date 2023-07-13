with open('hasil.txt', 'r') as file:
    lines = file.readlines()

hosts = []
for line in lines:
    data = eval(line)
    if 'Host' in data:
        hosts.append(data['Host'])

with open('hasil2.txt', 'w') as file:
    for host in hosts:
        file.write(host + '\n')
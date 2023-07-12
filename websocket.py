# Author: HanzHhe x Misploit
# Follow Facebook: https://www.facebook.com/HanzStayGoth666

import requests, socket, ssl

def gethttp(host):
   try:
     sock = socket.socket()
     sock.settimeout(5)
     sock.connect((host, 80))
     payload = f"GET / HTTP/1.1\r\nHost: sg1.hostip.us\r\nConnection: upgrade\r\nUpgrade: websocket\r\nUser-Agent: Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36\r\n\r\n".encode()
     sock.send(payload)
     data = sock.recv(1024).decode("utf-8", errors="replace")
     if data:
        return {'Host': host, 'Status': data.split("\r\n")[0]}
     else:
        return {'Host': host, "Status": "No Respon"}
   except Exception as e:
     return f"Host: {host}, Error: {e}"

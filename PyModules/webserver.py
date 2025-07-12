import socket
import network

ROUTES = {}

def on(route, file):
    ROUTES[route] = file

def begin(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('' , port))
    s.listen(2)
    print(f'Serving on http://{network.WLAN(network.STA_IF).ifconfig()[0]}:{port}')
    while True:
        soc, addr = s.accept()
        print("Got a connection from ", addr)
        request = soc.recv(1024).decode()
      
        try:
            path = request.split(' ')[1]
        except:
            path = "/"

        if path in ROUTES:
            try:
                with open(ROUTES[path], 'r') as f:
                    content = f.read()
                soc.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
                soc.sendall(content)
            except:
                soc.send("HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\n")
                soc.send("Error loading file.")
        else:
            soc.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n")
            soc.send("404 - Not Found")
          
        soc.close()

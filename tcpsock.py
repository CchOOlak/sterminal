import socket
import threading

class TCPSockServer(threading.Thread):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        super(TCPSockServer, self).__init__()

    def run(self):
        self.sock.listen(5)
        while True:
            try:
                client, _ = self.sock.accept()
                client.settimeout(60)
                threading.Thread(target=self.listenToClient, args=(client,)).start()
            except:
                break

    def listenToClient(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
    
    def close(self):
        print("server shuted down")
        self.sock.close()


class TCPSockClient(threading.Thread):
    def __init__(self, host, port, message):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.message = message
        super(TCPSockClient, self).__init__()
    
    def run(self):
        self.sock.sendall(self.message.encode())
        data = self.sock.recv(1024)
        print('Received', repr(data.decode()))
        self.sock.close()
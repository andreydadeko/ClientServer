import socket

class client():

    def connect(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def send_message(self, message):
        self.sock.send(message)
        response = str(self.sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

    def disconect(self):
        self.sock.close()

CL = client()

for i in range(20):
    CL.connect('localhost', 5555,)
    for k in range(5):
        CL.send_message(k)
    #CL.disconect()
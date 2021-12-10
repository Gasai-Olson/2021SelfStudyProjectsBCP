import socket
from threading import Thread

'''
program is only built to run multiple echo servers/clients

'''

class serverhost:
    def __init__(self,address):
        self.HOST, self.PORT = address
    def handle_echo(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
class client:
    def __init__(self,address):
        self.HOST, self.PORT = address

    def tcp_echo_client(self,message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            print('s')
            s.sendall(bytes(message))
            data = s.recv(1024)

        print('Received', repr(data))

class cardinal:
    pass
    '''
create system to track sockets by numeric value
    '''



example_client = client(('127.0.0.1',8888))#port 8888 not reserved
example_server = serverhost(('127.0.0.1',8888))
Thread(target = example_server.handle_echo()).start()
Thread(target=example_client.tcp_echo_client('testing')).start()
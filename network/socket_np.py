import socket


class Socket:
    "tao la class Socket"
    HOST = ''
    PORT = 8080

    def __init__(self):
        self.sock = socket.socket()
        Socket.HOST = socket.gethostname()

    def server(self):
        print(f"server start on host: {Socket.HOST}")

        self.sock.bind((Socket.HOST, Socket.PORT))

        print("")
        print("server done binding")
        print("")
        print("server is waiting client connect")
        print("")

        # server waiting client ket noi( code tam dung)
        self.sock.listen(3)

        # print(f"conn: {conn}\nclient: {client}")

        while True:
            conn, client = self.sock.accept()

            message = input(str("Server: "))
            # ma hoa tu server khi gui
            message = message.encode()
            conn.send(message)
            print(f"tin nhan da duoc gui di")
            print("")

            incomming_message = conn.recv(1024)
            incomming_message = incomming_message.decode()
            print(f"{incomming_message}")

    def client(self, name='client'):
        Socket.HOST = input(str("vui long nhap hostname or ip cua server:"))

        # (host, port) => la cua may chu server, host=name or ip
        self.sock.connect((Socket.HOST, Socket.PORT))
        print('da ket noi toi server', Socket.HOST)

        while True:
            incomming_message = self.sock.recv(1024)
            incomming_message = incomming_message.decode()
            print(f"Server: {incomming_message}")

            message = input(str(f"{name}: "))
            message = (name + ': ' + message).encode()
            self.sock.send(message)

            print(f"tin nhan da duoc gui di")
            print("")
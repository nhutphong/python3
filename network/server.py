#!/usr/bin/python

# import socket

# s = socket.socket()
# host = socket.gethostname()
# print(f"server start on host: {host}")

# port = 8080
# s.bind((host, port))

# print("")
# print("server done binding")
# print("")
# print("server is waiting client connect")
# print("")

# # server waiting client ket noi( code tam dung)
# s.listen(3)

# conn, addr = s.accept()
# print(f"conn: {conn}\naddr: {addr}")

# while True:
#   message = input(str("Server: "))
#   # ma hoa tu server khi gui
#   message = message.encode()
#   conn.send(message)
#   print(f"tin nhan da duoc gui di")
#   print("")

#   incomming_message = conn.recv(1024)
#   incomming_message = incomming_message.decode()
#   print(f"client: {incomming_message}")



from socket_np import Socket

class Server(Socket):
  def __init__(self):
    super().__init__()


def main():
  server = Server()
  server.server()

main()




## aiohttp

# from aiohttp import web

# async def handle(request):
#     name = request.match_info.get('name', "Anonymous")
#     text = "Hello, " + name
#     return web.Response(text=text)

# app = web.Application()
# app.add_routes([web.get('/', handle),
#                 web.get('/{name}', handle)])

# web.run_app(app)


# if __name__ == '__main__':
#     pass
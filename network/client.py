#!/usr/bin/python

# import socket

# s = socket.socket()
# host = input(str("vui long nhap hostname or ip cua server:"))
# port = 8080

# # (host, port) => la cua may chu server, host=name or ip
# s.connect((host, port))
# print('da ket noi toi server', host)

# while True:
#     incomming_message = s.recv(1024)
#     incomming_message = incomming_message.decode()
#     print(f"Server: {incomming_message}")
#     print("")

#     message = input(str("client:"))
#     message = message.encode()
#     s.send(message)

#     print(f"tin nhan da duoc gui di")
#     print("")


from socket_np import Socket

class Client(Socket):
    def __init__(self):
        super().__init__()


def main():
    client = Client()
    client.client(name='thanhdung')

    client2 = Client()
    client2.client(name='tanheo')

main()



# # aiohttp

# import aiohttp
# import asyncio

# async def fetch(session, url):
# 	async with session.get(url) as response:
# 			return await response.text()

# async def main():
# 	async with aiohttp.ClientSession() as session:
# 		html = await fetch(session, 'https://python.org')
# 		print(html)

# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())

# if __name__ == '__main__':
# 	asyncio.run(main())
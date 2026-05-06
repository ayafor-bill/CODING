import socket

target_host = 'localhost'
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_host))

client.send("GET / HTTP/1.1\r\nHOST: 0.0.0.0\r\n\r\n")

response = client.recv(4096)

print(response)
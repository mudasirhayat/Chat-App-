import socket
from _thread import *
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"
port=54321
print("waiting for the connection......")
client.connect((ip,port))
response=client.recv(2048)
def recieve_thread(connection):
    while True:
        data=connection.recv(2048)
        print(data.decode("utf-8"))
    connection.close()

start_new_thread(recieve_thread,(client,))
while True:
    Input=input("client saying.....")
    client.send(str.encode(Input))

client.close()    
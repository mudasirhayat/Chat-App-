# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:49:57 2021

@author: MudasirHayat
"""

import socket
import os
from _thread import *

ip="127.0.0.1"
port=54321
ServerSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Threadcount=0
ServerSocket.bind((ip,port))
print("Server is listening......")
ServerSocket.listen(5)
clients =[] 
def thread_client(connection):
    connection.send(str.encode("Welcome to the server......"))
    while True:
        data=connection.recv(2048)
        reply="server:"+ data.decode('utf-8')
        if not data:
            break
        for client in clients: client.sendall(str.encode(reply))
    connection.close()    

while True:
    client , address = ServerSocket.accept()
    print("server is connected to"+ address[0]+":" +str(address[1]) )
    start_new_thread(thread_client,(client,))
    Threadcount+=1
    print("Thread number :"+str(Threadcount))
    clients.append(client)
ServerSocket.close()    
import socket
from _thread import *
import sys

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
    
#opens port for connections to begin limited to 2 connections
s.listen(2)
print("Waiting for a connection, Server Started.")

#Create a threaded function for connections
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)
                
            conn.sendall(str.encode(reply))
            
        except:
            print("Random error occured")
            break
        
    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn,))
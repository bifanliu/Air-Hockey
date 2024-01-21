import socket
from _thread import *

# Create socket, socket.socket([family], [type] , [proto]), Type: TCP/UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind(host, port)
address = ("localhost",5555)
try:
    s.bind(address)
except socket.error as e:
    str(e)

# Listen, 10 is the maximum socket connected to server
s.listen(10)
print("Waiting for a connection, Server Started")

p = 0
client_pool = [0]*100
singlepuck = 0
multipuck = 0
singlepcknum = 0
multipucknum = 0

# Thread connect
def threaded_client(conn, p, msg):
    conn.send(msg.encode('utf8'))
    start = True
    while start:
        if msg == "start":
            start = False
        else:
            msg = conn.recv(1024).decode('utf8')
    while True:
        pos = conn.recv(1024).decode('utf8')
        if pos == "start":
            pos = conn.recv(1024).decode('utf8')
        client_pool[p].sendall(pos.encode('utf8'))
        if pos == "over":
            conn.clear()

# Server keeps listening
while True:
        conn, addr = s.accept()
        number = conn.recv(1024).decode('utf8')
        if number == "1":
            print("number is ",number)
            multipuck = multipuck + 1
            print(multipuck)
        elif number == "2":
            print("number is ",number)
            singlepuck = singlepuck + 1
        if multipuck == 1 and number == "1":
            msg = "wait the other player"
            client_pool[p] = conn
            start_new_thread(threaded_client, (conn, p+1, msg))
            multipucknum = p+1
            p = p+2
        elif singlepuck == 1 and number == "2":
            msg = "wait the other player"
            client_pool[p] = conn
            singlepcknum = p+1
            start_new_thread(threaded_client, (conn, p+1, msg))
            p = p+2
        elif singlepuck == 2 and number == "2":
            msg = "start"
            client_pool[singlepcknum] = conn
            client_pool[singlepcknum-1].send(msg.encode('utf8'))
            start_new_thread(threaded_client, (conn, singlepcknum-1, msg))
            singlepcknum = 0
            singlepuck = 0
        elif multipuck == 2 and number == "1":
            print("start")
            msg = "start"
            client_pool[multipucknum] = conn
            client_pool[multipucknum-1].send(msg.encode('utf8'))
            start_new_thread(threaded_client, (conn, multipucknum-1, msg))
            multipuck = 0
            multipucknum = 0

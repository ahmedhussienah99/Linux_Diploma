import socket
import threading
import time

DISCONNECT_MESSAGE = "DISCONNECT"
def handle_client(Client, address_client):
   global server
   global thre
   connected=True
   while connected:
        data = Client.recv(1024)
        strr=data.decode('UTF-8')
        print(f"Accepted connection from {address_client}{data.decode('UTF-8')}")
        msg="Msg received"
        Client.send(msg.encode('UTF-8'))
        if str(strr) == str(DISCONNECT_MESSAGE):
            connected = False
   print(DISCONNECT_MESSAGE)
   Client.close()

FORMAT = 'UTF-8'

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
print(socket.gethostname())

address=(SERVER,5000)
#open socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to reuse socket again after close without warining address already in use
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server work on this address
server.bind(address)
#sever can handel with 10 clients
server.listen(10)
count=0
while True :
    #waiting clients and get this client and address
    Client,address_client=server.accept()
    thread = threading.Thread(target=handle_client, args=(Client, address_client))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    thread.join()
    if threading.activeCount()-1 == 0 :
            server.shutdown(socket.SHUT_RDWR)
            break
    
    
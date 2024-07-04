import socket


SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, 5000)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Send data to the server
while True :
    msg=str(input("please enter the message or DISCONNECT :"))
    client.send(msg.encode())

    # Receive data from the server
    data = client.recv(1024)
    print(f"Received from server: {data.decode()}")
    if msg=="DISCONNECT":
        print("DISCONNECT")
        client.close()
        break

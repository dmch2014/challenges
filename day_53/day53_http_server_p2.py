#https://medium.com/@stephen.biston/write-an-http-server-from-the-ground-up-in-9-minutes-with-python-1fdb9800a26a

import socket
import select

if __name__ == "__main__":
    # Get socket file descriptor as a TCP socket using the IPv4 address family
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set some modes on the socket, not required but it's nice for our uses
    listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port_input= int(input("Enter the port you want to bind the server: "))
    # Get the IP address and port of the local socket

    print("Hostname-->:%s" %(socket.gethostname))

    address_port = ("127.0.0.1", port_input)
    # leserve address and port
    listener_socket.bind(address_port)
    # listen for connections, a maximum of 1
    listener_socket.listen(1)
    local_address = listener_socket.getsockname()
    print("Server listening @ %s:%s" % (local_address[0],local_address[1]))

    # loop indefinitely to continuously check for new connections
    while True:
        # Poll the socket to see if there are any newly written data, note excess data dumped to "_" variables
        read_ready_sockets, _, _ = select.select(
            [listener_socket],  # list of items we want to check for read-readiness (just our socket)
            [],  # list of items we want to check for write-readiness (not interested)
            [],  # list of items we want to check for "exceptional" conditions (also not interested)
            0  # timeout of 0 seconds, makes the method call non-blocking
        )
        # if a value was returned here then we have a connection to read from
        if read_ready_sockets:
            # select.select() returns a list of readable objects, so we'll iterate, but we only expect a single item
            for ready_socket in read_ready_sockets:
                # accept the connection from the client and get its socket object and address
                client_socket, client_address = ready_socket.accept()

                # read up to 4096 bytes of data from the client socket
                client_msg = client_socket.recv(4096)

                print("Client said:" + client_msg.decode())


                # Send a response to the client, notice it is a byte string
                # replacing the client_socket.sendall call from before
                client_socket.sendall(
                    bytes("""HTTP/1.1 200 OK\r\nContent-type: text/html\r\nSet-Cookie: ServerName=steveserver\r\n\r\n<!doctype html>
                        <html>
                            <head/>
                            <body>
                                <h1>Welcome to the server!</h1>
                                <h2>Server address: {}:{}</h2>
                                <h3>You're connected through address: {}:{}</h3>
                                <body>
                                    <pre>{}</pre>
                                </body>
                            </body>
                        </html>\r\n\r\n
                        """.format(address_port[0], address_port[1], client_address[0], client_address[1], client_msg.decode("utf-8")))

                    #bytes("HTTP/1.1 200 OK")
                )

                try:
                    # close the connection
                    client_socket.close()
                except OSError:
                    # client disconnected first, nothing to do
                    pass
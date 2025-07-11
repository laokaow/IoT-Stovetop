import wifiConnection


def http_get(url = 'http://detectportal.firefox.com/'):
    import socket                           # Used by HTML get request
    import time                             # Used for delay
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialise the socket
    s.connect(addr)                         # Try connecting to host address
    # Send HTTP request to the host with specific path
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receve response
    print(rec_bytes)                        # Print the response
    s.close()                               # Close connection

#First thing that should run
print("Booting Stovetop Monitoring Device")

# Connecting to wifi when giving the system power
try:
    ip = wifiConnection.connect_wifi()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Gets information about the network connection
try:
    http_get()
except (Exception, KeyboardInterrupt) as err:
    print("No Internet", err)

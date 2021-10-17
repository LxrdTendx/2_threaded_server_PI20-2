import socket
import threading
from progres_Bar import printProgressBar
N = 2 ** 16 - 1
counter = 0
spaces = " " * 100 + "\n"


def scan(arr, thr, host):
    global counter
    for port in arr:
        sock = socket.socket()
        try:
            sock.connect((host, port))
            print("Port", port, "open", end=spaces)
            printProgressBar(counter, 66, prefix='Progress:', suffix='Success', length=50)
        except:
            continue
        finally:
            sock.close()
    counter += 1
    return


host = input("Host:")
if host == '':
    host = '127.0.0.1'

printProgressBar(0, 66, prefix='Progress:', suffix='Success', length=50)

for thread in range(66):
    arr = []
    for i in range(1000):
        arr.append(thread * 1000 + i)
        if arr[i] >= N:
            break
    thr = threading.Thread(target=scan, args=[arr, thread, host])
    thr.start()

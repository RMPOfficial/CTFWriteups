import socket
s = socket.create_connection(('localhost', 4000), timeout=5)
f = s.makefile('rwb', buffering=0)
skip = False
while True:
    line = f.readline()
    print(line)
    if skip == True: skip = False; continue
    if not line: break
    toWrite = line[::-1].split()[0] + b'\n'; print(toWrite)
    f.write(toWrite); skip = True;


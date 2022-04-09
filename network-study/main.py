import sys
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_RAW)
s.bind(("en0", 0))
r=s.recv(2000)
sys.stdout.write("<%s>\n"%repr(r))

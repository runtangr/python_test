#!usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',50007)
sk = socket.socket()
sk.connect(ip_port)
while True:
    msg = input("<<:").strip()
    sk.sendall(bytes(msg,encoding='utf8'))
    server_reply = sk.recv(1024)
    print('server_reply:',server_reply.decode())
sk.close()
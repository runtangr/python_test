#!usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
class MYTCOHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print('new connect:',self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data:break
            print('client say:',data.decode())
            self.request.send(data)

if __name__ == '__main__':
    HOST,PORT = "localhost",50007
    server = socketserver.ThreadingTCPServer((HOST,PORT),MYTCOHandle)
    server.serve_forever()


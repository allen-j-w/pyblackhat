# -*-coding:utf-8 -*-
import socket

if __name__ == '__main__':
    target_host = '127.0.0.1'
    target_port = 8888

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send('GET / HTTP/1.1\r\nHOST:baidu.com\r\n\r\n')
    res = client.recv(4096)
    print res
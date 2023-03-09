import time
import click
import os
import sys
import keyboard
import socket

@click.command()
@click.option('-n', prompt='The name of the file')



def hello(n):
    d = n
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((n, 3030))
    s.listen(1)
    conn, addr = s.accept()
    while True:
            
            data = conn.recv(1024)
            conn.sendall(data)
            if not data:
                pass
            else:
                keyboard.write(data.decode('utf-8'))





if __name__ == '__main__':
    hello()

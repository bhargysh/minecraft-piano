from pythonosc import osc_message_builder
from pythonosc import udp_client
from mcpi import minecraft
from time import sleep

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
mc = minecraft.Minecraft.create()

positions = mc.player.getTilePos()

'''def bulldozer(x, y, z):
    mc.setBlocks(x - 30, y, z - 30, x + 30, y + 30, z + 30, 0)
bulldozer(positions.x, positions.y, positions.z)'''

def make_octave(x, y, z):
    mc.setBlocks(x - 30, y, z - 30, x + 30, y + 30, z + 30, 0)
    for i in range(0, 19, 3):
        white_key(positions.x + i, positions.y, positions.z)
    for i in range(2, 18, 3):
        if i == 8:
            continue  
        black_key(positions.x + i, positions.y, positions.z)

def black_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)

def white_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)

def centre_steve():
    mc.player.setPos(positions.x + 8, positions.y + 3, positions.z + 12)

make_octave(positions.x, positions.y, positions.z)
centre_steve()
'''def play_note(note):
    sender.send_message('/play_this', note)
    sleep(0.5)'''

from pythonosc import osc_message_builder
from pythonosc import udp_client
from mcpi import minecraft
from time import sleep

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
mc = minecraft.Minecraft.create()

positions = mc.player.getTilePos()
print(positions)

def clear_space(x, y, z):
    mc.setBlocks(x - 70, y, z - 70, x + 70, y + 70, z + 70, 0)

def make_octave(x, y, z):
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
    mc.player.setPos(positions.x + 8, positions.y, positions.z + 12)

clear_space(positions.x, positions.y, positions.z)
make_octave(positions.x, positions.y, positions.z)
centre_steve()

white_notes = [60, 62, 64, 65, 67, 69, 71]
black_notes = [61, 63, 0, 66, 68, 70]

def play_note(note):
    sender.send_message('/play_this', note)
    sleep(0.5)

while True:
    new_pos = mc.player.getTilePos()
    print(new_pos)
    block_below = mc.getBlock(new_pos.x, new_pos.y - 1, new_pos.z)
    print(block_below)

    if block_below != 44 and block_below != 49:
        block_below = mc.getBlock(new_pos.x, new_pos.y, new_pos.z)

    relative_pos = positions.x - new_pos.x

    if block_below == 44:
        notes_across = relative_pos // -3
        print('about to play white key')
        play_note(white_notes[notes_across])

    if block_below == 49:
        notes_across = ((relative_pos - 1) // -3) - 1
        print('about to play black key')
        play_note(black_notes[notes_across])

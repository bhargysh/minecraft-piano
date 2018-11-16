from pythonosc import osc_message_builder
from pythonosc import udp_client
from time import sleep
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)


def play_note(note):
    sender.send_message('/play_this', note)
    sleep(0.5)

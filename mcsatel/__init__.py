import socket
from threading import Thread
from mcdreforged.api.all import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def mcs_recv(server):
    while True:
        cmd = client.recv(4096).decode("utf-8")
        print(cmd)
        server.execute(cmd)


def on_load(server: PluginServerInterface, old):
    client.connect(("127.0.0.1", 20429))
    Thread(target=mcs_recv, args=(server,)).start()


def on_info(server: PluginServerInterface, info: Info):
    if not info.is_user:
        client.send(info.content.encode("utf-8"))


def on_unload(server: PluginServerInterface):
    client.close()

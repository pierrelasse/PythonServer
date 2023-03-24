import socket
import json
import os
import random
import sys
from threading import *

username = f"UrmomGayXD.{random.randint(0, 100000)}"
sessionid = "f995c690-9eb5-44ec-b128-1bd0e96cda23"

class Client:
    def __init__(self):
        self.main()

    def main(self):
        os.system("title Client [Disconnected]")

        host = "localhost"
        port = int(input("Port: "))
        host = host.replace("localhost", "127.0.0.1")
        port = port
        
        self.connect(host, port)
        
        os.system(f"title Client [{host}:{port}]")
        
        try:
            self.serverThread()

        except Exception as e:
            err = str(e).strip()
            err = err.replace("[WinError 10054]", "")
            self.ondisconnect(err)
        
    def connect(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.connect((host, port))
        self.server.send(packetgen("login", username=username, sessionid=sessionid))
        
        Thread(target=self.client, args=()).start()
        
    def serverThread(self):
        while True:
            data = self.server.recv(1024).decode('utf-8')
            
            if data:
                #print(f"[PACKET] {data}")
                
                packet = json.loads(data)
                type = packet['type']
                
                # MessagePacket
                if type == "message":
                    msg = packet['message']
                    print(f"[CHAT] {msg}")
                
                # ChatMessagePacket
                elif type == "chatmessage":
                    msg = packet['format'].replace("[username]", packet['username']).replace("[message]", packet['message'])
                    print(f"[CHAT] {msg}")
                    
                # DisconnectPacket
                elif type == "disconnect":
                    self.ondisconnect(packet['error'])

                    
    def ondisconnect(self, err):
        #os.system('cls' if os.name == 'nt' else 'clear')
        os.system("title Client [Disconnected]")
        print(f"Disconnected: {err}")
        sys.exit()


    def client(self):
        while True:
            try:
                inp = input("")
            except:
                print()
                continue
            try:
                packet = {}
                if inp.startswith("/"):
                    packet = packetgen("command", command=inp)

                else:
                    packet = packetgen("chat", message=inp)
                    if not len(inp) > 0:
                        print("Cannot send empty chat message")
                        continue

                self.server.send(packet)

            except AttributeError:
                print("You are not connected to a server!")
                global running
                running = False

def packetgen(type, **kwargs):
    packet = {"type": type}
    for arg in kwargs:
        packet[arg] = kwargs[arg]
    return json.dumps(packet).encode('utf-8')


def run():
    Client()
    
run()
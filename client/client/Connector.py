import socket
import json
import os
import sys
from threading import *

from csdata import gd

from log import logger

class Connector:
    connected = False
    
    def __init__(self):
        self.main()

    def main(self):
        os.system("title Client [Disconnected]")

        host = "localhost"
        while True:
            try:
                port = int(input("Port: "))
                break
            except:
                pass
        host = host.replace("localhost", "127.0.0.1")
        port = port
        
        self.connected = True
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
        
        logger.info(f"Connecting to {host}, {port}", "Connector Thread")

        err = False
        try:
            self.server.connect((host, port))
        except ConnectionRefusedError:
            err = "ConnectionRefusedError: Server offline / not reachable"
        except Exception as e:
            return
        if err:
            logger.error(f"&cFailed to connect to server!\n\n{err}\n")
            return

        username = gd.session['username']
        sessionid = gd.session['token']
        self.server.send(packetgen("login", username=username, sessionid=sessionid)) # gd.session['token'] # gd.session['username']
        
        self.clientthread = Thread(target=self.client, args=())
        self.clientthread.start()
        
    def serverThread(self):
        while True:
            data = self.server.recv(1024).decode('utf-8')
            
            if data:
                #print(f"[PACKET] {data}")
                
                try:
                    packet = json.loads(data)
                except:
                    logger.error("Error while decoding packet!")
                    continue
                type = packet['type']
                
                # MessagePacket
                if type == "message":
                    msg = packet['message']
                    logger.info(f"[CHAT] {msg}", "Connector Thread")
                
                # ChatMessagePacket
                elif type == "chatmessage":
                    msg = packet['format'].replace("[username]", packet['username']).replace("[message]", packet['message'])
                    logger.info(f"[CHAT] {msg}", "Connector Thread")
                    
                # DisconnectPacket
                elif type == "disconnect":
                    self.ondisconnect(packet['error'])

 
    def ondisconnect(self, err):
        self.connected = False
        #os.system('cls' if os.name == 'nt' else 'clear')
        os.system("title Client [Disconnected]")
        print(f"Disconnected: {err}")
        run()


    def client(self):
        while self.connected == True:
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
                        if self.connected == True:
                            print("Cannot send empty chat message")
                        continue

                try:
                    self.server.send(packet)
                except Exception as e:
                    print(f"Cannot send packet: {e}")

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
    Connector()
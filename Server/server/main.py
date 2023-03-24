print("Loading libaries, please wait...")

import time

start_time = time.time()

import socket
from threading import *
import os
#import sys
import traceback

if os.path.isfile("python39.dll"):
    os.chdir(os.path.normpath(os.getcwd() + "\\.."))
else:    
    os.chdir(os.getcwd() + "\\server")
if not os.path.isdir(os.getcwd() + "\\server"):
    os.mkdir(os.getcwd() + "\\server")

from csdata import *

from client.client import connectionHandler as newConnection

from log import logger

from server.disconnect import disconnect

from utils import stopallthreads, forceexit, sendto, get_hwid

from server.licenseKey import verifyKey as licensekey_verify

from server.loadfilesystem import loadfilesystem

from plugin.plugin import Plugin

from client.command import LoadCommands, ExecuteCommand


class Server:
    host = "127.0.0.1"
    port = 0
    
    def __init__(self, type=""):
        if type == "run":
            thread = Thread(target=self.serverThread, args=()).start()
            pd.threads.append(thread)
            self.main()
            
        elif type == "shutdown":
            if not self.shutdown == False:
                self.shutdown()


    def main(self):
        loadfilesystem(self)

        logger.info(f"Enviroment: root='{pd.path['root']}', authFile='{pd.path['sessionids']}', name='PROD', host='{self.host}', port='{self.port}'", "main")
        logger.info(f"Starting server version {sinfo.version}", "main")
        
        logger.info(f"Creating server enviroment", "main")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        licensekey_verify(self.licenseKey)

        LoadCommands()
        Plugin()
        
        try:
            self.server.bind((self.host, self.port))
        except Exception as e:
            logger.error("**** FAILED TO BIND TO PORT! *****", "main")
            logger.warn("Perhaps a server is already running on that port?", "main")
            logger.warn(f"Exception: {e}", "main")
            print(logger.color("&eTranslation: &c[WinError 10013] Der Zugriff auf einen Socket war aufgrund der Zugriffsrechte des Sockets unzulässig &ameans: The fucking port is alr in use&r", "&"))
            self.shutdown()
            
        logger.info(f"Using default channel type", "main")
        self.port = self.server.getsockname()[1]
        logger.info(f"Bound host and port", "main")
        
        logger.info(f"Loading sessions", "main")
        sessionid.loadids()

        #print(f"Connect using: ip: {host} | port: {port}")
        
        logger.info(f'Done ({str(time.time() - start_time)[0:6]}s)! For help, type "help"', "main")
        #logger.info(f"Timings reset", "main")
        #start_time = None
        
        self.server.listen()
        logger.info(f"Listening on /{self.host}:{self.port}", "main")
        os.system(f"title Server [{self.host}:{self.port}]")
        
        while not self.shutdown == False:
            try:
                try:
                    (client, address) = self.server.accept()
                except KeyboardInterrupt:
                    return
                cd.clients_connected[client] = {}
                cd.clients_connected[client]['client'] = client
                newConnection(client, address)
            except Exception:
                print(f"Failed while hadling client:\n")
                traceback.print_exc()


    def serverThread(self):
        while not self.shutdown == False:
            try:
                cmd = input("")
                command = ExecuteCommand(cmd)
                if command == "Unknown":
                    sendto("CONSOLE", "Unknown command.")
                else:
                    try:
                        command("CONSOLE")
                    except Exception as e:
                        logger.error(f"An error occured while executing a command!\n{e}")
            except EOFError:
                logger.info(f"Shutting down system...", "Server Thread")
                self.shutdown()

   
    def shutdown(self):
        self.shutdown = False
        logger.info(f"Shutting down...", "Shutdown Thread")
        time.sleep(0.3)
        
        logger.info(f"Stopping threads [{len(pd.threads)}]", "Shutdown Thread")
        stopallthreads()

        time.sleep(0.5)
        logger.info(f"Closing pending connections", "Shutdown Thread")
        logger.info(f"Disconnecting {len(cd.clients_connected)} connections", "Shutdown Thread")
        for c in cd.clients_connected:
            try:
                disconnect(c, "Server Closed", supersilent=True)
            except:
                pass

        time.sleep(0.7)
        logger.info(f"Closing listener [{self.host}:{self.port}]", "Shutdown Thread")
        try:
            self.server.close()
        except:
            pass
        
        logger.info(f"Bayeeeee have a greatful time!", "Shutdown Thread")
        forceexit()

    # def registerEvent(self, event, func):
    #     self.events.append({
    #         "event":  event,
    #         "func": func,
    #         "pluginname": "abc"
    #     })
        
    # def triggerEvent(self, event):
    #     for event in self.events:
    #         if event[event] == event:
    #                 event['func']()
                    
    # def triggerEventfromPlugin(self, event, plugin):
    #     for event in self.events:
    #             if event['pluginname'] == plugin:
    #                     event['func']()


def startup():
    pd.path['root'] = os.path.dirname(__file__)
    pd.path['sdroot'] = os.path.normpath(pd.path['root'] + "\\..\\server-data")
    pd.path['pluginroot'] = os.path.normpath(pd.path['sdroot'] + "\\Server.base\\plugins")
    pd.path['sessionids'] = pd.path['root'] + "\\sessionid.txt"
    pd.path['shutdown'] = Server().shutdown
    pd.path['hwid'] = get_hwid()

try:
    if os.name == "nt":
        os.system(f"title Server [Not listening]")
        startup()
        Server("run")
except KeyboardInterrupt:
    Server("shutdown")

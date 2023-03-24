from threading import *
import os

from csdata import gd

from log import logger

from client.Session import Session

from reader import argreader

from client.Connector import Connector


class Client:
    def __init__(self, type, args=None):
        if type == "run":
            self.main(args)
        elif type == "shutdown":
            if not self.shutdown == False:
                self.shutdown = False
                self.shutdown()
    
    def main(self, args):
        args = argreader.fetchargs(args)
        
        username = argreader.gvfa(args, "username")
        sessionid = argreader.gvfa(args, "sessionid")
        if username == "null" or sessionid == "null":
            exit()
        session = Session.session(username, sessionid)
        gd.session = session
        
        logger.info(f"Setting user: {session['username']}")
        logger.info(f"(Session ID is token:{session['token']})")
        
        thread = Thread(target=self.clientThread, args=()).start()
        gd.threads.append(thread)
        
    def clientThread(self):
        try:
            #input("")
            Connector()
        except EOFError:
            self.shutdown()


    def shutdown(self):
        logger.info(f"Stopping!", "Shutdown Thread")
        
        logger.info(f"Stopping threads [{len(gd.threads)}]", "Shutdown Thread")
        for thread in gd.threads:
            try:
                thread.shutdown
            except:
                pass

        # time.sleep(0.5)
        # logger.info(f"Closing pending connections", "Shutdown Thread")
        # logger.info(f"Disconnecting {len(cd.clients_connected)} connections", "Shutdown Thread")
        # for c in cd.clients_connected:
        #     try:
        #         disconnect(c, "Server Closed", supersilent=True)
        #     except:
        #         pass

        # time.sleep(0.5)
        # logger.info(f"Closing listener [{self.host}:{self.port}]", "Shutdown Thread")
        # try:
        #     self.server.close()
        # except:
        #     pass
        
        logger.info(f"Bayeeeee have a greatful time!\nKomischer error \/ :(", "Shutdown Thread")
        os._exit(-1)
        
        
def Main(args):
    try:
        Client("run", args)
    except KeyboardInterrupt:
        Client("shutdown")
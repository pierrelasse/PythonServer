import os

class sinfo:
    version = "1.0.0"

class cd:
    clients_connected = {}
    sessionids = []
    
class pd:
    threads = []
    path = {}
    
class plugins:
    lp = {}
    revents = []
    cache = {}
    
class commands:
    cmds = []
    load = None
    hperm = None
    aliases = []
    
class packets:
    pcks = []
    handlers = {}
    load = None
    
class sessionid:
    def loadids():
        path = pd.path['sessionids']
        
        if not os.path.isfile(path):
            open(path, 'w').close()

        with open(path, 'r') as f:
            pd.sessionids = f.readlines()

    def checkid(sess):
        for s in pd.sessionids:
            if str(sess).strip() == str(s).strip():
                return True
        return False
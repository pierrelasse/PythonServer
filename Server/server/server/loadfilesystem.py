from utils import makefolderifnotthere, makefileifnotthere

from log import logger

from reader import configreader

from csdata import pd


def loadfilesystem(self):
    cfgreader = configreader()
    
    path = pd.path['root'] + "\\..\\start.bat"
    makefileifnotthere(path)
    with open(path, 'w') as f:
        f.write("""@echo off & cd server\n:a\nServer.exe\necho Done & pause > nul & goto a""")

    # server-data
    path = pd.path['sdroot']
    makefolderifnotthere(path)

    # server-data/Server.base
    path = path + "\\Server.base"
    makefolderifnotthere(path)

    # server-data/Server.base/plugins
    makefolderifnotthere(path + "\\plugins")

    # server-data/Server.base/userdata
    #makefolderifnotthere(path + "\\userdata")

    # server-data/Server.base/server.properties
    makefileifnotthere(path + "\\server.properties")
    with open(path + "\\server.properties", 'r') as f:
        config = f.readlines()
    config = cfgreader.loadconfig(config)

    cfgreader.setvalue(config, "port", "53363", False)
    cfgreader.setvalue(config, "max_clients", "5", False)
    cfgreader.setvalue(config, "licenseKey", "", False)

    pd.serverproperties = config
    with open(path + "\\server.properties", 'w') as f:
        f.write("# Server Config\n# Epic text here!\n" + cfgreader.writeconfig(config))
        
    # Check Port | Fetch
    self.port = cfgreader.gvfc(config, "port")
    if self.port == "null":
        logger.error("Failed to fetch port from config!", "Config-Loader Thread")
        self.shutdown()
    
    # Check Port | IsNumber
    try:
        self.port = int(self.port)
    except:
        logger.error("The port needs to be a number!", "Config-Loader Thread")
        self.shutdown()
        
    # Check Port | IsValid
    if not 0 <= self.port <= 65535:
        logger.error(f"The port is not valid since {self.port} is out of range! (1 - 65535 i think hehe)", "Config-Loader Thread")
        self.shutdown()
        

    # License Key
    self.licenseKey = cfgreader.gvfc(config, "licenseKey")

        
    # server-data/default
    path = pd.path['sdroot'] + "\\default"
    makefolderifnotthere(path)

    # server-data/default/data
    path = path + "\\data"
    makefolderifnotthere(path)
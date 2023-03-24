import os
import ctypes
import subprocess
from threading import *

from csdata import cd, pd

from packet.coder import PacketCoder as packet

from log import logger

# from utils import 

def sendto(client, message):
    if client == "CONSOLE":
        logger.info(message, "Server Thread")
    else:
        try:
            client.send(packet.gen("message", message=message))
        except:
            pass

 
def broadcast(message):
    for c in cd.clients_connected:
        sendto(c, message)


def broadcastpacket(packet):
    for c in cd.clients_connected:
        try:
            c.send(packet)
        except:
            pass


def getaddress(client):
    host = "null"
    port = "null"
    try:
        host = cd.clients_connected[client]['host']
        port = cd.clients_connected[client]['port']
    except:
        pass

    return f"{host}:{port}"


def getusername(client):
    username = "null"
    try:
        username = cd.clients_connected[client]['username']
    except:
        pass
    return f"({cd.clients_connected[client]['client'].fileno()}) {username}"
def getuname(client):
    return getusername(client)


def isclientconnected(client):
    try:
        client.sendall(b"")
        return True
    except:
        return False


def makefolderifnotthere(path):
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except:
            pass

def makefileifnotthere(path):
    if not os.path.isfile(path):
        try:
            open(path, 'w').close()
        except:
            pass
        
def stopallthreads():
     for thread in pd.threads:
        try:
            thread.shutdown()
        except:
            pass
        

def messagebox(title, text, type=1):
    """
    MB_ABORTRETRYIGNORE = 2
    MB_CANCELTRYCONTINUE = 6
    MB_HELP = 0x4000
    MB_OK = 0
    MB_OKCANCEL = 1
    MB_RETRYCANCEL = 5
    MB_YESNO = 4
    MB_YESNOCANCEL = 3

    MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
    MB_ICONINFORMATION = MB_ICONASTERISK = 0x40
    MB_ICONQUESTION = 0x20
    MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10

    MB_DEFBUTTON1 = 0
    MB_DEFBUTTON2 = 0x100
    MB_DEFBUTTON3 = 0x200
    MB_DEFBUTTON4 = 0x300

    MB_APPLMODAL = 0
    MB_SYSTEMMODAL = 0x1000
    MB_TASKMODAL = 0x2000

    MB_DEFAULT_DESKTOP_ONLY = 0x20000
    MB_RIGHT = 0x80000
    MB_RTLREADING = 0x100000

    MB_SETFOREGROUND = 0x10000
    MB_TOPMOST = 0x40000
    MB_SERVICE_NOTIFICATION = 0x200000

    IDABORT = 3
    IDCANCEL = 2
    IDCONTINUE = 11
    IDIGNORE = 5
    IDNO = 7
    IDOK = 1
    IDRETRY = 4
    IDTRYAGAIN = 10
    IDYES = 6
    """
    try:
        return ctypes.windll.user32.MessageBoxW(None, str(text), str(title), int(type))
    except:
        pass
def messageboxnowait(title, text, type=1):
    thread = Thread(target=messagebox, args=(title, text, type))
    thread.start()
    pd.threads.append(thread)
    

"""THE BEST"""
def forceexit(code=-1):
    os._exit(code)
    
    
def get_hwid():
    try:
        return str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    except:
        try:
            return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())
        except:
            pass
    return "<error>"
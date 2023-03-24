import traceback

from packet.coder import PacketCoder as packet

from utils import broadcastpacket, getuname, getusername, sendto

from server.disconnect import disconnect

from csdata import cd

from log import logger

from client.command import ExecuteCommand

from plugin.pluginEvents import TriggerEvent


def clientThread(client):
    cc = client
    try:
        while True:
            r = thread(client)
            
            if r == True:
                disconnect(client)
                return

    except ConnectionResetError:
        disconnect(cc)

    except Exception as e:
        print(f"\n\nError while trying to handle packet:\n\n")
        traceback.print_exc()
        
        if client:
            reason = "Internal Server Error"
            disconnect(client, reason)
            clientThread(client)

    
def thread(client):
    try:
        data = client.recv(1024)
    except:
        return True

    p = packet.load(data)
    try:
        type = packet.gvfp(p, "type")
    except:
        type = "null"
    
    #print(f"[PACKET] {type}-=>{p}")
    from client.packets import HandlePacket
    
    resp = HandlePacket(type)
    if not resp == 404:
        resp(client, p)
    
    # KeepAlivePacket
    elif type == "keepalive":
        ...


    # ChatPacket
    elif type == "chat":
        message = packet.gvfp(p, "message")[0:90]
        if message == "null":
            return
        else:
            illegal = None
            if "§" in message:
                illegal = "§"
            elif "\033" in message:
                illegal = "\\033"
            if illegal:
                disconnect(client, "Illegal characters (§)")
                return
        username = getuname(client)
        format = "<[username]> [message]"
        a = format.replace("[username]", getusername(client)).replace("[message]", message)
        
        TriggerEvent("OnChat", client, message, format)
        
        logger.info(f"[CHAT] {a}", "Client Thread")
        broadcastpacket(packet.gen("chatmessage", username=username, message=message, format=format))
        

    #CommandPacket
    elif type == "command":
        cmd = packet.gvfp(p, 'command').lower()
        p = "/"
        logger.info(f"{getusername(client)} executed command: {cmd}", "Client Thread")
        # Commands
        command = ExecuteCommand(cmd[1:])
        
        TriggerEvent("OnCommand", client, cmd, command)
        
        if command == "Unknown":
            sendto(client, "Unknown command.")
        else:
            try:
                command(client)
            except Exception as e:
                sendto(client, "&cAn error occured while executing this command! Please check the console for more information.")
                logger.error("An error occured while executing a command!")
                traceback.print_exc()

    else:
        logger.warn(f"{getuname(client)} sent an unknown packet!")
        print(logger.color(f"""
&ePacket:
--------------------------------

{data}

--------------------------------
&eWarn End&r
""", "&"))
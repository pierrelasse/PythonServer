from threading import *

from csdata import cd, pd, sessionid

from packet.coder import PacketCoder as packet

from client.thread import clientThread

from event.joinEvent import Event as event_join

from server.disconnect import disconnect


def connectionHandler(client, address):
        print(f"[/{address[0]}:{address[1]}] Connected")
        
        try:
            loginpacket = client.recv(1024).decode('utf-8')
        except:
            disconnect(client, silent=True)
            return
        
        if not loginpacket:
            return
        
        cd.clients_connected[client]['id'] = client.fileno()
        cd.clients_connected[client]['host'] = address[0]
        cd.clients_connected[client]['port'] = address[1]
        
        loginpacket = packet.decode(loginpacket)
        
        if not packet.gvfp(loginpacket, "type") == "login":
            disconnect(client, "Invalid login packet", silent=True)
            return
        
        client_uuid = packet.gvfp(loginpacket, "uuid")
        cd.clients_connected[client]['uuid'] = client_uuid
        if not 0 <= len(client_uuid) <= 16:
            disconnect(client, "Invalid username", silent=True)
            return
        
        client_username = packet.gvfp(loginpacket, "username")
        cd.clients_connected[client]['username'] = client_username
        if len(client_username) > 16:
            disconnect(client, "Invalid username", silent=True)
            return
        
        client_sessionid = packet.gvfp(loginpacket, "sessionid")
        if sessionid.checkid(client_sessionid) == False:
            disconnect(client, "Unable to authenticate", silent=True)
            return
        
        
        print(f"{client_username}[/{address[0]}:{address[1]}] logged in")
        
        event_join(client)

        thread = Thread(target=clientThread, args=(client, )).start()
        pd.threads.append(thread)
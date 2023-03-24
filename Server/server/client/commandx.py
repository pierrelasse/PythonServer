import client.command

# #import importlib

# from utils import sendto

# from server.disconnect import disconnect

# from csdata import cd, plugins

# from log import logger


# def Command(client, cmd, p):
#     if cmd == p+"help":
#         sendto(client, "HELP HERE")

#     elif cmd == p+"reload":
#         sendto(client, logger.color("&cCommand is currently disabled", "&"))
#         #sendto(client, "Reloading...")
#         #importlib.reload(Command)
        
#     elif cmd == p+"kickall":
#         for c in cd.clients_connected:
#             disconnect(c, "Kicked by an Operator")
            
#     elif cmd == p+"plugins" or cmd == p+"pl":
#         pl = '&f, &a'.join(plugins.lp)
#         sendto(client, logger.color(f"&fPlugins ({len(plugins.lp)}): &a{pl}", "&"))
        
#     elif cmd == p+"triggerevent":
#         for event in plugins.revents:
#             for e in plugins.revents[event]:
#                 ecl = {
#                     "client": client
#                 }
#                 e(ecl)

#     else:
#         sendto(client, 'Unknown command. Use "/help" for help.')

from csdata import commands


def LoadCommands():
    commands.cmds = []
    
    import client.commands.StopCommand as command; commands.cmds.append(command.Command)
    import client.commands.PluginCommand as command; commands.cmds.append(command.Command)
    import client.commands.ReloadCommand as command; commands.cmds.append(command.Command)
    import client.commands.EventsCommand as command; commands.cmds.append(command.Command)
    import client.commands.ListCommand as command; commands.cmds.append(command.Command)
    
    commands.aliases = []
    for alias in commands.cmds:
        for a in alias.aliases:
            commands.aliases.append(a)
    

def ExecuteCommand(cmd):
    for command in commands.cmds:
        if cmd in command.aliases:
            return command.execute
    return "Unknown"

def HasPermission(client):
    if client == "CONSOLE":
        return True
    else:
        return False

commands.load = LoadCommands
commands.hperm = HasPermission
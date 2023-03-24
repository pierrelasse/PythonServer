# import pure-python

# from reader import argreader, configreader

"""
Argparser but better 😎
"""
class argreader:
    def fetchargs(argv, prefix="--"):
        args = {}

        for arg in argv:
            if arg.startswith(prefix):
                try:
                    arg = arg[int(len(prefix)):]
                    n = arg.split('=', 1)[0]
                    v = arg.split('=', 1)[-1]
                    if len(n) > 0 and len(v) > 0:
                        args[n] = v
                except:
                    pass
                
        return args

    def gvfa(args, value):
        v = "null"
        try:
            v = args[value]
        except:
            pass
        return v
    
# argreader = argreader()

# args = argreader.fetchargs(sys.argv()) # args: --test=something

# value1 = argreader.gvfa(args, "test") # = something or null if not set


"""
Config reader :D
"""
class configreader:
    def loadconfig(self, text):
        values = {}
        for a in text:
            a = str(a).strip()
            if not a.startswith("#") and "=" in a:
                n = a.split('=', 1)[0].split('#', 1)[0]
                v = a.split('=', 1)[-1].split('#', 1)[0].strip()
                if len(n) > 0:
                    values[n] = str(v)
        return values

    def writeconfig(self, config):
        values = ""
        for n in config:
            v = ""
            v = config[n]
            if len(n) > 0:
                values = values + f"{n}={v}\n"
        return values
    
    def setvalue(self, config, path, value, overwrite=True):
        if overwrite == False:
            try:
                if config[path]:
                    return config
            except:
                pass
        config[path] = value
        return config
    
    def gvfc(self, config, path):
        value = "null"
        try:
            value = config[path]
        except:
            pass
        return value
    
# cfgreader = configreader()

# configfile = 'config.properties'
# with open(configfile, 'r') as f:
#     config = f.readlines()
# config = cfgreader.loadconfig(config)

# cfgreader.setvalue(config, "name", "value", False)

# config = cfgreader.writeconfig(config)

# with open(configfile, 'w') as f:
#     f.write("#Header\n" + config)

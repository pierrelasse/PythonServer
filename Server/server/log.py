import time
import os
os.system("")

class logger:
    RESET = '\033[0m'

    def __gettime(self):
        return time.strftime("%H:%M:%S")
    
    def __hextorgb(self, h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    
    def __rgbtocolor(self, r, g, b):
        return f'\033[{38};2;{r};{g};{b}m'
    
    def __hextocolor(self, h):
        r = self.__hextorgb(h)
        return self.__rgbtocolor(r[0], r[1], r[2])
    
    def __strhex(self, text, prefix="§"):
        list = str(text).split(prefix)

        r = []
        for i in list:
            hex = i.split(">")[0]
            if hex.startswith("<"):
                hex = hex[1:]
                if len(hex) == 6:
                    i = i.replace(f"<{hex}>", self.__hextocolor(hex))
            r.append(i)
        return ''.join(r)
    
    def color(self, message, prefix="§"):
        message = message.replace(prefix + "0", self.__hextocolor("#000000"))
        message = message.replace(prefix + "1", self.__hextocolor("#0000AA"))
        message = message.replace(prefix + "2", self.__hextocolor("#00AA00"))
        message = message.replace(prefix + "3", self.__hextocolor("#00AAAA"))
        message = message.replace(prefix + "4", self.__hextocolor("#AA0000"))
        message = message.replace(prefix + "5", self.__hextocolor("#AA00AA"))
        message = message.replace(prefix + "6", self.__hextocolor("#FFAA00"))
        message = message.replace(prefix + "7", self.__hextocolor("#AAAAAA"))
        message = message.replace(prefix + "8", self.__hextocolor("#555555"))
        message = message.replace(prefix + "9", self.__hextocolor("#5555FF"))
        message = message.replace(prefix + "a", self.__hextocolor("#55FF55"))
        message = message.replace(prefix + "b", self.__hextocolor("#55FFFF"))
        message = message.replace(prefix + "c", self.__hextocolor("#FF5555"))
        message = message.replace(prefix + "d", self.__hextocolor("#FF55FF"))
        message = message.replace(prefix + "e", self.__hextocolor("#FFFF55"))
        message = message.replace(prefix + "f", self.__hextocolor("#FFFFFF"))
        
        message = message.replace(prefix + "r", self.RESET)
        
        message = self.__strhex(message, prefix)

        return message
    
    def _print(self, color, thread, type, message, prefix):
        time = self.__gettime()
        color = self.color(f"&{color}", "&")
        try:
            print(f"{color}[{time}] [{thread}/{type}] {self.color(message, prefix)}{self.RESET}")
        except:
            print(f"{color}[{time}] [{thread}/{type}]", message, self.RESET)

    def info(self, message, thread="Server Thread", prefix="§"):
        self._print("r", thread, "INFO", message, prefix)
    
    def error(self, message, thread="Server Thread", prefix="§"):
        self._print("c", thread, "ERROR", message, prefix)
        
    def warn(self, message, thread="Server Thread", prefix="§"):
        self._print("e", thread, "WARN", message, prefix)
        


logger = logger()
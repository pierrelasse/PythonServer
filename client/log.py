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
        return message

    def info(self, message, thread="Client Thread"):
        time = self.__gettime()
        print(f"[{time}] [{thread}/INFO] {self.color(message)}{self.RESET}")
    
    def error(self, message, thread="Client Thread"):
        time = self.__gettime()
        red = self.color("&c", "&")
        print(f"{red}[{time}] [{thread}/ERROR] {self.color(message)}{self.RESET}")

logger = logger()
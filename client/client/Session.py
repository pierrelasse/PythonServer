import random
import string

class Session:

    def session(username=None, sessionid=0):
        if not username:
            username = "Player"+''.join(random.choice(string.digits) for _ in range(3))
        session = {
            "username": str(username),
            "token": str(sessionid)
        }
        return session
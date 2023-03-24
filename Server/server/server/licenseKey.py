from log import logger

from csdata import pd

from utils import messagebox


def verifyKey(key):
    # :^)            \/ Working 2022 [No rat] [Not patched]
    keys = ['KEY_254-326-246-864', 'KEY_415-456-896-150']
    err = False
    
    logger.info("Authenticating server license key...", "svlicensecheck")
    
    if key in keys:
        logger.info("Server license key authentication succeeded. Welcome!", "svlicensecheck")
    elif key == "":
        err = "No key was specified."
    else:
        err = "The specified key does not exist."
        
    if err:
        err = f"Error: Could not authenticate server license key. {err}"
        logger.error(err, "svlicensecheck")
        messagebox("Fatal Error", err, 0x10 | 0x40000)
        pd.path['shutdown']()

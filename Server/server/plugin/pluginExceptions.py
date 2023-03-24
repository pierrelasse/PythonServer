
class NoIndexFile(Exception):
    def __init__(self, e=None):
        super().__init__(e)

class FailedToLoadIndex(Exception):
    def __init__(self, e=None):
        super().__init__(e)

class InvalidArguments(Exception):
    def __init__(self, e=None):
        super().__init__(e)
        
class PluginAlreadyLoaded(Exception):
    def __init__(self, e=None):
        super().__init__(e)
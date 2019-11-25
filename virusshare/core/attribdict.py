class AttribDict(dict):
    def __getattr__(self,name):
        return self[name] if name in self else None
    def __setattr__(self,name,value):
        self[name] = value

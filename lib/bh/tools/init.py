class Nothing:
    def __repr__(self,*a,**b):
        return '<NOTHING>'
NOTHING=Nothing()
class Namespace4Dict:
    def __init__(self,dikt):
        self.dikt=dikt
    def __getattr__(self,name):
        return self.__dict__['dikt'].get(name, NOTHING)

from importlib import import_module as imp
def main(*a,**b):
    MM= __name__ + '.' + '__main__'
    FN=imp(MM).main
    return FN(*a,**b)

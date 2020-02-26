import sys
from local.util import report, preparse, imp
class Namespace(): pass
#print(777, __name__)
def main(*a,**b):
    MM= __name__ + '.' + '__main__'
    FN=imp(MM).main
    return FN(*a,**b)
def __call__(self,*a,**b):
    print('ok')
#def __call__(*a,**b):
#    return fibo(*a,**b)
def _main(n, init=(1,1)):
    report(__name__, 'main', args )
    OPT,bang = args
    args, bang = preparse(OPT.args + bang)
    if not args:
        return null()
    cmd = args.pop(0)
    try:
        mod = imp( "%s.%s" % (__name__,cmd ))
    except ModuleNotFoundError:
        mod=None
    if mod == None:
        print('STUB: %s %s' % (cmd, args) )
    else:
        print('CALLING %s.main()' % mod.__name__ )
        mod.main(OPT, args)
def null():
    report(__name__, 'null', ())
    print( 'try -h' )


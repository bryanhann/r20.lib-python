def __call__(*a,**b):
    print( 'MATH:__init__:__call__: stub' )
#print('THEMATH.__init__', __name__ )
#from local.MATH.FIBO.__main__ import main as fibo
from local.util import report, preparse, imp
import sys
import os
def inject(mypath,mymod):
    from pathlib import Path
    this = Path(mypath)
    subcommands = [ x.stem for x in this.iterdir() if (x/'__init__.py').is_file() ]
    for cmd in subcommands:
        MOD=imp("%s.%s" % (__name__,cmd))
        setattr(mymod, cmd.lower(), MOD.__call__ )
#imodules() )
    print(__name__.split('.'))
#def test(): 5/0
def main(*args):
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


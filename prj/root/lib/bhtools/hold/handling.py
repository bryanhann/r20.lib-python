import sys
from pathlib import Path
from local.util import imp

def split_bang(args):
    bang=args[:]
    args = []
    while bang and not bang[0]=='!':
        args.append(bang.pop(0))
    return args, bang

def WithLocals_LC( _locals, target = '__main__.py' ):
    assert type(_locals)==type(locals())
    if not _locals['__name__'] == '__main__':
        raise Exception( "Use this function only if __name__=='__main__'" )
    prefix=_locals['__package__']
    root=_locals['__file__']
    suffix = Path(target).stem
    paths = top(root).glob('*/%s' % target)
    names = [xx.parent.stem for xx in paths]
    dotts=[dott_join( prefix, xx, suffix) for xx in names ]
    return dict( zip( names, dotts  ) )

def namespace4dict(dikt):
    class Namespace(): pass
    ret = Namespace()
    for item in dikt.items():
        ret.__setattr__( *item )
    return ret

def top(path):
    path=Path(path)
    if path.is_file():
        path = path.parent
    assert path.is_dir()
    return path
def stub(mod, msg):
    def inner(*x,**y):
        print("STUB %s: %s" % (str(mod), msg) )
    return inner
def WithLocals_handler( _locals, parser, fn4nameD ):
    D1=fn4nameD
    assert type(_locals)==type(locals())
    if not _locals['__name__'] == '__main__':
        raise Exception( "Use this function only if __name__=='__main__'" )
    LC = WithLocals_LC( _locals )
    args,bang = split_bang(sys.argv)
    OPTS = parser.parse_args(args)
    args=OPTS.args[2:] # cut off sys.argv and cmd
    cmd =  (OPTS.args+[''])[1]
    if cmd in D1.keys():
        fn = D1[cmd]
    elif cmd in LC.keys():
        mod = imp( LC[cmd] )
        fn = getattr(mod, '__subhandler', stub(mod.__name__, 'nohandler') )
    else:
        fn = lambda *x,**y : exit( 'unknown' )
    exit( fn(opts_list=[OPTS],args=args,bang=bang) )

def parent_parsers(package):
    parts = package.split('.')
    acc = []
    while parts:
        dott = '.'.join( parts + ['parse'])
        parts.pop()
        try:
            acc.append(imp(dott).parser)
        except (ModuleNotFoundError,AttributeError):
            continue
    return acc
def dott_join(*parts):
    return '.'.join(parts)


import hashlib
import datetime
import os
import shutil
import argparse
import sys
from importlib import import_module as imp
def modreport(xx):
    show='__doc__.__file__.__package__.__name__'.split('.')
    for k,v in xx.__dict__.items():
        if k in show:
            print((k,v))
    print()
def show(xx,depth):
    if depth > 3: return
    def show_dict(xx,depth=0):
        for key,val in xx.items():
            rhs = repr(val)
            if len(rhs)<60: return print( '%s%s ==> %s'% ('    '*depth, str(key).ljust(10), rhs[:60]))
            rhs = str(type(val))
            print( '%s%s ==> %s'% ('    '*depth, str(key).ljust(10), rhs[:60]))
            show(val, depth+1)
    def show_list(xx,depth):
        for item in xx:
            show(item,depth+1)
            print()
    if type(xx)==type({}):       show_dict(xx,depth)
    elif type(xx)==type([]):     show_list(xx,depth)
    elif hasattr(xx,'__dict__'): show_dict( xx.__dict__, depth )
def preparse(args):
    bang=args[:]
    args=[]
    while bang and not bang[0]=='!':
        args.append(bang.pop(0))
    return args,bang
def report(globalname, localname, args=None):
    print('%s: %s : %s' % (globalname, localname, str(args)))

from pathlib import Path, PosixPath

def padded(_list, n=5, v=''):
    return _list[:] + [v]*n
def getdefault(_list,_index,_default=''):
    try:
        return _list[_index]
    except IndexError:
        return _default

def unzip(pairs):
    a=[pair[0] for pair in pairs]
    b=[pair[1] for pair in pairs]
    return a,b
def prj(stuff,n):
    for item in stuff:
        yield( item[n] )
wrap = lambda fn_name : lambda obj : getattr( obj, fn_name )
lmap = lambda *a,**b : list(map(*a,**b))
lzip = lambda *a,**b : list(zip(*a,**b))
lprj = lambda *a,**b : list(prj(*a,**b))

def split_list(_list,_val):
    _list = _list[:]
    if _val in _list:
        n = _list.index(_val)
        return _list[:n], _list[n:]
    return _list, []
def get_local_parser(dott):
    import importlib
    aa = dott.split('.')
    aa.insert(-1, 'parsers' )
    aa = '.'.join(aa)
    mod = importlib.import_module(aa)
    return mod.parser
def md5(path):
    a=hashlib.md5()
    a.update(path.read_bytes())
    return a.hexdigest()

def walk(item):
    item = Path(item)
    if not item.exists():
        return
    if item.is_symlink():
        return
    if item.is_file():
        yield item
        return
    for subitem in item.iterdir():
        for xx in walk(subitem):
            yield xx

def append(log,entry,*x):
    with open(log, 'a') as fd:
        fd.write( entry + '\n' )

def dry( cmd, arglist, OPT ):
    out = "%s%s" % (cmd.__name__, repr(arglist) )
    if OPT.dryrun: 
        print( 'dryrun> %s' % out )
    elif OPT.verbose:
        print( 'verbose> %s' % out )
    if not OPT.dryrun:
        cmd(*arglist)

def defaultget( _list, _index, _default='' ):
    try:
        return _list[_index]
    except IndexError:
        return _default

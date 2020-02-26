LEVEL='C'
import argparse
help="Cosmetic option demonstrates inclusion of the '%s' parser" % LEVEL
subparser=argparse.ArgumentParser(prog=__name__, add_help=False)
subparser.add_argument( "--%s" % LEVEL, action="store_true", help=help)
subparser.add_argument( 
    "--exit" , 
    action="store", 
    help="exit with code",
    metavar='<ERR>'
)

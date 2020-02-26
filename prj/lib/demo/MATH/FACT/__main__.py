print('THEFACT.__MAIN__',__name__)
import sys
if __name__=='__main__':
    from local import imp
    foo = imp(__package__)
    print( sys.argv )
    print( __package__+'sf' )
    print(foo.__call__)
    arg = sys.argv[1]
    arg = int(arg)
    print( foo.__call__(arg))

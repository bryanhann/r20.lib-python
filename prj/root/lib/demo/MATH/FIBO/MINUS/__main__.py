import sys
from local import parser

parser.add_argument( 'arg', action='store', type=int )
parser.add_argument( '--init', action='store', nargs=2, default=[1,1])

def main(n, init=(1,1)):
    class Namespace: pass
    global G
    G=Namespace()
    G.MEMO={}
    G.MEMO={}
    G.MEMO[0]=init[0]
    G.MEMO[1]=init[1]
    return _fibo(n)

def _fibo(n):
    if n in G.MEMO:
        return G.MEMO[n]
    else:
        return _fibo(n-1) + _fibo(n-2)

if __name__=='__main__':
    OPT=parser.parse_args()
    result = main(
        int(OPT.arg),
        init = list(map(int,OPT.init))
    )
    result = - result
    if OPT.nolf:
        sys.stdout.write( str(result) )
    else:
        sys.stdout.write( str(result) + '\n' )

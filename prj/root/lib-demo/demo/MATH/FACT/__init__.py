import sys
from local.util import report, preparse, imp
def __call__(N):
    assert type(N)==type(1)
    assert N >= 0
    if N==0:
        return 1
    else:
        return N * __call__(N-1)

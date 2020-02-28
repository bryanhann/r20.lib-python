import bhtools.parse as __P

PP=__P.superparser(__package__)
DD=__P.dictionize_mip(__package__)


def dump(dikt):
    for item in dikt.items():
        print( '%s ==> %s\n' % item )

def test_dump(regtest):
    with regtest:
        dump(DD)

def main():
    opt = PP.parse_args()
    if opt.exit:
        exit(int(opt.exit))
    elif opt.dump:
        dump(DD)
    else:
        print( 'your opt was %s' % str(opt) )
        print( 'your args were %s' % str(opt.args) )
        print( 'try -h' )

if __name__=="__main__":
    main()

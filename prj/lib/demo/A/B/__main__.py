import bh.tools.parse as __P
if __name__=="__main__":
    opt = __P.superparser(__package__).parse_args()
    if opt.dump:
        exit("--dump is unimplemented at this level")
    print("try -h")

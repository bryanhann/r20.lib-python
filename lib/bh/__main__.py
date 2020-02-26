from bh.tools.parse import superparser
import sys
parser = superparser(__package__)
opt = parser.parse_args()
print( sys.argv )
print(opt)

import os
import glob
import sys

def retrieve(path):
    if os.path.isdir(path):
        print 'is dir'
        return glob.glob("{0}{1}".format(path, '*.txt'))
    elif os.path.isfile(path):
        return [path]
    else:
        print "Unable to get file(s) using {0}".format(path)
        sys.exit(0)

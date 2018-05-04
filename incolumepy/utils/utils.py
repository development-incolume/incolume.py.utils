import os
from platform import python_version

if python_version() < '3.0': range = xrange

DEBUG=True
DEBUG=False
def read(*rnames):
    '''
    return content from file informed in '*rnames'
    '''
    if DEBUG: open(os.path.join(os.path.dirname(__file__), *rnames)).read()
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

def namespace(s):
    '''
    return the namespace from to s='incolumepy.package.module'
    >>> namespace('incolumepy.package.module')
    '''
    if DEBUG: print (len(s.split('.')))
    l = []
    w = ''
    if len(s.split('.')) > 1:
        for i in range(len(s.split('.'))):
            if i == 0:
                w = s.split('.')[i]
                l.append(w)
            elif i>0 and i < len(s.split('.')) -1:
                w += '.' + s.split('.')[i]
                l.append(w)
    else:
        l.append(s.split('.')[0])
    return l


if __name__ == "__main__":
    pass

import os


def read(*rnames):
    '''
    return content from file informed in '*rnames'
    :param rnames:
    :return:
    >>> read(os.path.dirname(__file__), 'version.txt')
    0.2
    '''
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


def namespace(package_name):
    '''
    return the namespace from to s='incolumepy.package.module'
    :param s:
    :return:

    >>> namespace('incolumepy.package.module')
    ['incolumepy','incolumepy.package']

    >>> namespace('incolumepy')
    ['incolumepy']
    '''
    s = package_name.split('.')
    l = []
    if len(s)<=0:
        raise ValueError('package_name not can be void')
    elif len(s) == 1:
        l.append(package_name)
    else:
        for item in s[:-1]:
            print(item)
            if l:
                l.append('{}.{}'.format(l[-1], item))
            else:
                l.append(item)
            print(l)
    return l


if __name__ == "__main__":
    pass
    #namespace('incolumepy.package.subpackage.module')
    #namespace('incolumepy.package')
    namespace('incolumepy')
    namespace('')
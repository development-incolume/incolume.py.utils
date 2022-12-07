def nspace(e):
    # print(e)
    result = []
    try:
        elements, a = e.rsplit('.', maxsplit=1)
    except ValueError:
        return e
    # print(f"{elements=} {a=}")
    for item in elements.split('.'):
        pass
    return result


def void0():
    a = 'abcdefgh'
    result = ''
    for l in a:
        result += l
        print(result)


def void1():
    a = 'abcdefgh'
    result = []
    temp = ''
    for l in a[:-1]:
        temp = f'{temp}.{l}' if temp else l
        print(temp)
        result.append(temp)
    return result


def void2():
    a = 'incolume.py.package.subpackage.module'
    result = []
    temp = ''
    for bit in a.split('.')[:-1]:
        temp = f'{temp}.{bit}' if temp else bit
        print(temp)
        result.append(temp)
    return result


def void3(package_name: str = None):
    package_name = package_name or 'incolume.py.package.subpackage.module'
    result = []
    temp = ''
    for bit in package_name.split('.')[:-1]:
        temp = f'{temp}.{bit}' if temp else bit
        print(temp)
        result.append(temp)
    return result


def void4(package_name: str = None):
    # package_name = package_name or 'incolume.py.package.subpackage.module'
    result = []
    temp = ''
    bits = package_name.split('.')
    if len(bits) <= 1:
        return bits

    for bit in bits[:-1]:
        temp = f'{temp}.{bit}' if temp else bit
        # print(temp)
        result.append(temp)
    return result


def void5(package_name: str = None):
    # package_name = package_name or 'incolume.py.package.subpackage.module'
    result = []
    temp = ''
    try:
        bits = package_name.split('.')
    except AttributeError:
        return result

    if len(bits) <= 1:
        return bits

    for bit in bits[:-1]:
        temp = f'{temp}.{bit}' if temp else bit
        # print(temp)
        result.append(temp)
    return result


def run():
    print(

        s1 := 'incolume.py.package.module',
        nspace(s1),
        # s2 := 'incolume.module',
        # nspace(s2),
        # s3 := 'module',
        # nspace(s3),
        '',
        # void0(),
        # void1(),
        # void2(),
        # void3(),
        void5('module'),
        void5('package.module'),
        void5('incolume.py.package.subpackage.module'),
        void5(None),
        '',
        sep='\n'
    )


if __name__ == '__main__':  # pragma: no cover
    run()

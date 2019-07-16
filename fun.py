from pandas import DataFrame


def get_table(mod):
    t = []
    for v2 in range(mod):
        r = []
        for v1 in range(mod):
            r.append((v1 * v2) % mod)
        t.append(r)
    return t


def print_table(mod):
    t = get_table(mod)
    names = ['[' + str(v) + ']' for v in range(mod)]
    df = DataFrame(t, columns=names, index=names)
    print('\nMult-table mod =', mod)
    print(df)


def get_powers(mod):
    t = []
    for v in range(mod):
        r = []
        for p in range(1, mod):
            r.append((v ** p) % mod)
        t.append(r)
    return t


def print_powers(mod):
    t = get_powers(mod)
    print('\nPower table mod =', mod)
    for v in range(2, mod):
        print('[' + str(v) + ']:', t[v], 'order=' + str(get_order(v, mod)))


def get_order(v, mod):
    order = 0
    for p in range(2, mod):
        if (v ** p) % mod == 1:
            order = p
            break
    return order


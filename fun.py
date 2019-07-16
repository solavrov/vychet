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
        for p in range(1, mod + 1):
            r.append((v ** p) % mod)
        t.append(r)
    return t


def print_powers(mod):
    t = get_powers(mod)
    print('\nPower table mod =', mod)
    for v in range(2, mod):
        in_mod_power = str(t[v][-1])
        if in_mod_power == v:
            sign1 = '!!!'
        else:
            sign1 = ''
        order = get_order(v, mod)
        if order == mod - 1:
            sign2 = '*'
        else:
            sign2 = ''
        print('[' + str(v) + ']:',
              t[v][:-1],
              'power=mod:' + str(in_mod_power) + sign1,
              'order=' + str(order) + sign2)


def get_order(v, mod):
    order = 0
    for p in range(2, mod):
        if (v ** p) % mod == 1:
            order = p
            break
    return order


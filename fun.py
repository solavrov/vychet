from pandas import DataFrame


def get_table(mod):
    t = []
    for j in range(mod):
        r = []
        for i in range(mod):
            r.append((i * j) % mod)
        t.append(r)
    return t


def print_table(mod):
    t = get_table(mod)
    names = ['[' + str(e) + ']' for e in range(mod)]
    df = DataFrame(t, columns=names, index=names)
    print('\nMult-table mod =', mod)
    print(df)


def get_powers(mod):
    t = []
    for i in range(mod):
        r = []
        for p in range(1, mod):
            r.append((i ** p) % mod)
        t.append(r)
    return t


def print_powers(mod):
    t = get_powers(mod)
    print('\nPower table mod =', mod)
    for i in range(2, mod):
        print('[' + str(i) + ']:', t[i])

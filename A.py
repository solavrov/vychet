from itertools import product
from pandas import DataFrame


class A:
    table = None

    def __init__(self, i):
        self.i = i

    @staticmethod
    def set_table(table):
        A.table = table

    @staticmethod
    def print_table():
        print(DataFrame(A.table), '\n')

    def __mul__(self, other):
        return A(A.table[self.i][other.i])

    def __repr__(self):
        return 'A(' + str(self.i) + ')'

    def __eq__(self, other):
        return self.i == other.i

    def __ne__(self, other):
        return self.i != other.i

    @staticmethod
    def check_associativity():
        is_associative = True
        n = len(A.table)
        list_of_three = list(product(range(n), repeat=3))
        for e in list_of_three:
            if (A(e[0]) * A(e[1])) * A(e[2]) != A(e[0]) * (A(e[1]) * A(e[2])):
                print('Not associative, example: ', A(e[0]), '*', A(e[1]), '*', A(e[2]))
                is_associative = False
        if is_associative:
            print('Associativity is confirmed!')
        print('\n')

from fun import print_table, print_powers
from A import A

A.set_table([[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]])
A.print_table()
A.check_associativity()

A.set_table([[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 1, 0], [3, 2, 0, 1]])
A.print_table()
A.check_associativity()

A.set_table([[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]])
A.print_table()
A.check_associativity()

A.set_table([[0, 1, 2, 3], [1, 3, 0, 2], [2, 0, 3, 1], [3, 2, 1, 0]])
A.print_table()
A.check_associativity()

A.set_table([[0, 1, 2, 3, 4], [1, 2, 4, 0, 3], [2, 4, 3, 1, 0], [3, 0, 1, 4, 2], [4, 3, 0, 2, 1]])
A.print_table()
A.check_associativity()

A.set_table([[0, 1, 2, 3, 4], [1, 3, 0, 4, 2], [2, 4, 3, 1, 0], [3, 0, 4, 2, 1], [4, 2, 1, 0, 3]])
A.print_table()
A.check_associativity()

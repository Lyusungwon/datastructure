# Homework

import rbt as rb
import numpy as np
rbt = rb.RBT()
results = []
not_found = []
with open('input.txt') as inputfile:
    for line in inputfile:
        x = int(line)
        if x > 0:
            rbt.rb_insert(rb.Node(x))
        elif x < 0:
            min = rbt.bt_search(rbt.root, np.absolute(x))
            if min == -1:
                not_found.append(x)
            else:
                rbt.rb_delete(min)
        else:
            rbt.count_node()
            rbt.inorder_iter(rbt.root)
            print()

# Homework 06

import rbt as rb
import numpy as np

rbt = rb.RBT()
missed = []
with open('input.txt') as inputfile:
    for line in inputfile:
        x = int(line)
        if x > 0:
            rbt.rb_insert(rb.Node(x))
        elif x < 0:
            min = rbt.bt_search(rbt.root, np.absolute(x))
            if min == -1:
                missed.append(x)
            else:
                rbt.rb_delete(min)
        else:
            break
inputfile.close()

with open('search.txt') as inputfile:
    for line in inputfile:
        x = int(line)
        rbt.search_print(x)
inputfile.close()

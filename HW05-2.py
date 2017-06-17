# Homework 05-2

import rbt as rb
import numpy as np

rbt = rb.RBT()
missed = []
insert = 0
deleted = 0
with open('input.txt') as inputfile:
    print("file name =", inputfile.name)
    for line in inputfile:
        x = int(line)
        if x > 0:
            rbt.rb_insert(rb.Node(x))
            insert += 1
        elif x < 0:
            min = rbt.bt_search(rbt.root, np.absolute(x))
            if min == -1:
                missed.append(x)
            else:
                rbt.rb_delete(min)
                deleted += 1
        else:
            print("total =", insert - deleted)
            print("insert =", insert)
            print("deleted =", deleted)
            print("miss =", len(missed))
            rbt.count()
            rbt.inorder_iter(rbt.root)
            break

inputfile.close()

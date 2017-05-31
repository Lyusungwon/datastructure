# Homework

import rbt as rb
rbt = rb.RBT()
results = []
with open('input.txt') as inputfile:
    for line in inputfile:
        x = int(line)
        if x > 0:
            str("node", x)
            rb.Node(x)

        # results.append(line)
print(results)

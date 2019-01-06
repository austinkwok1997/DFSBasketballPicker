import numpy as np


def solve(salary, cost, points, n):
    K = np.zeros((n+1,salary+1))
    for i in range(n+1):
        for w in range(salary+1):
            if (i==0) or (w==0):
                K[i,w] = 0
            elif cost[i-1] <= w:
                K[i,w] = max(K[i-1,w],K[i-1,w-int(cost[i-1])] + points[i-1])
            else:
                K[i,w] = K[i-1,w]
    print(K[n,salary])
import numpy as np

N = 5

x1 = np.random.random(N)

x2 = [np.random.random(10)/10 for i in range(N)]
c1 = [x1, x2]
print(x1)
print('_____________')
print(x2)
print('_____________')
print(c1)
print('_____________')
print(c1[1])
print('_____________')
print(c1[1][1])

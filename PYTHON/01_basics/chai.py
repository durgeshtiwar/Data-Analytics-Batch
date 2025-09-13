# from hello_chai import chai
# chai("ginger tea")

# import numpy as np
import time
n = 5000
m1 = [[e for e in range(n)] for i in range(n)]
m2 = [[e for e in range(n)] for i in range(n)]
start = time.time()
for i in range(n):
  for j in range(n):
    m1[i][j]+m1[i][j]



end = time.time()
print("%6f sec"%(end-start))
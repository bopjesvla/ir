results = open('results-85-100.txt').read()

import re
import numpy as np

numbers = re.findall(r'[\d\.]+$', results, re.MULTILINE)
res = np.reshape(numbers, (-1, 3))

sim = res[:,0].astype(int)
map = res[:,1].astype(float)
p30 = res[:,2].astype(float)

print(sim)
print(p30)


import pandas as pd
from matplotlib import pyplot as plt

results = open('results-85-100.txt').read()

import re
import numpy as np

numbers = re.findall(r'[\d\.]+$', results, re.MULTILINE)
res = np.reshape(numbers, (-1, 3))
df = pd.DataFrame(res).astype({0: int, 1: float, 2: float})
df.columns = ['Minimal Synonym Similarity', 'MAP', 'P30']
ax = df.plot('Minimal Synonym Similarity', ['MAP', 'P30'])
plt.show()

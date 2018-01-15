import sys
print(sys.path)

import numpy
import matplotlib.pyplot as plt

years = [1990, 1999, 2000, 2001, 2002, 2003]
pop = [12, 14, 20, 32, 39, 49]

# plt.plot(years, pop)
plt.plot(years, pop)
# plt.xscale('log')
plt.show()
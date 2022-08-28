from calendar import c
from matplotlib.pyplot import clim
import numpy as np

import numpy as np

kanto = np.array([73,67,43])

weights = np.array([0.3,0.2,0.5])

print(type(weights))

dp = np.dot(kanto,weights)
print(dp)

print(kanto * weights)
print((kanto * weights).sum())

climate_data = np.array([[73,67,43],[91,88,64],[87,134,58],[102,43,37],[69,96,70]])

print(climate_data.shape)

print(np.matmul(kanto, weights))


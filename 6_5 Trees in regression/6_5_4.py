import numpy as np
from sklearn import tree

x = np.arange(-2, 3, 0.1).reshape(-1, 1)
y = 0.3 * x ** 2 - 0.2 * x ** 3 - 0.5 * np.sin(4*x)

# здесь продолжайте программу
clf = tree.DecisionTreeRegressor(max_depth=4)
clf.fit(x, y)
pr_y = clf.predict(x).reshape(-1, 1)
Q  = np.mean((pr_y[1:]-y[1:])**2)

print(Q)
import matplotlib.pyplot as plt
plt.plot(x, y, c='g', label="origin")
plt.plot(x, pr_y, c='r', label="regression tree")
plt.legend()
plt.show()
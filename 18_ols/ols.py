import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# Vector
x = np.arange(0, 1, 0.01)
y = 2 * x + np.random.randn(len(x))

X = np.matrix(x).T
Y = np.matrix(y).T
X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()
model.summary()

plt.figure(figsize=(10, 6), dpi=300)
plt.scatter(x, y)
plt.plot(x, Y_predict)
plt.grid()
plt.savefig("plot.png")


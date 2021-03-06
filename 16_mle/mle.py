import matplotlib.pyplot as plt
import numpy as np

# Import netCDF file

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(r"Title", fontsize=16)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$y$', fontsize=14)

# Prepare Data to Plot
x = np.arange(1, 5, 0.1)
err = np.random.randn(len(x))
y = 2 * x + 3 + err

x_bar = np.average(x)
y_bar = np.average(y)
xy_bar = np.dot(x, y) / len(x)
x2_bar = np.dot(x, x) / len(x)

a = (xy_bar - x_bar * y_bar) / (x2_bar - x_bar ** 2)
b = y_bar - a * x_bar

x_model = np.arange(1,5,0.01)
y_model = a * x_model + b

# Plot with Legends
plt.scatter(x, y, label='Data')
plt.plot(x_model, y_model, label=r'$y={}x + {}$'.format(a, b))

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig("plot.png", dpi=300)

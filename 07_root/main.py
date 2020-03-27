from bisect_method import bisect, log
import numpy as np
import matplotlib.pyplot as plt

# Root
root1 = bisect(lambda x: 2**x - 2 - x, 0, 10)
root2 = bisect(lambda x: x - log(x+2, 2), 0, 10)
root3 = bisect(lambda x: 2**x - 2 - log(x+2, 2), 0, 10)

print(root1)
print(root2)
print(root3)

# Plot
x = np.arange(-1, 4, 0.01)
y1 = np.power(2, x) - 2
y2 = np.log2(x+2)
y3 = x

plt.figure(figsize=(10,6), dpi=300)
plt.title("Graph for exp, log")
plt.plot(x, y1, label="Exp")
plt.plot(x, y2, label="Log")
plt.plot(x, y3, label="x")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("graph.png")

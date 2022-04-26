import numpy as np
import matplotlib.pyplot as plt

import FirstDerivativeMethod
import Function
import SecondDerivativeMethod

step = 0.1
x = np.arange(-3, 3, step)
y = np.arange(-10, 10, step)
X, Y = np.meshgrid(x, y)
f = Function.RosenbrockFunction(1.0, 5.0)
Z = f.v_draw(X, Y)
fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
# x_path, y_path = FirstDerivativeMethod.steepest_descent_method(f, [-3, - 3], 0.001, 200)
# x_path, y_path = SecondDerivativeMethod.new_town_method(f, [-3, - 3], 0.001, 200)
x_path, y_path = SecondDerivativeMethod.dfp_method(f, [-3, - 3], 0.001, 200)
print(x_path)
print(y_path)
cs = ax.contour(X, Y, Z, 100)
plt.clabel(cs, fontsize=10, colors=['red', 'red', 'white'])
plt.plot(x_path, y_path, linewidth=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.xticks(np.arange(-3, 3, 0.4))
plt.yticks(np.arange(-10, 10, 1))
plt.tight_layout()
plt.show()

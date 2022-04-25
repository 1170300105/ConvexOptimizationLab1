import numpy as np


# 罗森布鲁克函数 Rosenbrock
# f(x,y) = (1-x)^2 + 100(y-x^2)^2.
# 该函数非凸但具有唯一极小值点(1,1)
class RosenbrockFunction:
    @staticmethod
    def v_list(pos: list):
        x = pos[0]
        y = pos[1]
        return (1 - x) * (1 - x) + 100 * (y - x ** 2) ** 2

    @staticmethod
    def v(x, y):
        return (1 - x) * (1 - x) + 100 * (y - x ** 2) ** 2

    @staticmethod
    def g_list(pos):
        x = pos[0]
        y = pos[1]
        return RosenbrockFunction.g(x, y)

    @staticmethod
    def g(x, y):
        return [400 * x * (x * x - y) + 2 * x - 2, 200 * (y - x ** 2)]

    @staticmethod
    def h(x, y):
        return [[1200 * x * x - 400 * y + 2, -400 * x], [-400 * x, 200]]

    @staticmethod
    def h_list(pos):
        x = pos[0]
        y = pos[1]
        return RosenbrockFunction.g(x, y)


class RosenbrockLambdaFunction:
    dx = 0.0
    dy = 0.0
    x0 = 0.0
    y0 = 0.0

    def __init__(self, dx, dy, x0, y0):
        self.dy = dy
        self.dx = dx

    def v(self, l):
        return RosenbrockLambdaFunction.v(self.x0 + l * self.dx, self.y0 + l * self.yx)

    def d(self, l):
        g = RosenbrockFunction.g(self.y0 + l * self.yx)
        return g[0] * self.dx + g[1] * self.dy

    def d2(self, l):
        y1 = self.y0 + l * self.yx
        x1 = self.x0 + l * self.dx
        return 2 * (self.dx ** 2) - 400 * (y1 - x1 ** 2) * (self.dx ** 2) + 200 * (self.dy - 2 * x1 * self.dx) ** 2


class LambdaFunction:
    def __init__(self, f, pos, d):
        self.f = f
        self.pos = pos
        self.d = d

    def v(self, l):
        return self.f.v_list((self.pos + l * self.d).tolist())


# y = (x - 1)^2
class SimpleTest:
    @staticmethod
    def v_list(pos):
        x = pos[0]
        return (x - 1.0) ** 2

    @staticmethod
    def v(x):
        return (x - 1.0) ** 2

    @staticmethod
    def g(pos):
        x = pos[0]
        return [2*x]


if __name__ == '__main__':
    print("___END___\n")

import numpy as np


# 罗森布鲁克函数 Rosenbrock
# f(x,y) = (a-x)^2 + b(y-x^2)^2.
# 该函数非凸但具有唯一极小值点(1,1)
class RosenbrockFunction:
    def __init__(self, a=1, b=10):
        self.a = a
        self.b = b

    def v_list(self, pos: list):
        x = pos[0]
        y = pos[1]
        return (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2

    def v(self, x, y):
        return (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2

    def g_list(self, pos):
        x = pos[0]
        y = pos[1]
        return self.g(x, y)

    def g(self, x, y):
        return [4 * self.b * x * (x * x - y) + 2 * (x - self.a), 2 * self.b * (y - x ** 2)]

    def h(self, x, y):
        return [[12 * self.b * x * x - 4 * self.b * y + 2, -4 * self.b * x], [-4 * self.b * x, 2 * self.b]]

    def h_list(self, pos):
        x = pos[0]
        y = pos[1]
        return self.h(x, y)

    # 为画图用的求值函数

    def v_draw(self, x, y):
        return (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2


class RosenbrockLambdaFunction:
    dx = 0.0
    dy = 0.0
    x0 = 0.0
    y0 = 0.0

    def __init__(self, dx, dy, x0, y0, a, b):
        self.dy = dy
        self.dx = dx
        self.x0 = x0
        self.y0 = y0
        self.f = RosenbrockLambdaFunction(a, b)

    def v(self, l):
        return f.v(self.x0 + l * self.dx, self.y0 + l * self.dy)

    def d(self, l):
        g = f.g(self.x0 + l * self.dx, self.y0 + l * self.dy)
        return g[0] * self.dx + g[1] * self.dy

    def d2(self, l):
        y1 = self.y0 + l * self.dy
        x1 = self.x0 + l * self.dx
        return 2 * (self.dx ** 2) - 400 * (y1 - x1 ** 2) * (self.dx ** 2) + 200 * (self.dy - 2 * x1 * self.dx) ** 2


class LambdaFunction:
    def __init__(self, func, pos, d):
        self.f = func
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
        return [2 * x]

    @staticmethod
    def h(pos):
        x = pos[0]
        return [2]


if __name__ == '__main__':
    f = RosenbrockFunction(1, 5)
    print(f.v(1, 1))
    print("___END___\n")

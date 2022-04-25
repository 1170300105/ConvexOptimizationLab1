# 罗森布鲁克函数 Rosenbrock
# f(x,y) = (1-x)^2 + 100(y-x^2)^2.
# 该函数非凸但具有唯一极小值点(1,1)
class RosenbrockFunction:
    def f(self, x, y):
        return (1 - x) * (1 - x) + 100 * (y - x ** 2) ** 2

    def g(self, x, y):
        return [400 * x * (x * x - y) + 2 * x - 2, 200 * (y - x ** 2)]

    def H(self, x, y):
        return [[1200 * x * x - 400 * y + 2, -400 * x], [-400 * x, 200]]


class RosenbrockLambdaFunction:
    dx = 0.0
    dy = 0.0
    x0 = 0.0
    y0 = 0.0

    def __init__(self, dx, dy, x0, y0):
        self.dy = dy
        self.dx = dx

    def f(self, l):
        return RosenbrockLambdaFunction.f(self.x0 + l * self.dx, self.y0 + l* self.yx)


if __name__ == '__main__':
    print("___END___\n")

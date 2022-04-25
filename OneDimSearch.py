import Function


# 黄金分割法-一维搜索
def golden_partition_search(f, area, limit):
    l = area[0]
    r = area[1]
    k = 0.6180339887
    a = l + (1 - k) * (r - l)
    b = l + k * (r - l)
    while b - a < limit:
        va = f.v(a)
        vb = f.v(b)
        if va >= vb:
            l = a
            a = b
            b = l + k * (r - l)
        else:
            r = b
            b = a
            a = l + (1 - k) * (r - l)
    return (a + b) / 2


# 进退法-确定粗略区间
def search_area_get(f, limit_count, step_length, init_val=0):
    d0 = init_val + step_length * 20

    for i in range(limit_count):
        d1 = d0 + step_length
        v0 = f.v(d0)
        v1 = f.v(d1)
        if v0 > v1:
            while v0 > v1:
                step_length *= 2
                d2 = d1 + step_length
                v2 = f.v(d2)
                if v2 >= v1:
                    return [d0, d2]
                else:
                    d0, v0 = d1, v1
                    d1, v1 = d2, v2
        elif v0 < v1:
            while v0 < v1:
                step_length *= 2
                d2 = d0 - step_length

                v2 = f.v(d2)
                if v2 >= v0:
                    return [d2, d1]
                else:
                    d1, v1 = d0, v0
                    d0, v0 = d2, v2
        else:
            return [d0, d1]


if __name__ == '__main__':
    print(search_area_get(Function.SimpleTest, 20, 0.25, -10))
    print(search_area_get(Function.SimpleTest, 20, 0.25, 4))
    print("___END___\n")
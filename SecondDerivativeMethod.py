import numpy as np

import Function
import OneDimSearch


def new_town_method(f, init_pos, end_limit, count_limit):
    init_pos = np.array(init_pos, dtype='float64')
    search_path_x = [init_pos.tolist()[0]]
    search_path_y = [init_pos.tolist()[1]]
    count = 0
    while count < count_limit:
        count += 1
        g = f.g_list(init_pos)
        d = np.array(g) * -1
        h = np.array(f.h_list(init_pos), dtype='float64')
        inv = np.linalg.inv(h)
        d = np.dot(inv, g)
        fl = Function.LambdaFunction(f, init_pos, d)
        area = OneDimSearch.search_area_get(fl, 1000, 0.25, -5)
        step = OneDimSearch.golden_partition_search(fl, area, 0.000001)
        new_pos = init_pos + step * d
        print(new_pos)
        search_path_x.append(new_pos.tolist()[0])
        search_path_y.append(new_pos.tolist()[1])
        if np.linalg.norm(new_pos - init_pos) < end_limit:
            break
        init_pos = new_pos
    return search_path_x, search_path_y


def dfp_method(f, init_pos, end_limit, count_limit):
    search_path = []

    return search_path


def bfgs_method(f, init_pos, end_limit, count_limit):
    search_path = []
    return search_path

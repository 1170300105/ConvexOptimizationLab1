import numpy as np
import Function
import OneDimSearch


def cyclic_coordinate_method(f, init_pos, end_limit, count_limit):
    init_pos = np.array(init_pos, dtype='float64')
    search_path_x = [init_pos.tolist()[0]]
    search_path_y = [init_pos.tolist()[1]]
    n = len(init_pos)
    count = 0
    while count < count_limit:
        d = [0] * n
        d[count % n] = 1
        d = np.array(d)
        fl = Function.LambdaFunction(f, init_pos, d)
        area = OneDimSearch.search_area_get(fl, 1000, 0.25, -5)
        step = OneDimSearch.golden_partition_search(fl, area, 0.000001)
        new_pos = init_pos + step * d
        search_path_x.append(new_pos.tolist()[0])
        search_path_y.append(new_pos.tolist()[1])
        if np.linalg.norm(new_pos - init_pos) < end_limit:
            break
        init_pos = new_pos
        count += 1
    return search_path_x, search_path_y


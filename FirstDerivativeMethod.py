import numpy as np
import Function
import OneDimSearch


def steepest_descent_method(f, init_pos, end_limit, count_limit):
    v0 = f.v_list(init_pos)
    init_pos = np.array(init_pos)
    search_path_x = [init_pos.tolist()[0]]
    search_path_y = [init_pos.tolist()[1]]
    log = []
    count = 0
    while count < count_limit:
        count += 1
        g = f.g_list(init_pos)
        d = np.array(g) * -1
        fl = Function.LambdaFunction(f, init_pos, d)
        area = OneDimSearch.search_area_get(fl, 1000, 0.25, -5)
        step = OneDimSearch.golden_partition_search(fl, area, 0.000001)
        new_pos = init_pos + step * d
        v_new = f.v_list(new_pos.tolist())
        search_path_x.append(new_pos.tolist()[0])
        search_path_y.append(new_pos.tolist()[1])
        log.append("init = " + str(init_pos.tolist()) + ",g = " + str(g) + "area = " + str(area) + "step = "
                   + str(step) + "new pos = " + str(new_pos.tolist()) + "v = " + str(v_new))
        if np.linalg.norm(new_pos - init_pos) < end_limit:
            break
        init_pos = new_pos
    return search_path_x, search_path_y


if __name__ == '__main__':
    res = steepest_descent_method(Function.SimpleTest, [-200], 0.001, 200)
    for path in res:
        print(path)
    print("___END___\n")

import numpy as np
import Function
import OneDimSearch


def steepest_descent_method_hd(f, init_pos, end_limit, count_limit):
    v0 = f.v_list(init_pos)
    init_pos = np.array(init_pos)
    search_path_x = [init_pos.tolist()[0]]
    search_path_y = [init_pos.tolist()[1]]
    log = []
    count = 0
    dlast = np.array(f.g_list(init_pos)) * -1
    dlast /= np.linalg.norm(dlast)
    step = 0.05
    print(step)
    new_pos = init_pos + step * dlast
    init_pos = new_pos
    search_path_x.append(init_pos.tolist()[0])
    search_path_y.append(init_pos.tolist()[1])
    beta = 0.1
    print(search_path_x)
    print(search_path_y)
    while count < count_limit:
        count += 1
        g = f.g_list(init_pos)
        d = np.array(g)/np.linalg.norm(g) * -1
        step = step + beta * np.dot(d, dlast)
        new_pos = init_pos + step * d
        search_path_x.append(new_pos.tolist()[0])
        search_path_y.append(new_pos.tolist()[1])
        if np.linalg.norm(new_pos - init_pos) < end_limit or np.linalg.norm(g) < end_limit:
            break

        init_pos = new_pos
        dlast = d
    print(count)
    return search_path_x, search_path_y

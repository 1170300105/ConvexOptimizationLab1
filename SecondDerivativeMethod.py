import numpy as np


def new_town_method(f, init_pos, end_limit, count_limit):
    search_path = []
    init_pos = np.array(init_pos)
    search_path = []
    count = 0
    while count < count_limit:
        count += 1
        g = f.g(init_pos)
        d = np.array(g) * -1
        h = np.array(f.h_list(init_pos))
        new_pos = init_pos + np.linalg.inv(h) * d
        if np.linalg.norm(new_pos - init_pos) < end_limit:
            break
        init_pos = new_pos
    return search_path

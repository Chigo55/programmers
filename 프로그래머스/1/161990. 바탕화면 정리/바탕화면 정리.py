def solution(wallpaper):
    ans = []
    pos = []
    for idx, val_x in enumerate(wallpaper):
        for idy, val_y in enumerate(val_x):
            if val_y == '#':
                pos.append([idx, idy])

    pos.sort(key=lambda x: x[0])
    pos = list(zip(*pos))

    max_x, min_x = max(pos[0])+1, min(pos[0])
    max_y, min_y = max(pos[-1])+1, min(pos[-1])
    ans.extend([min_x, min_y, max_x, max_y])

    return ans
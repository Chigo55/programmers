def solution(num_list, n):
    import numpy as np
    ans = np.reshape(num_list, (-1, n))
    return ans.tolist()
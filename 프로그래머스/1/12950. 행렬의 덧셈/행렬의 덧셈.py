def solution(arr1, arr2):
    import numpy as np
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    ans = arr1 + arr2
    return ans.tolist()
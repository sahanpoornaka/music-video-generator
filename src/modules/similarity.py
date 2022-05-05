import numpy as np
from scipy.spatial import distance


def calculate_cosine_distance(mtx_A, mtx_B):

# A = np.array([[1,2,3,2,5,6,2,2,6,2],[12,4,5,5],[1,2,4],[1],[2],[2]], dtype=object )
# B = np.array([[2,3,4,5,2,4,3,4,5,6],[12,4,5,5],[1,2,4],[1],[2],[2]], dtype=object )

    Aflat = np.hstack(mtx_A)
    Bflat = np.hstack(mtx_B)

    dist = distance.cosine(Aflat, Bflat)

    return dist
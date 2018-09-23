import numpy as np


def prod_non_zero_diag(x):
    diag = np.diag(x)
    return diag[diag.nonzero()].prod()

def are_multisets_equal(x, y):
    return np.array_equal(np.bincount(x), np.bincount(y))

def max_after_zero(x):
    indices = np.where(x == 0)[0] + 1
    indices = indices[np.where(indices < len(x))]
    if len(indices) == 0:
        return None
    return max(x[indices])

def convert_image(img, coefs):
    return np.dot(img, coefs)

def run_length_encoding(x):
    ind = np.nonzero(x[1:] != x[:-1])[0]
    elems = np.append(x[ind], x[-1])
    ind = np.append([0], ind + 1)
    ind = np.append(ind, [x.shape[0]])
    counters = ind[1:] - ind[:-1]
    return elems, counters

def pairwise_distance(x, y):
    return np.linalg.norm(x[:, :, None] - y[:, :, None].T, axis=1)
    

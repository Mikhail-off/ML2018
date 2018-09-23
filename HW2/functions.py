import collections
from math import sqrt

def prod_non_zero_diag(x):
    prod = 1
    for i in range(min(len(x), len(x[0]))):
        if x[i][i] != 0:
            prod *= x[i][i]
    return prod

def are_multisets_equal(x, y):
    firstSet = collections.Counter(x)
    secondSet = collections.Counter(y)
    return firstSet == secondSet

def max_after_zero(x):
    toRet = None
    for i in range(1, len(x)):
        if toRet == None and x[i - 1] == 0:
            toRet = x[i]
        elif x[i - 1] == 0 and x[i] > toRet:
            toRet = x[i]
    return toRet 

def convert_image(img, coefs):
    num_channels = len(coefs)
    h = len(img)
    w = len(img[0])
    res_img = [ [0]*w for _ in range(h) ]
    for y in range(h):
        for x in range(w):
            for ch in range(num_channels):
                res_img[y][x] += coefs[ch] * img[y][x][ch]
    return res_img

def run_length_encoding(x):
    elems = []
    counters = []
    if len(x) == 0:
        return elems, counters
    elems.append(x[0])
    counters.append(1)
    for elem in x[1:]:
        if elems[-1] == elem:
            counters[-1] += 1
        else:
            elems.append(elem)
            counters.append(1)
    return elems, counters

def pairwise_distance(x, y):
    gramm_matrix = [ [0.0]*len(x) for _ in range(len(y)) ]
    for i in  range(len(x)):
        for j in range(len(y)):
            vec1 = x[i]
            vec2 = y[j]
            for k in range(len(vec1)):
                gramm_matrix[i][j] += (vec1[k] - vec2[k])**2
            gramm_matrix[i][j] = sqrt(gramm_matrix[i][j])
    return gramm_matrix


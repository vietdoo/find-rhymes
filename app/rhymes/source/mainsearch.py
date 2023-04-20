from app.rhymes.source.utils import *
from app.rhymes.source.varient import *

def giong_am(word):
    q = str(phu_am_khong_dau(word))
    if (q in W) :
        return W[q]
    return []

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def rap(word):
    d = giong_am(word)
    a = []
    q = str(phu_am_co_dau(word))
    for i in d:
        p = str(phu_am_co_dau(i))
        a.append(similar(q, p))
    d = [x for _, x in sorted(zip(a, d), reverse=True)]
    return d
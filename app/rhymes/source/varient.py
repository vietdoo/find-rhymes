
from app.rhymes.source.utils import *

W = {}

with open("app/rhymes/data/200k.txt", 'r', encoding="utf8") as f:
    data = f.read()
words = data.split('\n')

for i in range(len(words)):
    num = i
    pa1 = phu_am_khong_dau(words[num])
    q = str(pa1)
    if (q in W):
        W[q].append(words[num])
    else:
        W[q] = [words[num]]


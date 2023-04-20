import pandas as pd
import random
import re
from difflib import SequenceMatcher
from app.rhymes.source.para import *


def clean_string(s):
    s = s.lower()
    s = s.replace('\'', '')
    s = s.replace('"', '')
    s = s.replace('-', ' ')
    s = s.replace('!', ' ')
    s = s.replace('  ', ' ')
    return s

def khong_dau(word):
    output = word
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

def nice_word(word):
    word = word.replace('ay', 'ai')
    word = word.replace('iêc', 'iêt')
    return word

def phu_am_khong_dau(word):
    pa = []
    for i in word.split(' '):
        w = khong_dau(i)
        w = nice_word(w)
        for na in NA:
            if (w.startswith(na) or w.startswith(na.capitalize())):
                w = w[len(na):]
                break
        pa.append(w)
    return pa

def phu_am_co_dau(word):
    pa = []
    for i in word.split(' '):
        w = nice_word(i)
        for na in NA:
            if (w.startswith(na) or w.startswith(na.capitalize())):
                w = w[len(na):]
                break
        pa.append(w)
    return pa


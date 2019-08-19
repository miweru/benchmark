#!/usr/bin/env python3
from setuptools import setup
import random
import cProfile
import string
from time import time
from collections import Counter
from scipy.sparse import lil_matrix
from sklearn.decomposition import TruncatedSVD
from somajo import Tokenizer



def b1():
    t=time()
    words = ["".join(random.choices(string.ascii_letters, k=5)) for _ in range(10000000)]
    wordc = Counter(words).most_common()
    w2id = {w:i for i,w in enumerate(wordc)}
    id2w = {v:k for k,v in enumerate(w2id)}
    print(time()-t)

def b2():
    t=time()
    _ = Tokenizer().tokenize("".join(random.choices(string.printable,k=1000000)))
    print(time()-t)
    
def b3():
    t=time()
    matrix = lil_matrix((1000,200000))
    for _ in range(2000000):
        i, j = random.randint(0,999), random.randint(0,199999)
        matrix[i,j]=random.random()
    matrix = matrix.tocsc()
    pca = TruncatedSVD(n_components=10)
    target = pca.fit_transform(matrix)
    print(time()-t)

def benchmark(*args,**kwargs):
    random.seed(42)
    print("="*30)
    print("Count Words and build dict")
    cProfile.run("b1()")
    print("="*30)
    print("Tokenize")
    cProfile.run("b2()")
    print("="*30)
    print("Count Words and build dict")
    cProfile.run("b3()")

benchmark()

setup = benchmark

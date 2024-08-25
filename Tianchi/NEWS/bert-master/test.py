import numpy as np
import tensorflow as tf
time_v = "0.023 0.023 0.023 0.0 0.114 0.0 0.136 0.136 0.227 0.159 0.045 0.0 0.0 0.0 0.0 0.0 0.068 0.0 0.023 0.0 0.0 0.0 0.0 0.023"
veclist = []
vec = []
for i in time_v.split(' '):
    veclist.append(float(i))
    print(veclist)
vec.append(veclist)
vec.append(veclist)
print(vec)
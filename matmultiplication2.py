import mxnet as mx
from mxnet import nd

import numpy as np
import time

dim=3

x1=nd.ones((dim,dim))
y1=nd.ones((dim,dim))
x2=np.ones((dim,dim))
y2=np.ones((dim,dim))

start_time=time.time()
np.dot(x2,y2)
stop_time=time.time()

print(stop_time-start_time)


start_time=time.time()
nd.dot(x1,y1)
stop_time=time.time()

print(stop_time-start_time)

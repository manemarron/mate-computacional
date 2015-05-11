import numpy as np
def euler(y,dy,tau,N):
    dt = tau / float(N-1)
    for t in xrange(N-1):
        y[t+1]=y[t] + dy(y[t])*dt
    return y
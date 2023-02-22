import numpy as np
from scipy.optimize import minimize
#Number of Frames
M=2
#Max packet length
MTU=1500
#Probabillity distribuion of each packet length
alpha = np.zeros(MTU+1)
file = open("distribution.txt")
for i,j in zip(range(0,MTU+1),file.read().split("\n")):
    alpha[i] = float(j)
file.close()
#Objective function is the sum of all  alpha[k-1]*P(k), where is the length of the packets going from 1 to MTU and P(k) is the padding of the length k
def averageCost(X):
    ac = 0
    FW = np.zeros(M+1)
    for i,j in zip(range(1,M+1),range(0,M)):
        Xm = int(np.floor(X[j]))
        FW[i] = np.sum(alpha[0:Xm+1])
        ac = ac + Xm*(FW[i]-FW[i-1])
    return ac
#Bounds  1 <= X[i] <= MTU
bounds = [(1,MTU) if i < M-1 else (MTU,MTU) for i in range(0,M)]
# X[0] < X[1] < X[2] ...
#constraints = [ {'type':'ineq','fun': lambda X:X[i]-X[i-1]+1} for i in range(1,M)]
X0=[100,1500]
#Optimization Method
#method='Nelder-Mead'
method='Powell'
#Optimizing Padding
sol=minimize(averageCost,X0,method=method,bounds=bounds)
#showing Padding values
f = open("padding"+str(M)+".txt","w")
for i in range(0,M):
    lb = int(np.floor(sol.x[i-1])) if i >0 else 0
    ub = int(np.floor(sol.x[i]))
    padding = ""
    for j in range(lb+1,ub+1):
        padding = padding + str(j) + " " + str(ub) + "\n"
    f.write(padding)
    print("padding(k) = ",ub," ",lb," < k <= ",ub)
f.close()

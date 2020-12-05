#正交匹配法 参考https://zhuanlan.zhihu.com/p/52276805
import torch
import torch.nn as nn
import numpy as np
import torchvision
import time

def reconstruct_greedy(K,M,N):
    x=torch.randn((N,1))
    A=torch.randn((M,N))
    # 稀疏化
    kk=np.random.permutation(range(N))
    x[kk[0:N-K]]=0#??1-0?语法
    # 稀疏的x
    print(x)
    # 便于观测结果，仅打印非0元素
    print(x[kk[N-K:N]])
    # 压缩
    y=A@x
    # OMP算法
    r=y
    xk=0
    label=[]
    for k in range(K):
        #遍历A的原子a,计算其与r的相关度,即对r的贡献
        #maxn=np.argmax(np.array([abs(A[:,n].t()@r) for n in range(N)]))
        maxn=np.argmax(abs(A.t()@r))
        label.append(maxn)
        #计算min|y-Anewx|,计算Anew对y的贡献
        #代码？？？
        if k==0:
            Anew=A[:,maxn].reshape(A.shape[0],1)
        else:
            Anew=torch.cat([Anew,A[:,maxn].reshape(A.shape[0],1)],1)
        xk=Anew.pinverse()@y
        r=y-Anew@xk
    xx=torch.zeros(N,1)
    for i in range(len(label)):
        xx[label[i]]=xk[i]
    # zeropad=nn.ZeroPad2d(padding=(0,0,0,N-xk.shape[0]))
    # xk=zeropad(xk)
    print('原信号')
    print(x.T)
    print('重构信号信号')
    print(xx.T)


if __name__ == '__main__':
    start = time.clock()
    #K,M,N=8,50,100
    K,M,N=1000,1500,23000
    reconstruct_greedy(K,M,N)
    end = time.clock()
    print('cpu-time:'+str(end - start))

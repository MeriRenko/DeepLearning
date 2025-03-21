import numpy as np
##关于1957年古早的感知机的发明？
#感知机是具有输入和输出的算法，权重和偏置作为其参数。
#偏置可以理解为神经元被激活的难易程度
#单层感知机可以表示与门，或门和与非门等逻辑电路。
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
    
def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
    
def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
#单层感知机无法实现异或门。
#两层感知机可以实现异或门。
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y
#书中很好奇为什么说单层感知机只能表示线性空间，加上激活函数不就是可以表示非线性空间了吗
#计算机可以完全由与非门构成，多层感知机理论上可以实现计算机。
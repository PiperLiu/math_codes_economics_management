"""DAY 3 examples, stdlib only. Exact fractions except the two-column QR.
This is not a general least-squares solver. No files or network are accessed.
"""
from fractions import Fraction as F
from math import sqrt,isclose

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(a,x): return tuple(dot(row,x) for row in a)
def transpose(a): return list(zip(*a))
def mm(a,b): return [list(mv(transpose(b),row)) for row in a]
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def solve2(a,b):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if not det: raise ValueError('This example requires an invertible 2 by 2 matrix')
    return (F(b[0]*a[1][1]-a[0][1]*b[1],det),F(a[0][0]*b[1]-b[0]*a[1][0],det))
def fit2(a,b):
    at=transpose(a)
    return solve2(mm(at,a),mv(at,b))
def main():
    a=(1,1); b=(3,1); c=F(dot(a,b),dot(a,a))
    p=tuple(c*x for x in a); r=sub(b,p)
    assert p==(2,2) and dot(a,r)==0
    print('直线投影:',p,'残差:',r)
    m=[[1,0],[0,1],[1,1]]; b=(2,1,4)
    x=fit2(m,b); p=mv(m,x); r=sub(b,p)
    assert x==(F(7,3),F(4,3)) and mv(transpose(m),r)==(0,0)
    assert dot(r,r)==F(1,3)
    print('三维读数: 输入',x,'预测',p,'残差',r,'平方和',dot(r,r))
    assert fit2(m,(2,1,3))==(2,1)
    design=[[1,-1],[1,0],[1,1]]; data=(0,1,3)
    theta=fit2(design,data); residual=sub(data,mv(design,theta))
    assert theta==(F(4,3),F(3,2)) and dot(residual,residual)==F(1,6)
    shifted=fit2(design,(2,3,5))
    assert shifted==(theta[0]+2,theta[1])
    assert sub((2,3,5),mv(design,shifted))==residual
    print('轨迹: 截距与速度',theta,'残差',residual)
    a1,a2=transpose(m)
    q1=tuple(v/sqrt(dot(a1,a1)) for v in a1)
    r12=dot(q1,a2);u2=sub(a2,tuple(r12*v for v in q1))
    r22=sqrt(dot(u2,u2));q2=tuple(v/r22 for v in u2)
    q=transpose([q1,q2]);upper=[[sqrt(2),r12],[0,r22]]
    for got,want in zip(sum(mm(q,upper),[]),sum(m,[])):
        assert isclose(got,want,abs_tol=1e-12)
    assert isclose(dot(q1,q2),0,abs_tol=1e-12)
    assert isclose(dot(q1,q1),1) and isclose(dot(q2,q2),1)
    rhs=mv(transpose(q),b);x2=rhs[1]/r22;x1=(rhs[0]-r12*x2)/sqrt(2)
    assert isclose(x1,7/3) and isclose(x2,4/3)
    print('QR 回代:',(x1,x2))
    d=[[1,1],[0,0]];pseudo=[[F(1,2),0],[F(1,2),0]]
    assert mv(pseudo,(2,1))==(1,1)
    assert mm(mm(d,pseudo),d)==d and mm(mm(pseudo,d),pseudo)==pseudo
    for t in [-3,0,2]:
        candidate=(1+t,1-t)
        assert mv(d,candidate)==(2,0) and dot(candidate,candidate)==2+2*t*t
        print('相同输出的输入:',candidate,'长度平方:',dot(candidate,candidate))
    print('全部算例核对通过；通用结论的理由见正文。')
if __name__=='__main__':main()

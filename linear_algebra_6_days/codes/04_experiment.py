"""Verify explicit DAY 4 examples, Python 3.9+ stdlib, no file writes."""
from math import sqrt,pi,isclose
from pathlib import Path
import runpy

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mv(a,x):return tuple(dot(row,x) for row in a)
def mm(a,b):return [list(mv(list(zip(*b)),row)) for row in a]
def close(a,b):return all(isclose(x,y,abs_tol=1e-10) for x,y in zip(a,b))
def main():
    scene=runpy.run_path(str(Path(__file__).with_name('04_visuals.py')))
    rot=scene['rot'];data=scene['points']()
    s=[[2,1],[1,2]];b=[[1,1],[1,-1]];binv=[[.5,.5],[.5,-.5]]
    assert mv(s,(1,1))==(3,3) and mv(s,(1,-1))==(1,-1)
    assert mm(mm(b,[[3,0],[0,1]]),binv)==s
    def apply(x):
        z=rot(x,-pi/4)
        return rot((2*z[0],.5*z[1]),pi/6)
    for v,sigma,u in [(rot((1,0),pi/4),2,rot((1,0),pi/6)),(rot((0,1),pi/4),.5,rot((0,1),pi/6))]:
        assert close(apply(v),tuple(sigma*a for a in u))
        assert isclose(dot(apply(v),apply(v)),sigma*sigma)
    assert close(tuple(sum(p[j] for p in data) for j in range(2)),(0,0))
    c=[[sum(p[i]*p[j] for p in data)/7 for j in range(2)] for i in range(2)]
    assert close(c[0],(24/7,16/7)) and close(c[1],(16/7,24/7))
    q1=(1/sqrt(2),1/sqrt(2));q2=(-1/sqrt(2),1/sqrt(2))
    for q,eig,err in [(q1,40/7,8),(q2,8/7,40)]:
        assert close(mv(c,q),tuple(eig*a for a in q))
        residual=sum(sum((p[j]-dot(p,q)*q[j])**2 for j in range(2)) for p in data)
        assert isclose(residual,err)
    assert isclose((40/7)/(48/7),5/6)
    # A sample scan checks plotted variance and residual identities, not a proof of optimality.
    for k in range(101):
        q=rot((1,0),k*pi/100)
        variance=sum(dot(p,q)**2 for p in data)/7
        assert variance<=40/7+1e-10
        assert isclose(variance,dot(q,mv(c,q)))
    eps=1e-4;delta=1e-4
    assert isclose(delta/eps,1)
    print('特征对与对角化核对通过；SVD 两对方向及长度核对通过。')
    print('八点协方差:',c,'特征值:',(40/7,8/7))
    print('第一主轴保留方差:',5/6,'总重建平方误差: 8')
    print('小奇异值方向的恢复误差:',delta/eps,'；零方向在伪逆中取零。')
if __name__=='__main__':main()

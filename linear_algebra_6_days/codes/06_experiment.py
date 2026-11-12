"""Solve and check the lesson's reduced one-dimensional SDP, without packages.

This is not a general SDP solver. Optimality follows from the interval proof
in the note; the bisection independently approaches its PSD boundary.
"""
from fractions import Fraction as F
from math import sqrt

def matrix(c):
    return ((F(1),F(3,5),F(3,5)),(F(3,5),F(1),c),(F(3,5),c,F(1)))
def mv(a,x):return tuple(sum(v*w for v,w in zip(row,x)) for row in a)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def quad(a,x):return dot(x,mv(a,x))
def eigenvalues(c):
    c=float(c);delta=sqrt(c*c+F(72,25))
    return sorted((1-c,1+c/2-delta/2,1+c/2+delta/2))
def check_answers():
    """Exact arithmetic checks for the new exercise answers, not general proofs."""
    # Exercise 1: two eigenvectors identify each 2D transformation.
    cases=[(((F(1),F(0)),(F(0),F(1))),[((1,0),1),((0,1),1)]),
           (((F(8,5),F(4,5)),(F(4,5),F(2,5))),[((2,1),2),((1,-2),0)]),
           (((F(1),F(6,5)),(F(6,5),F(1))),[((1,1),F(11,5)),((1,-1),F(-1,5))])]
    for a,pairs in cases:
        for v,lam in pairs:assert mv(a,v)==tuple(lam*x for x in v)
    assert quad(((1,-1),(-1,1)),(2,3))==1
    assert quad(((1,2),(2,1)),(1,-1))==-2
    # Exercise 3: changed fixed correlations have a different feasible interval.
    for c in [F(-4,5),F(-1,2),F(0),F(1),F(6,5)]:
        a=((F(1),F(1,2),F(1,2)),(F(1,2),F(1),c),(F(1,2),c,F(1)))
        for x,y,z in [(F(-1),F(1),F(1)),(F(0),F(1),F(-1)),(F(2,3),F(1,5),F(-3,7))]:
            assert quad(a,(x,y,z))==(x+(y+z)/2)**2+(c+F(1,2))/2*(y+z)**2+(1-c)/2*(y-z)**2
    assert F(-1,2)-F(-4,5)==F(3,10)
    assert 2*F(3,10)**2==F(9,50)
    # Exercise 4: count both symmetric off-diagonal entries.
    cost=((2,0,0),(0,0,F(-3,2)),(0,F(-3,2),0));x=matrix(F(3,5))
    trace=sum(cost[i][j]*x[j][i] for i in range(3) for j in range(3))
    assert trace==2*x[0][0]-3*x[1][2]==F(1,5)
    # Exercise 5: full Frobenius squared errors for two different feasible sets.
    a=((F(1),F(6,5)),(F(6,5),F(1)))
    clipped=((F(11,10),F(11,10)),(F(11,10),F(11,10)))
    corr=((F(1),F(1)),(F(1),F(1)))
    error=lambda b:sum((b[i][j]-a[i][j])**2 for i in range(2) for j in range(2))
    assert error(clipped)==F(1,25) and error(corr)==F(2,25)
    # Exercise 7: feasible does not imply optimal.
    c,t=F(0),F(4,5)
    assert min(eigenvalues(c))>0 and abs(c+F(4,5))<=t and t>F(13,25)

def main():
    check_answers()
    observed=F(-4,5);cstar=F(-7,25);tstar=cstar-observed
    v=(F(-6,5),F(1),F(1));repaired=matrix(cstar)
    assert quad(matrix(observed),v)==F(-26,25)
    # Complete-square identity for representative inputs; general proof is in the note.
    for c in [observed,cstar,F(0),F(1),F(6,5)]:
        for x,y,z in [(F(2,3),F(-1,5),F(3,7)),v,(F(0),F(1),F(-1))]:
            square=(x+F(3,5)*(y+z))**2+(c+F(7,25))/2*(y+z)**2+(1-c)/2*(y-z)**2
            assert quad(matrix(c),(x,y,z))==square
    assert mv(repaired,v)==(0,0,0) and tstar==F(13,25)
    assert sum((repaired[i][j]-matrix(observed)[i][j])**2 for i in range(3) for j in range(3))==F(338,625)
    # The PSD crossing is bracketed here. This interval follows the lesson's construction.
    lo,hi=-.8,0.0
    assert min(eigenvalues(lo))<0<min(eigenvalues(hi))
    for _ in range(45):
        mid=(lo+hi)/2
        if min(eigenvalues(mid))<0:lo=mid
        else:hi=mid
    assert abs(hi-float(cstar))<1e-12
    w=(F(0),F(1,2),F(1,2));variance=quad(repaired,w)
    assert sum(w)==1 and all(x>=0 for x in w) and variance==F(9,25)
    for t,d in [(F(0),F(0)),(F(1,3),F(1,4)),(F(1),F(0))]:
        candidate=(t,(1-t)/2+d,(1-t)/2-d)
        assert quad(repaired,candidate)==F(9,25)+F(12,25)*t+F(4,25)*t*t+F(64,25)*d*d
    # KKT certificate for the nonnegative fusion QP.
    nu=F(-18,25);mu=(F(12,25),F(0),F(0))
    assert all(2*a+nu-b==0 for a,b in zip(mv(repaired,w),mu))
    assert all(a*b==0 for a,b in zip(w,mu)) and all(m>=0 for m in mu)
    signed=tuple(x/sum(v) for x in v)
    assert signed==(F(-3,2),F(5,4),F(5,4)) and quad(repaired,signed)==0
    print('原矩阵的负方差检验:',quad(matrix(observed),v))
    print('精确修复: c =',cstar,'; 最小改动 =',tstar)
    print('边界二分区间:',lo,hi)
    print('修复矩阵特征值:',eigenvalues(cstar))
    print('非负融合权重:',w,'; 方差:',variance)
    print('允许负权重时的零方差组合:',signed)
    print('正文与参考答案的精确算例、区间边界及融合 KKT 核对通过；不是通用 SDP 求解器。')
if __name__=='__main__':main()

"""Exact checks for DAY 5 teaching examples; stdlib only, not a QP solver."""
from fractions import Fraction as F

def mv(a,x):return tuple(sum(v*w for v,w in zip(row,x)) for row in a)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def quad(a,x):return dot(x,mv(a,x))
def main():
    h1=((1,2),(2,1));h2=((1,-1),(-1,1))
    assert quad(h1,(1,-1))==-2 and quad(h2,(1,1))==0
    # Exact identity for the PSD example is (x-y)^2; this finite check only checks arithmetic.
    for x,y in [(2,3),(-1,4),(0,0)]:assert quad(h2,(x,y))==(x-y)**2
    a=((1,0),(0,1),(1,1));h=(F(2,3),F(-1,5));ah=mv(a,h)
    gram=((2,1),(1,2));assert quad(gram,h)==dot(ah,ah)
    assert (2*1-2,2*1-2)==(0,0) # equality stationary condition with nu=-2
    for t in [F(-1),F(1),F(3,2)]:assert t*t+(2-t)**2==2*(t-1)**2+2
    sigma=((1,0,0),(0,4,0),(0,0,9));w=(F(36,49),F(9,49),F(4,49));nu=F(-72,49)
    assert sum(w)==1 and all(v>0 for v in w)
    assert all(2*v+nu==0 for v in mv(sigma,w))
    assert quad(sigma,w)==F(36,49) and dot(w,(10,12,9))==F(504,49)
    print('三传感器权重:',w,'方差:',quad(sigma,w),'本次融合值:',dot(w,(10,12,9)))
    c=((1,2),(2,9));w0=(1,0);mu=(0,2);nu=-2
    assert all(2*v+nu-m==0 for v,m in zip(mv(c,w0),mu))
    assert all(m>=0 for m in mu) and all(x*m==0 for x,m in zip(w0,mu))
    assert quad(c,w0)==1
    wu=(F(7,6),F(-1,6));assert sum(wu)==1 and quad(c,wu)==F(5,6)
    print('非负约束解:',w0,'乘子:',mu,'等式乘子:',nu)
    print('允许负权重解:',wu,'方差:',quad(c,wu))
    # A global certificate: f(w)-f(w0)=mu·(w-w0)+(w-w0)^T sigma (w-w0),
    # when 1^T w=1. sigma is PD by the completed-square identity in the lesson.
    for t in [F(0),F(1,3),F(1)]:
        w=(t,1-t);d=(t-1,1-t)
        assert quad(c,w)-1==dot(mu,d)+quad(c,d)>=0
    # Exercise answers: eigenpairs, completed squares, KKT and fusion values.
    for mat,v,lam in [(h1,(1,1),3),(h1,(1,-1),-1),(h2,(1,1),0),(h2,(1,-1),2)]:
        assert mv(mat,v)==tuple(lam*a for a in v)
    x,y=2,-1
    assert (2*x-4,4*y+4)==(0,0)
    assert x*x+2*y*y-4*x+4*y==-6
    for x,y in [(F(1,3),F(-2,5)),(2,-1),(0,0)]:
        assert x*x+2*y*y-4*x+4*y==(x-2)**2+2*(y+1)**2-6
    x,y,nu=2,2,-4
    assert x+y==4 and (2*x+nu,2*y+nu)==(0,0) and x*x+y*y==8
    for offset,mu in [(2,4),(0,0)]:
        x=0
        assert x>=0 and mu>=0 and mu*x==0 and 2*(x+offset)-mu==0
    weights=(F(9,10),F(1,10));sensor=((1,0),(0,9))
    assert sum(weights)==1 and all(v>0 for v in weights)
    assert all(2*v-F(9,5)==0 for v in mv(sensor,weights))
    assert quad(sensor,weights)==F(9,10) and dot(weights,(8,12))==F(42,5)
    for t in [F(-1),F(1,3),F(7,6)]:
        assert quad(c,(t,1-t))==6*(t-F(7,6))**2+F(5,6)
    print('全部正文与思考题精确算例、KKT 核对通过；一般证明见正文。')
if __name__=='__main__':main()

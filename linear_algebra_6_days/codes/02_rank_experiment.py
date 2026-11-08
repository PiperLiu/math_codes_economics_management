"""DAY 2: exact rank and null-direction examples, Python 3.9+ stdlib.
Inputs are small, explicitly specified rational matrices. No tolerance or file I/O.
"""
from fractions import Fraction

def rank(matrix):
    if not matrix:
        return 0
    n=len(matrix[0])
    if any(len(row)!=n for row in matrix):
        raise ValueError('Rows must have equal length')
    a=[[Fraction(v) for v in row] for row in matrix]
    r=0
    for col in range(n):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        value=a[r][col]
        a[r]=[v/value for v in a[r]]
        for i in range(r+1,len(a)):
            value=a[i][col]
            a[i]=[u-value*v for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def mv(a,x):return tuple(sum(u*v for u,v in zip(row,x)) for row in a)
def augmented(a,b):return [list(row)+[value] for row,value in zip(a,b)]

def main():
    A=[[1,0,1],[0,1,1],[0,0,0]]
    B=[[1,0,1],[0,1,1],[1,1,2]]
    x0=(2,1,0);z=(-1,-1,1)
    print('主线矩阵 A 的精确秩：',rank(A))
    print('零空间方向 z 的输出：',mv(A,z))
    for t in [-2,0,1,3]:
        x=tuple(a+t*b for a,b in zip(x0,z))
        print('t =',t,'输入',x,'输出',mv(A,x))
    print('B 的秩：',rank(B))
    print('一致读数的增广秩：',rank(augmented(B,(2,1,3))))
    print('不一致读数的增广秩：',rank(augmented(B,(2,1,4))))
    for eps in [Fraction(0),Fraction(1,1000000)]:
        E=[[1,0,0],[0,1,0],[0,0,eps]]
        print('epsilon =',eps,'精确秩 =',rank(E))
    print('epsilon = 1/1000000 时，高度恢复误差：',Fraction(1,1000000)/Fraction(1,1000000))

if __name__=='__main__':main()

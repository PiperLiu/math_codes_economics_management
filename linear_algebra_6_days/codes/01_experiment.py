"""Lesson 1 examples. Python 3.9+, standard library only, no file writes."""

def mv(a,v):
    if not a or any(len(row)!=len(v) for row in a):
        raise ValueError('matrix columns must match vector length')
    return tuple(sum(x*y for x,y in zip(row,v)) for row in a)

if __name__ == '__main__':
    A=((2,1),(0,1))
    S=((2,0),(0,1))
    R=((0,-1),(1,0))
    v=(2,1)
    print('A (2,1) =',mv(A,v))
    print('R S (1,1) =',mv(R,mv(S,(1,1))))
    print('S R (1,1) =',mv(S,mv(R,(1,1))))
    S3=((2,0,0),(0,1,0),(0,0,1))
    Rz=((0,-1,0),(1,0,0),(0,0,1))
    print('Rz S3 (1,1,1) =',mv(Rz,mv(S3,(1,1,1))))
    B=((1,1),(0,1))
    Binv=((1,-1),(0,1))
    coords=mv(Binv,(3,2))
    print('New coordinates of (3,2) =',coords)
    print('Reconstructed vector =',mv(B,coords))

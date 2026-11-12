"""Optional direct SDP model. Requires existing numpy, cvxpy and an SDP solver.

No packages are installed by this script. The lesson's standard-library
experiment is independent of this optional numerical solver demonstration.
"""
import sys

def main():
    try:
        import numpy as np
        import cvxpy as cp
    except ImportError:
        print('需要已有 NumPy、CVXPY 环境；可先运行 06_experiment.py。',file=sys.stderr)
        return 2
    solvers=cp.installed_solvers()
    solver=next((s for s in ('CLARABEL','SCS','CVXOPT') if s in solvers),None)
    if solver is None:
        print('未找到本例支持的 SDP 求解器：CLARABEL、SCS 或 CVXOPT。',file=sys.stderr)
        return 2
    c=cp.Variable(name='correlation_23');t=cp.Variable(name='change_bound')
    R=cp.bmat([[1.0,0.6,0.6],[0.6,1.0,c],[0.6,c,1.0]])
    problem=cp.Problem(cp.Minimize(t),[R >> 0,c+0.8<=t,-(c+0.8)<=t])
    try:
        problem.solve(solver=solver)
    except cp.error.SolverError as exc:
        print(f'求解失败：{exc}',file=sys.stderr)
        return 2
    print('NumPy:',np.__version__,'CVXPY:',cp.__version__,'solver:',solver)
    print('status:',problem.status)
    if problem.status not in (cp.OPTIMAL,cp.OPTIMAL_INACCURATE) or R.value is None:
        print('未获得可检查的最优候选。',file=sys.stderr)
        return 2
    X=np.asarray(R.value);cv=float(c.value);tv=float(t.value)
    if not (np.all(np.isfinite(X)) and np.isfinite(tv)):
        print('结果包含非有限数值。',file=sys.stderr)
        return 2
    sym=np.linalg.norm(X-X.T,'fro');diag=np.max(np.abs(np.diag(X)-1))
    fixed=max(abs(X[0,1]-.6),abs(X[0,2]-.6))
    eig=np.linalg.eigvalsh((X+X.T)/2)
    residual=max(0.0,abs(cv+.8)-tv)
    objective_error=abs(tv-.52)  # Known exact lower bound and attainable value for THIS example.
    print('c =',cv,'t =',tv,'\nR =\n',X)
    print('对称残差:',sym,'单位对角线残差:',diag,'固定条目残差:',fixed)
    print('特征值:',eig,'幅度约束残差:',residual,'目标对精确值误差:',objective_error)
    tol=1e-6  # For this unit-scale teaching example, not a universal acceptance rule.
    passed=max(sym,diag,fixed,max(0.0,-eig[0]),residual,objective_error)<tol
    if problem.status==cp.OPTIMAL_INACCURATE or not passed:
        print('需要进一步检查精度；未自动验收。',file=sys.stderr)
        return 1
    print('本例状态与残差检查通过。')
    return 0
if __name__=='__main__':sys.exit(main())

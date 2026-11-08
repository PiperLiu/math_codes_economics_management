# 六天重学线性代数｜空间变换、秩、特征值与凸优化

这套笔记面向学过计算规则、希望重新理解概念的学习者。案例使用几何变换、机器人定位、点云和传感器误差。每天一章，约 2.5～3 小时；目标是建立概念框架，并完成小规模优化实验，不承诺六天掌握全部理论。

## 六天路线

| 天数 | 章节标题：直观问题｜知识点 | 内容与当天产出 | 状态 |
| --- | --- | --- | --- |
| 1 | 矩阵是怎样改变空间的？｜向量、基、线性变换、矩阵乘法与换基 | 向量、基、张成、线性映射、复合、换基；画出物体变换后的样子 | [第一课](./notes/01空间与线性变换.md) · [参考答案](./notes/01空间与线性变换.md#思考题参考答案) |
| 2 | 压扁空间究竟丢掉了什么？｜秩、零空间、线性方程组与行列式 | 线性相关、列空间、零空间、秩、秩–零化度、方程解、可逆性、行列式；解释三维到平面的信息损失 | [第二课](./notes/02秩与线性方程组.md) · [参考答案](./notes/02秩与线性方程组.md#思考题参考答案) |
| 3 | 测量互相矛盾时，怎样找到最接近的解？｜正交投影、最小二乘、QR 与伪逆 | 内积、正交、投影、最小二乘、QR、伪逆；拟合机器人轨迹 | 待学习 |
| 4 | 哪些方向最特殊？｜特征值、特征向量、SVD 与 PCA | 特征值、特征向量、对角化的条件、实对称谱定理、SVD、PCA；读懂点云主轴和误差椭球 | 待学习 |
| 5 | 为什么有些二次曲面是碗，有些是马鞍？｜二次型、半正定性、凸性、KKT 与 QP | 二次型、正定/半正定、梯度、Hessian、凸性、乘子、KKT 的适用条件、凸 QP；融合传感器测量 | 待学习 |
| 6 | 如何直接优化一个矩阵？｜PSD 锥、矩阵不等式与半正定规划（SDP） | PSD 锥、矩阵不等式、标准 SDP、相关矩阵补全/修复、求解状态与残差；完成小规模 SDP 并解释数值误差 | 待学习 |

第 2、4、5 天分别集中解决秩、特征值、半正定性。每天先画图和预测，再推导与计算，最后用自己的话回答问题。第一、二课正文已编写；后四章目前只有路线，不是已经完成的教材。

## 终点先看清：凸 QP 与 SDP

对同一物理量的无偏传感器测量，设误差协方差为实对称矩阵 $\Sigma\succeq0$，融合权重为 $w\in\mathbb R^n$。非负加权融合可以写成

$$\min_w w^\top\Sigma w\quad\text{s.t.}\quad\mathbf1^\top w=1,\quad w\geq0.$$

这是凸二次规划（QP）。半正定性表示对每个方向 $z$ 都有 $z^\top\Sigma z\geq0$；它不表示每个矩阵元素非负，也不自动保证最优解唯一。

标准半正定规划（SDP）则可以写成

$$\min_{X\in\mathbb S^n}\operatorname{tr}(CX)\quad\text{s.t.}\quad\operatorname{tr}(A_iX)=b_i,\quad X\succeq0.$$

这里 $\mathbb S^n$ 是实对称矩阵空间，$C,A_i$ 为给定对称矩阵，$X$ 为未知矩阵，$\operatorname{tr}$ 是对角元素之和。目标及等式约束对 $X$ 都是线性的。含 PSD 约束但目标非线性的问题，不能不加说明就叫这个标准形式；第六天会区分原问题与等价改写。形式核对参考 [Boyd 与 Vandenberghe 教材](https://web.stanford.edu/~boyd/cvxbook/)及 [CVXPY 的 SDP 示例](https://www.cvxpy.org/examples/basic/sdp.html)。现在不用解它们，只需知道第一天的空间语言最终会用在哪里。

## 参考资源如何使用

- [3Blue1Brown：Linear transformations and matrices](https://www.3blue1brown.com/lessons/linear-transformations/)：用运动建立直觉，第一天读矩阵列向量与空间变换部分。
- [Immersive Linear Algebra，第 6 章 The Matrix](https://immersivemath.com/ila/ch06_matrices/ch06.html)：交互图辅助检查自己的空间预测。
- [MIT 18.06SC，Gilbert Strang，2011](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)：从 The Geometry of Linear Equations、Multiplication and Inverse Matrices 补上列组合及公式体系，后续选读四个子空间、投影与分解。
- [Boyd 与 Vandenberghe：Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)：第 5～6 天选读第 2～5 章相关部分，帮助区分凸集、凸函数、问题形式及最优性条件。

参考页面核对日期：2026-11-05。正文为重新组织的教学解释；数值例子、自绘图与练习为本课程设计，不复制教程图像。原始大纲和旧笔记保持原样。

## 文件与实验

- 正文：`notes/`；自绘图：`images/`；可编辑绘图源码和数值实验：`codes/`。
- 第一、二课实验仅用 Python 标准库：在本目录运行 `python3 codes/01_experiment.py` 或 `python3 codes/02_rank_experiment.py`。
- 绘图说明、环境与检查记录：[codes/README.md](./codes/README.md)。

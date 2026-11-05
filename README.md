# 数学、经济与管理：学习笔记与代码

记录数学基础、优化建模与工具实践中的概念、证明、例题和代码。按课程或专题持续补充，既保留学习过程中的思考，也逐步补充更清楚的解释与验证。

## 从这里开始

| 专题 | 内容 | 阅读入口 |
| --- | --- | --- |
| 管理数学基础 | 矩阵理论、泛函分析、凸分析、模糊数学 | [章节索引](./Foundations_of%20_Managerial%20_Mathematics/README.md) · [证明与学习方法](./Foundations_of%20_Managerial%20_Mathematics/methodology.md) |
| Gecode 中文笔记 | 约束建模、安装与运行、搜索及可视化示例 | [专题说明与索引](./gecode_MPG_notes/README.md) |

这些是持续整理的学习记录，不代表完整教材或已全面校验的教程。部分旧笔记使用图片记录题目和推导；后续补充会逐步增加可直接阅读的文字、公式与自绘示意图。

## 管理数学基础

沿用课程章节编号，当前正文位于专题的 `notes/` 目录。

- **矩阵理论**：线性变换及其矩阵表示、特征值与特征向量、相似矩阵、标准形、特征值估计与矩阵分析。
- **泛函分析**：距离空间与完备性、压缩映射与不动点、赋范空间、有界线性算子与泛函。
- **凸分析**：凸集及分离定理、Farkas 引理、凸函数、凸规划与最优性条件。
- **模糊数学**：模糊集、隶属函数、扩张原理、模糊数、模糊关系及矩阵。

具体条目见[管理数学基础目录](./Foundations_of%20_Managerial%20_Mathematics/README.md)。跨章节的证明思路与学习心得放在[方法论](./Foundations_of%20_Managerial%20_Mathematics/methodology.md)。主题目录中带空格的历史名称予以保留，命令行访问时需要加引号。

## Gecode 中文笔记

以 *Modeling and Programming with Gecode* 为主要参考，结合 C++ 例子记录工具使用与建模过程。

1. [Gecode 是什么？使用示例与笔记说明](./gecode_MPG_notes/notes/01Gecode是什么？使用示例？笔记说明.md)
2. [Gecode 安装](./gecode_MPG_notes/notes/02Gecode安装.md)
3. [Gecode 基础知识](./gecode_MPG_notes/notes/03Gecode基础知识.md)：以 `SEND + MORE = MONEY` 为例，介绍约束、分支规则、搜索与 Gist。

对应代码：[Golf 示例](./gecode_MPG_notes/codes/01example/) · [SendMoreMoney 示例](./gecode_MPG_notes/codes/03sendmoremoney/)。

现有环境说明记录的是 Windows 10、VC++ 2019 与 Gecode 6.2.0；`run.ps1` 也包含当时的本机安装路径。它们是历史实践记录，尚未在当前环境重新验证。后续运行或更新示例时，应先核对依赖版本、路径与编译方式，并记录实际验证结果。

## 文件如何组织

```text
math_codes_economics_management/
├── README.md                              # 全库入口与主题说明
├── AGENTS.md                              # 后续整理与协作约定
├── Foundations_of _Managerial _Mathematics/
│   ├── README.md                          # 课程章节索引与已有记录
│   ├── methodology.md                     # 跨章节的学习方法
│   ├── notes/                             # 章节正文
│   └── images/                            # 正文配图
└── gecode_MPG_notes/
    ├── README.md                          # 主题索引与环境说明
    ├── notes/                             # 正文
    ├── codes/                             # 按示例组织的源码与运行脚本
    ├── images/                            # 正文配图
    ├── resources/                         # 原始参考资料
    └── attach/draw.io/                     # 已有可编辑绘图及导出图
```

新增笔记放到对应主题的 `notes/`，图片放在同级 `images/`，然后补充主题 README 的索引。新增独立专题时，再更新本页入口。配图优先采用自绘 SVG，补充推导与假设数据应明确标注；具体约定见 [AGENTS.md](./AGENTS.md)。

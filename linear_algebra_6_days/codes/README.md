# 线性代数课程：实验与绘图

`01_experiment.py` 是正文算例，使用 Python 3.9+ 标准库。输入为代码中显式列出的矩阵和向量；输出为变换后的坐标，不读取外部数据。

`01_scene.py` 为本项目的可编辑场景，无随机数、无网络请求。执行 `python3 codes/01_scene.py` 会更新两张静态 SVG；`svg_frame(t)` 返回网格变换的任意一帧。SVG 包含 viewBox、标题、描述和中文字体回退。图内概念与说明使用中文，保留矩阵符号、坐标与轴名；完整图意见正文。

## GIF 生成

使用 svg-to-gif 技能的 Python → SVG → resvg → PNG → FFmpeg 管线。`RENDERER` 指向该技能的 `scripts/render_animation.py`，从本专题根目录运行：

```sh
animation_tmp=$(mktemp -d)
python3 "$RENDERER" --scene "$PWD/codes/01_scene.py" \
  --output "$animation_tmp/01-grid-transform.gif" \
  --width 800 --fps 20 --seconds 8 --colors 64 \
  --no-gifsicle
cp "$animation_tmp/01-grid-transform.gif" "$PWD/images/01-grid-transform.gif"
```

现有输出需显式追加 `--overwrite`。本例未设置体积预算，未降低尺寸、帧率或色数。GIF 为 800×500、20 fps、8 秒、无限循环、1,278,359 字节，深色不透明背景。环境为 macOS arm64、Python 3.9.6、resvg 0.48.1、FFmpeg 9.0.2；未安装或更新依赖。未验证其他操作系统。

动画生成与检查在临时目录完成，只把最终 GIF 复制到 `images/`。JSON 渲染报告、校验清单、抽帧预览及关键帧目录均不保存到项目或阅读副本。正文使用的独立 SVG 配图和 `codes/` 中的绘图源码继续保留。

## 已做的检查（2026-11-05）

- 执行数值脚本，核对六项输出与正文算例。
- 核对二维、三维列向量去向，以及换基的方向与乘法次序。
- 渲染查看三维图、二维终点图；从实际 GIF 提取起点、中间、终点和最后一帧检查布局与往返接缝。
- 起止保持恒等矩阵，接缝两侧图形一致；检查 GIF 帧延迟与循环元数据。未将静态抽帧检查当作完整实时播放测试。
- 检查新 Markdown 的本地文件链接、正文导航锚点和图片路径。

这些检查只验证本课文件和算例，不是对整套课程或原有笔记的全面审核。

## 2026-11-06 教学修订

- 为动画增加实时进度参数 `s`，正文统一使用 `A(s)` 并解释它的输入与输出。
- 新增四张中文 SVG：坐标唯一性、线性组合的两条路线、二维输入到三维输出的列含义、复合变换的列追踪。
- 绘图源码为 `01_explanation_figures.py`；从专题根目录运行 `python3 codes/01_explanation_figures.py` 可重新生成四张图，不需要第三方 Python 包。
- 对新增 SVG 渲染检查文字、箭头和边界；核对文中小算例、公式配对、图片链接和加粗间距。GIF 参数保持不变，检查实际编码抽帧及接缝；没有用抽帧检查替代实时播放测试。

## 2026-11-07：按列追踪输入贡献

新增 `01-column-contributions.svg`，根据学习者手绘中的“第一列与输入分量相连”思路重绘。上方突出第一列与 `x₁=2` 的对应，下方用同色项连接三次行乘列计算和按列汇总。绘图源码为 `01_column_contributions.py`，在专题根目录运行 `python3 codes/01_column_contributions.py` 可重新生成；只使用 Python 标准库。已用 resvg 0.48.1 渲染检查中文、公式、连线和边界，并核对两列贡献及相加结果。

## 思考题参考答案配图

`01_answer_figures.py` 生成 `01-answer-vector-paths.svg`，展示第 1 题的列向量组合与第 4 题的两种操作顺序。在专题根目录运行 `python3 codes/01_answer_figures.py` 即可重绘，仅使用 Python 标准库。图中文字与坐标已通过 resvg 渲染检查；所有箭头使用固定标准坐标，网格间隔为 1。

## 第二课：秩、零空间与线性方程组

- `02_rank_experiment.py`：使用 Python 3.9+ 标准库 `fractions.Fraction` 做小规模精确消元；输入为脚本内的有理数矩阵，无文件读写和网络请求。输出主线矩阵与增广矩阵的秩、沿零空间移动的结果，以及非零极小缩放与完全压扁的精确秩差别。它不实现浮点容差或数值秩判断。
- `02_rank_figures.py`：生成四张中文 SVG，分别展示压扁后的维数、列之间的依赖、解集合与零空间、行列式的面积意义。图中分别注明三维投影或集合示意的用途。
- 从专题根目录运行 `python3 codes/02_rank_experiment.py`；需要重绘时运行 `python3 codes/02_rank_figures.py`，会更新本课四张 SVG。
- 2026-11-07 在 macOS、Python 3.9.6 下执行实验，用现有 resvg 0.48.1 渲染并查看四张图；核对输出与手算结果、中文布局、矩阵维数、正文链接与导航。未安装新依赖，未验证其他平台。

## 消元与约束的示意图

`02_elimination_figure.py` 生成 `02-elimination-constraints.svg`，用两个显示读数及其汇总对照冗余约束与不一致约束。图为教学构造，不是实际测量数据。运行 `python3 codes/02_elimination_figure.py` 可重绘，只使用 Python 标准库。已用 resvg 渲染检查中文布局与等式。


## 第三课：投影、最小二乘、QR 与伪逆

- `03_projection_experiment.py`：使用 Python 3.9+ 标准库，核对直线投影、三维读数的最小二乘、机器人匀速轨迹拟合、两列 Gram–Schmidt QR 与最小范数输入。有理数算例使用 `Fraction`；含根号的 QR 使用浮点运算并检查容差。没有文件读写或网络访问，不是通用数值求解器。
- `03_projection_figures.py`：生成四张中文 SVG，展示垂足的最短距离、输出平面的残差截面、时间位置图与读数空间的区别、QR 的基向量分解。图中注明真实坐标图、截面示意或基内坐标的用途。
- 在专题根目录运行 `python3 codes/03_projection_experiment.py`；运行 `python3 codes/03_projection_figures.py` 会重绘本课四张 SVG。
- 2026-11-09 在 macOS 上执行实验并通过断言；使用 resvg 0.48.1 渲染查看四张 SVG，核对中文布局、图意与计算结果。未安装新依赖。


### 伪逆的三段动图

`03_pinv_scenes.py` 保存几何场景；`03_pinv_projection.py`、`03_pinv_minimum.py`、`03_pinv_mapping.py` 是三个独立渲染入口，依次展示最近可达输出、最短输入、变化读数下的伪逆映射。动画用矩阵 D=[[1,1],[0,0]]，坐标固定；每帧独立计算，不反复迭代矩阵。

用 svg-to-gif 技能提供的 `render_animation.py` 渲染，每个入口使用 `--width 1000 --fps 10 --seconds 10 --colors 48`。例如将 `--scene` 指向本目录的 `03_pinv_minimum.py`，将 `--output` 指向临时目录中的 `03-pinv-minimum.gif`，检查完成后仅将 GIF 复制到 `images/`。重新生成已有输出需显式加 `--overwrite`。场景只依赖 Python 标准库；渲染需要 resvg 与 FFmpeg。渲染器自动生成的 JSON 和检查用中间文件留在临时目录；编辑场景后应重新渲染。

2026-11-09 使用现有工具生成三个循环 GIF，保留 1000 像素宽度、10 fps、10 秒及 48 色设置，没有为压缩缩小画布。未安装可选的 gifsicle。


## 第四课：特征值、SVD 与 PCA

- `04_experiment.py` 使用 Python 3.9+ 标准库核对正文构造的特征对、对角化、SVD、样本协方差、投影方差与重建误差；不是通用分解求解器。在专题目录运行 `python3 codes/04_experiment.py`。
- `04_visuals.py` 保存六张图的几何定义；直接运行会生成 `04-boundaries.svg` 与 `04-ellipsoid.svg`。
- `04_eigen.py`、`04_signs.py`、`04_svd.py`、`04_pca.py` 为四段 GIF 的渲染入口。使用 svg-to-gif 渲染器，设置 `--width 1000 --fps 10 --seconds 10 --colors 48`。输出指定到临时目录，检查后仅将 GIF 复制到 `images/`；不保存 JSON 报告或关键帧目录到项目。
- 图中明确区分固定矩阵下更换输入、展示用插值、转动投影方向和三维平行投影。PCA 使用八个明确构造的点，样本协方差分母为 7，无真实测量数据。
- 2026-11-10 在 macOS、Python 3.9.6 下运行实验；使用现有 resvg 0.48.1 与 FFmpeg 渲染并抽查图像、端点与循环衔接。四段 GIF 均为 1000×600、10 秒、10 fps、48 色，未降低设置或安装依赖。正文静态 SVG 与源码保留，检查中间文件放在临时工作目录。


## 第五课：二次型、凸性与约束优化

- `05_experiment.py` 使用 Python 3.9+ 标准库及 `Fraction` 核对二次型、等式约束解、传感器融合权重、边界 KKT 乘子及目标值。运行 `python3 codes/05_experiment.py`；它不是通用 QP 求解器，不安装求解器依赖。
- `05_visuals.py` 保存五张图的定义，直接运行生成曲面及权重两张 SVG。`05_directions.py`、`05_chord.py`、`05_constraint.py` 是三个 GIF 入口，分别展示方向截面、凸函数弦不等式、约束直线上的候选点。
- 使用 svg-to-gif 渲染器，设置 `--width 1000 --fps 10 --seconds 10 --colors 48`。输出到临时目录，检查后只复制 GIF 到 `images/`；不交付 JSON、关键帧或抽帧预览。
- 2026-11-11 在 macOS、Python 3.9.6 下运行精确算例；用现有 resvg 0.48.1 与 FFmpeg 渲染、检查静态图及 GIF 代表帧和循环衔接。GIF 为 1000×600、10 秒、10 fps，未缩减设置。所有数值及曲面均为教学构造。

第五课参考答案补充后，实验还核对两组特征对、配方后的最低值、等式与边界乘子，以及双传感器融合权重与读数；有限算例只检查计算，存在性与凸性结论的推导保留在正文。


## 第六课：半正定规划与综合实践

- `06_experiment.py` 使用 Python 3.9+ 标准库，以 `Fraction` 核对平方配方、非法相关矩阵、精确修复值、误差大小及后续融合的 KKT；二分搜索逼近本例一维 PSD 边界，不是通用 SDP 求解器。运行 `python3 codes/06_experiment.py`。
- `06_sdp_cvxpy.py` 是同一问题的可选直接建模版本，需已有 NumPy、CVXPY 及 CLARABEL、SCS 或 CVXOPT 之一；检查状态、对称性、单位对角线、固定条目、最小特征值、幅度约束与已知最优值。本次只检查语法，未安装依赖或运行该求解器示例。
- `06_visuals.py` 保存六幅图的定义，直接运行生成 `06-cone.svg`、`06-repair-choices.svg`、`06-roadmap.svg`。`06_slice.py`、`06_gram.py`、`06_repair.py` 为三个 GIF 渲染入口。
- 使用 svg-to-gif 渲染器，设置 `--width 1000 --fps 10 --seconds 10 --colors 48`。输出到临时目录，检查后仅将 GIF 复制到 `images/`；不交付 JSON、关键帧或抽帧预览。三维图采用有明确公式的平行投影；修复插值不是求解器轨迹。
- 2026-11-12 在 macOS、Python 3.9.6 下运行标准库实验；用现有 resvg 0.48.1 与 FFmpeg 渲染并检查静态图、GIF 代表帧与循环衔接。GIF 为 1000×600、10 秒、10 fps、48 色，未缩减设置或安装依赖。

第六课参考答案补充后，标准库实验进一步核对三个二阶矩阵的特征对、修改后的相关系数区间、迹的非对角系数、两种修复距离及“可行但非最优”的反例。一般结论的证明与适用条件仍以正文推导为准。

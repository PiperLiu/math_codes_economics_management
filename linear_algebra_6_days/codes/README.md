# 线性代数课程：实验与绘图

`01_experiment.py` 是正文算例，使用 Python 3.9+ 标准库。输入为代码中显式列出的矩阵和向量；输出为变换后的坐标，不读取外部数据。

`01_scene.py` 为本项目的可编辑场景，无随机数、无网络请求。执行 `python3 codes/01_scene.py` 会更新两张静态 SVG；`svg_frame(t)` 返回网格变换的任意一帧。SVG 包含 viewBox、标题、描述和中文字体回退。图内概念与说明使用中文，保留矩阵符号、坐标与轴名；完整图意见正文。

## GIF 生成

使用 svg-to-gif 技能的 Python → SVG → resvg → PNG → FFmpeg 管线。`RENDERER` 指向该技能的 `scripts/render_animation.py`，从本专题根目录运行：

```sh
python3 "$RENDERER" --scene "$PWD/codes/01_scene.py" \
  --output "$PWD/images/01-grid-transform.gif" \
  --width 800 --fps 20 --seconds 8 --colors 64 \
  --no-gifsicle --keep-keyframes
```

现有输出需显式追加 `--overwrite`。本例未设置体积预算，未降低尺寸、帧率或色数。GIF 为 800×500、20 fps、8 秒、无限循环、1,278,359 字节，深色不透明背景。环境为 macOS arm64、Python 3.9.6、resvg 0.48.1、FFmpeg 9.0.2；未安装或更新依赖。未验证其他操作系统。

[渲染报告](../images/01-grid-transform.gif.json)保存生成时工具身份、源码散列、参数和编码结果；其中路径记录的是当时的生成位置。报告不是跨机器的路径配置，重新生成时使用上述相对项目路径。四张可编辑关键帧在 `images/01-grid-transform.gif.keyframes/`。

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

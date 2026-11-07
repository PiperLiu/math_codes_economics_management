"""Column contributions to Mx, based on the learner's sketch. Standard library only."""
from pathlib import Path
from html import escape
BLUE='#71c9ff';CORAL='#ff8d83';TEXT='#e6edf4';MUTED='#a7bacb';GOLD='#f8d174'
def text(x,y,value,color=TEXT,size=23):
 return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{escape(str(value))}</text>'
def rect(x,y,w,h,color,opacity=.1):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" fill-opacity="{opacity}" stroke="{color}" stroke-width="2"/>'
def bracket(x,y,w,h):
 return f'<path d="M{x+10},{y} h-10 v{h} h10 M{x+w-10},{y} h10 v{h} h-10" stroke="{MUTED}" stroke-width="2" fill="none"/>'
def figure():
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="790" viewBox="0 0 1100 790"><title>矩阵乘向量：逐行求结果，按列看贡献</title><desc>输入 x=(2,1)，矩阵 M 的第一列为 (1,0,1)。蓝色连线将 x1=2 与第一列相连；下方三行展开式中，蓝色项分别为 1×2、0×2、1×2，展示 x1 对三个输出维度的贡献 (2,0,2)。第二列按 x2=1 加权后贡献 (0,1,1)，两者相加为 (2,1,3)。</desc><rect width="1100" height="790" fill="#101d2b"/><defs><marker id="tip" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10" fill="#71c9ff"/></marker></defs><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(30,43,'矩阵乘向量：逐行求结果，按列看贡献',size=29),text(30,80,'第一列的三个系数，分别记录同一个输入 x₁ 对三个输出维度的作用。',MUTED,22)]
 s += [text(25,267,'Mx =',size=28),bracket(115,178,150,155),rect(134,185,47,140,BLUE),rect(214,185,38,140,CORAL,.06)]
 for row,(a,b) in enumerate([(1,0),(0,1),(1,1)]):
  y=216+47*row;s += [text(146,y,a,BLUE,29),text(221,y,b,CORAL,29)]
 s += [text(297,266,'×',size=30),bracket(355,204,100,101),rect(375,210,60,40,BLUE),text(390,241,2,BLUE,29),text(390,289,1,CORAL,29),text(485,266,'=',size=30),bracket(552,178,70,155)]
 for i,val in enumerate([2,1,3]):s.append(text(575,216+i*47,val,GOLD,29))
 s += [text(350,355,'输入 x',MUTED,20),text(540,355,'输出 y = Mx',MUTED,20),text(130,355,'第一列',BLUE,19),text(210,355,'第二列',CORAL,19),'<path d="M157,182 C157,115 404,115 404,201" fill="none" stroke="#71c9ff" stroke-width="3" marker-end="url(#tip)"/>',text(210,130,'x₁ = 2 乘遍这一列',BLUE,21),text(700,215,'第一列：(1, 0, 1)',BLUE,23),text(700,258,'乘上 x₁ = 2',BLUE,23),text(700,301,'贡献：(2, 0, 2)',BLUE,25)]
 s += ['<path d="M30 390 H1070" stroke="#32475b"/>',text(40,434,'逐行计算',size=23),text(285,434,'来自 x₁ 的贡献',BLUE,23),text(585,434,'来自 x₂ 的贡献',CORAL,23),text(925,434,'输出',GOLD,23),rect(265,454,260,178,BLUE),rect(565,454,260,178,CORAL,.06)]
 for i,(a,b,result) in enumerate([(1,0,2),(0,1,1),(1,1,3)]):
  y=494+54*i
  s += [text(60,y,['y₁ =','y₂ =','y₃ ='][i],size=27),text(295,y,f'{a} × 2',BLUE,28),text(537,y,'+',size=25),text(595,y,f'{b} × 1',CORAL,28),text(850,y,'=',MUTED,26),text(945,y,result,GOLD,29)]
 s += [text(40,679,'按列汇总',size=23),text(265,679,'(2, 0, 2)',BLUE,25),text(537,679,'+',size=25),text(595,679,'(0, 1, 1)',CORAL,25),text(850,679,'=',size=25),text(925,679,'(2, 1, 3)',GOLD,25),text(40,733,'一行回答“这个输出怎么算”；一列回答“这个输入影响哪些输出、各贡献多少”。',MUTED,22),text(40,768,'本例第一列的第二个系数是 0，因此 x₁ 对第二个输出的贡献为 0。',MUTED,20),'</g></svg>']
 return ''.join(s)
if __name__=='__main__':
 out=Path(__file__).resolve().parents[1]/'images/01-column-contributions.svg'
 out.write_text(figure(),encoding='utf-8')

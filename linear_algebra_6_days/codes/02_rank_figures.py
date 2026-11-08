"""DAY 2 concept figures. Python 3.9+, standard library, no external inputs."""
from pathlib import Path
from html import escape
import math
OUT=Path(__file__).resolve().parents[1]/'images'
BLUE='#71c9ff';RED='#ff8d83';GOLD='#f8d174';GREEN='#99dfb0';GRAY='#a7bacb'
def txt(x,y,s,c='#e6edf4',size=21):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(s)}</text>'
def line(a,b,c=GRAY,w=2,dash=''):return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{c}" stroke-width="{w}" stroke-dasharray="{dash}"/>'
def arrow(a,b,c=GOLD,w=3):
 ang=math.atan2(b[1]-a[1],b[0]-a[0]); pts=[b]+[(b[0]-11*math.cos(ang+d),b[1]-11*math.sin(ang+d)) for d in [-.4,.4]]
 return line(a,b,c,w)+poly(pts,c)
def poly(pts,c,opacity=1):return f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{c}" fill-opacity="{opacity}"/>'
def start(title,sub,h=520):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{h}" viewBox="0 0 1100 {h}"><title>{escape(title)}</title><desc>{escape(sub)}</desc><rect width="1100" height="{h}" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',txt(30,42,title,size=28),txt(30,78,sub,GRAY,19)]
def save(name,s): (OUT/name).write_text(''.join(s)+'</g></svg>',encoding='utf-8')
def dot(p,c=GOLD):return f'<circle cx="{p[0]}" cy="{p[1]}" r="6" fill="{c}"/>'
def collapse():
 s=start('秩：输出还保留多少个独立方向','三幅图采用相同的三维平行投影；虚线为原始单位立方体。')
 verts=[(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
 edges=[(a,b) for i,a in enumerate(verts) for b in verts[i+1:] if sum(x!=y for x,y in zip(a,b))==1]
 for ox,rank,title in [(190,3,'原样保留'),(550,2,'抹去高度'),(910,1,'只保留第一坐标')]:
  def p(v):x,y,z=v;return ox+95*x-65*y,340-30*x-40*y-120*z
  def t(v):return (v[0],v[1] if rank>=2 else 0,v[2] if rank==3 else 0)
  s.append(txt(ox-115,128,title,size=23))
  for a,b in edges:s.append(line(p(a),p(b),'#52687c',1,'5 5'))
  if rank==2:s.append(poly([p(t(v)) for v in [(0,0,0),(1,0,0),(1,1,0),(0,1,0)]],BLUE,.15))
  for a,b in edges:
   if t(a)!=t(b):s.append(line(p(t(a)),p(t(b)),BLUE,3))
  for v,c in [((1,0,0),RED),((0,1,0),BLUE),((0,0,1),GREEN)]:
   if t(v)!=(0,0,0):s.append(arrow(p((0,0,0)),p(t(v)),c,4))
  s.extend([txt(ox-75,408,f'秩 = {rank}',GOLD,26),txt(ox-118,448,{3:'体积、面积与长度都可存在',2:'仍有面积，三维体积为零',1:'仍有长度，面积与体积为零'}[rank],GRAY,18)])
 s.append(txt(30,493,'秩描述所有可能输出的维数；图中有限物体只是帮助观察的样本。',GRAY,20))
 save('02-rank-collapse.svg',s)
def column_space():
 s=start('三个非零列，可以只张成一个平面','主线矩阵 A 的三列：a₁ = (1,0,0)，a₂ = (0,1,0)，a₃ = (1,1,0)。')
 def p(x,y,z=0):return 300+130*x-75*y,380-30*x-65*y-100*z
 s.append(poly([p(-.8,-.5),p(2,-.5),p(2,2),p(-.8,2)],BLUE,.12))
 for v,name in [((2,0,0),'y₁'),((0,2,0),'y₂'),((0,0,2.5),'y₃')]:s.extend([arrow(p(0,0),p(*v),GRAY,1),txt(p(*v)[0]+7,p(*v)[1],name,GRAY,19)])
 for v,name,c in [((1,0,0),'a₁',RED),((0,1,0),'a₂',BLUE),((1,1,0),'a₃',GOLD)]:s.extend([arrow(p(0,0),p(*v),c,4),txt(p(*v)[0]+10,p(*v)[1]-12,name,c,23)])
 s.extend([line(p(1,0),p(1,1),BLUE,2,'5 5'),line(p(0,1),p(1,1),RED,2,'5 5'),txt(640,175,'a₃ = a₁ + a₂',GOLD,29),txt(640,229,'第三列没有增加独立方向。',size=23),txt(640,284,'列空间：全部 (p,q,0)',size=23),txt(640,329,'一组基：a₁、a₂',size=23),txt(640,374,'秩：2',GOLD,26),txt(30,483,'浅蓝色区域表示输出平面的一部分；列空间本身无限延伸。',GRAY,20)])
 save('02-column-space.svg',s)
def fibers():
 s=start('零空间解释重合；列空间决定可达','集合关系示意，非三维坐标投影。z₀ = (−1,−1,1)，x₀ = (2,1,0)。',580)
 s.extend([txt(55,135,'输入空间',size=24),txt(700,135,'输出空间',size=24)])
 for y,c,label in [(260,BLUE,'零空间：t z₀'),(420,GOLD,'全部解：x₀ + t z₀')]:
  s.append(line((65,y+35),(430,y-60),c,3))
  for x in [140,240,340]:s.append(dot((x,y+35-(x-65)*95/365),c))
  s.extend([txt(60,y-83,label,c,22),arrow((445,y-15),(690,y-15),c),txt(520,y-30,'作用 A',c,18)])
 s.append(poly([(710,205),(1025,205),(1060,480),(745,480)],BLUE,.1))
 s.extend([dot((790,245),BLUE),txt(809,250,'0',BLUE,24),dot((790,405),GOLD),txt(809,410,'b = (2,1,0)',GOLD,22),txt(765,465,'列空间：y₃ = 0',GRAY,20),dot((970,165),RED),txt(720,181,'不可达：b′ = (2,1,1)',RED,20),txt(50,541,'沿同一条输入直线移动，输出不变；两条平行直线可对应不同输出。',GRAY,22)])
 save('02-solution-fibers.svg',s)
def determinant():
 s=start('行列式：单位面积经过变换后的有向倍率','二维例子；三个面板的坐标单位相同。',530)
 for ox,kind,title in [(85,0,'单位正方形'),(420,1,'拉伸与错切'),(790,2,'压到直线')]:
  def p(x,y):return ox+65*x,340-65*y
  if kind==0:verts=[(0,0),(1,0),(1,1),(0,1)]
  elif kind==1:verts=[(0,0),(2,0),(3,1),(1,1)]
  else:verts=[(0,0),(1,0),(3,0),(2,0)]
  s.extend([txt(ox-10,135,title,size=24),arrow(p(-.3,0),p(3.5,0),GRAY,1),arrow(p(0,-.3),p(0,2.4),GRAY,1)])
  pts=[p(*v) for v in verts];s.append(poly(pts,BLUE,.2))
  for a,b in zip(pts,pts[1:]+pts[:1]):s.append(line(a,b,BLUE,3))
  s.extend([arrow(p(0,0),pts[1],RED,4),arrow(p(0,0),pts[3],GOLD,3),txt(ox-10,405,['面积 1；det = 1','面积 2；det = 2','面积 0；det = 0'][kind],size=21),txt(ox-10,448,['两列独立','两列仍独立','两列线性相关'][kind],GRAY,21)])
 s.append(txt(30,499,'红、黄箭头是矩阵的两列；沿两列围出的平行四边形决定面积倍率。',GRAY,20))
 save('02-determinant-area.svg',s)
if __name__=='__main__':collapse();column_space();fibers();determinant()

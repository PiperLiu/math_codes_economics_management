"""Reference-answer vector diagrams; Python 3.9+ standard library only."""
from pathlib import Path
from html import escape
import math
RED='#ff8d83';BLUE='#71c9ff';GOLD='#f8d174';GRAY='#a7bacb'
def text(x,y,v,c='#e6edf4',size=19):
 return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(v)}</text>'
def line(a,b,c,w=1):
 return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{c}" stroke-width="{w}"/>'
def arrow(a,b,c,w=3):
 angle=math.atan2(b[1]-a[1],b[0]-a[0]); pts=[b]+[(b[0]-10*math.cos(angle+d),b[1]-10*math.sin(angle+d)) for d in [-.45,.45]]
 return line(a,b,c,w)+f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{c}"/>'
def scene():
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="1140" height="590" viewBox="0 0 1140 590"><title>第一题列向量组合与第四题操作顺序</title><desc>左侧从原点走两份第一列到 (2,2)，再走一份第二列到 (1,3)。中间先拉伸再旋转，终点为 (-1,2)；右侧先旋转再拉伸，终点为 (-2,1)。所有网格单位均为一。</desc><rect width="1140" height="590" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(30,42,'参考答案：列向量的组合与操作顺序',size=27),text(30,77,'三幅图均使用固定标准坐标系，每格 1 个单位。',GRAY,20)]
 def plot(ox):
  def p(x,y):return ox+50*x,340-50*y
  for x in range(-2,4):s.append(line(p(x,-1),p(x,4),'#293c50'))
  for y in range(-1,5):s.append(line(p(-2,y),p(3,y),'#293c50'))
  s.extend([arrow(p(-2,0),p(3.2,0),GRAY,1),arrow(p(0,-1),p(0,4.2),GRAY,1),text(ox-18,362,'0',GRAY,16),text(ox+163,345,'x',GRAY,16),text(ox+9,130,'y',GRAY,16)])
  return p
 p=plot(150)
 s.extend([text(30,114,'第 1 题：按列组合'),arrow(p(0,0),p(2,2),RED),arrow(p(2,2),p(1,3),BLUE),arrow(p(0,0),p(1,3),GOLD),text(255,245,'(2,2)',RED,18),text(205,179,'(1,3)',GOLD,18),text(30,439,'红：两份第一列，到 (2,2)',RED),text(30,473,'蓝：再加一份第二列',BLUE),text(30,507,'黄：总位移 (1,3)',GOLD)])
 for ox,title,mid,end,steps in [(555,'第 4 题：先 S，后 R',(2,1),(-1,2),['(1,1) → (2,1) → (−1,2)']),(955,'第 4 题：先 R，后 S',(-1,1),(-2,1),['(1,1) → (−1,1) → (−2,1)'])]:
  p=plot(ox)
  s.append(text(ox-145,114,title))
  for v,c in [((1,1),BLUE),(mid,RED),(end,GOLD)]:s.append(arrow(p(0,0),p(*v),c))
  s.extend([text(ox+55,285,'(1,1)',BLUE,18),text(p(*mid)[0]+4,p(*mid)[1]-12,str(mid),RED,18),text(p(*end)[0]-36,p(*end)[1]-32,str(end),GOLD,18),text(ox-145,439,'蓝：原向量；红：第一步后',GRAY,18),text(ox-145,473,'黄：最终向量',GOLD),text(ox-145,507,steps[0],size=19)])
 s.extend([text(30,563,'左图的两段位移首尾相加；中、右图的箭头是不同阶段的状态，不作相加。',GRAY,21),'</g></svg>'])
 return ''.join(s)
if __name__=='__main__':
 (Path(__file__).resolve().parents[1]/'images/01-answer-vector-paths.svg').write_text(scene(),encoding='utf-8')

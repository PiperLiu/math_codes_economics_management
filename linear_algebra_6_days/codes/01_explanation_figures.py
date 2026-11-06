"""Editable lesson diagrams. Python 3.9+ standard library; deterministic SVG."""
from pathlib import Path
from html import escape
import math
OUT=Path(__file__).resolve().parents[1]/'images'
RED='#ff8d83';BLUE='#71c9ff';GOLD='#f8d174';MUTED='#a7bacb'
def text(x,y,s,color='#e6edf4',size=21):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{escape(s)}</text>'
def line(a,b,color=MUTED,w=2,dash=''):
    return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="{w}" stroke-dasharray="{dash}"/>'
def arrow(a,b,color=GOLD,w=3):
    ang=math.atan2(b[1]-a[1],b[0]-a[0]); pts=[b]+[(b[0]-12*math.cos(ang+d),b[1]-12*math.sin(ang+d)) for d in (-.4,.4)]
    return line(a,b,color,w)+f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{color}"/>'
def start(title,subtitle,h=570):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{h}" viewBox="0 0 1100 {h}"><title>{escape(title)}</title><desc>{escape(subtitle)}</desc><rect width="1100" height="{h}" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(30,42,title,size=27),text(30,78,subtitle,MUTED,18)]
def save(name,items):
    (OUT/name).write_text(''.join(items)+ '</g></svg>',encoding='utf-8')
def plot(items,ox,oy,scale=60,xmax=4.8,ymax=3):
    def p(x,y): return (ox+scale*x,oy-scale*y)
    for i in range(int(xmax)+1):items.append(line(p(i,0),p(i,ymax),'#293c50',1))
    for i in range(int(ymax)+1):items.append(line(p(0,i),p(xmax,i),'#293c50',1))
    items.extend([arrow(p(0,0),p(xmax,0),MUTED,1),arrow(p(0,0),p(0,ymax),MUTED,1),text(ox-20,oy+25,'0',MUTED,17)])
    return p

def uniqueness():
    s=start('坐标唯一性：系数相加为零，不等于向量相加为零','左图：两个独立方向不能用一加一减抵消。右图：重复的方向才可以。')
    s.extend([text(45,125,'独立方向：b₁ = (1,0)，b₂ = (0,1)'),text(610,125,'重复方向：b₁ = b₂ = (1,0)')])
    p=plot(s,65,380)
    s.extend([arrow(p(0,0),p(3,0),RED),arrow(p(3,0),p(3,2),BLUE),text(210,240,'(3,2)',GOLD),arrow(p(3,2),p(4,2),RED),arrow(p(4,2),p(4,1),BLUE),text(320,325,'(4,1)',GOLD),text(90,420,'多一份 b₁，少一份 b₂：终点变了',size=19)])
    # Two displaced parallel routes demonstrate equal opposite vector cancellation.
    a=(650,260); b=(850,260)
    s.extend([arrow(a,b,RED),text(710,235,'+b₁',RED),arrow((850,300),(650,300),BLUE),text(710,335,'−b₂',BLUE),text(635,380,'同方向、等长度，反向后才抵消',size=19),text(45,475,'1b₁ − 1b₂ = (1,−1) ≠ 零向量',GOLD,23),text(610,475,'1b₁ − 1b₂ = 零向量',GOLD,23),text(30,535,'基要求线性无关：要组合出零向量，每一个系数都必须为零。',MUTED)])
    save('01-unique-coordinates.svg',s)

def linearity():
    s=start('线性：两条计算路线，到达同一个终点','例：T(x,y) = (2x+y,y)。红色第一段，蓝色第二段，黄色表示总位移。',610)
    p=plot(s,80,345,65,2.5,2.5)
    s.extend([text(55,130,'原空间：u + v = (1,1)'),arrow(p(0,0),p(1,0),RED),arrow(p(1,0),p(1,1),BLUE),arrow(p(0,0),p(1,1),GOLD),text(100,375,'u = (1,0)',RED,18),text(155,270,'v = (0,1)',BLUE,18)])
    q=plot(s,650,345,90,4,2)
    s.extend([text(630,130,'变换后：T(u) + T(v) = (3,1)'),arrow(q(0,0),q(2,0),RED),arrow(q(2,0),q(3,1),BLUE),arrow(q(0,0),q(3,1),GOLD),text(690,375,'T(u) = (2,0)',RED,18),text(885,240,'T(v) = (1,1)',BLUE,18),arrow((340,255),(595,255),MUTED),text(350,225,'把整个位移变换 T',MUTED,18)])
    s.extend([text(40,450,'路线一：先相加，再变换',size=22),text(390,450,'T(u + v) = T(1,1) = (3,1)',GOLD,22),text(40,495,'路线二：先分别变换，再相加',size=22),text(390,495,'T(u) + T(v) = (2,0) + (1,1) = (3,1)',GOLD,22),text(40,565,'配方保持不变；箭头的长度、夹角和图形的面积可以改变。',MUTED)])
    save('01-linearity.svg',s)

def columns():
    s=start('三行两列：两种输入基本动作，各有三个输出坐标','M 的第一列是第一支输入基向量的去向，第二列是第二支的去向。',670)
    p=plot(s,70,325,75,2,2)
    s.extend([text(45,125,'二维输入：两个坐标'),arrow(p(0,0),p(1,0),RED),arrow(p(0,0),p(0,1),BLUE),text(145,350,'e₁',RED),text(85,245,'e₂',BLUE)])
    # matrix as an explicit table, using matching column colors
    s.extend([text(350,145,'M：3 行 × 2 列'),text(330,260,'M =',size=26)])
    for j,vals in enumerate([(1,0,1),(0,1,1)]):
        x=420+75*j
        s.append(f'<rect x="{x-16}" y="183" width="60" height="156" rx="12" fill="{RED if j==0 else BLUE}" opacity=".13"/>')
        for i,val in enumerate(vals):s.append(text(x,218+48*i,str(val),RED if j==0 else BLUE,28))
    s.extend([text(415,372,'第 1 列',RED,17),text(493,372,'第 2 列',BLUE,17),arrow((265,255),(320,255),MUTED),arrow((560,255),(630,255),MUTED),text(710,125,'三维输出：每列三个坐标')])
    def q(x,y,z):return (820+90*x-65*y,370-30*x-35*y-100*z)
    for v,name in [((1.8,0,0),'x'),((0,1.8,0),'y'),((0,0,1.8),'z')]:
        s.extend([arrow(q(0,0,0),q(*v),MUTED,1),text(q(*v)[0]+5,q(*v)[1],name,MUTED,18)])
    s.extend([arrow(q(0,0,0),q(1,0,1),RED),arrow(q(0,0,0),q(0,1,1),BLUE),text(920,240,'(1,0,1)',RED,19),text(650,240,'(0,1,1)',BLUE,19),text(35,470,'第一列：M e₁ = (1,0,1)；第二列：M e₂ = (0,1,1)。',size=23),text(35,520,'输入 (2,1)：取两份第一列，加一份第二列。',size=23),text(35,565,'M (2,1) = 2(1,0,1) + 1(0,1,1) = (2,1,3)',GOLD,25),text(35,630,'右侧采用二维平行投影展示三维箭头；图中长度与夹角仅作示意。',MUTED,19)])
    save('01-columns-dimensions.svg',s)

def composition():
    s=start('乘积的每一列：追踪同一支基向量，连续经过两次变换','S：横向放大两倍；R：逆时针旋转 90°。右边的 S 先作用。',620)
    for x,label in [(50,'输入基向量'),(365,'先经过 S'),(680,'再经过 R')]:s.append(text(x,140,label,size=24))
    for y,values,col in [(230,['e₁ = (1,0)','S e₁ = (2,0)','R(S e₁) = (0,2)'],RED),(350,['e₂ = (0,1)','S e₂ = (0,1)','R(S e₂) = (−1,0)'],BLUE)]:
        for x,lab in zip([50,365,680],values):s.append(text(x,y,lab,col,24))
        s.extend([arrow((245,y-8),(340,y-8),col),arrow((575,y-8),(655,y-8),col)])
    s.extend([text(50,440,'把两个最终坐标按原顺序排成列：',size=23),text(585,465,'RS =',size=26),text(700,440,'0',RED,28),text(770,440,'−1',BLUE,28),text(700,487,'2',RED,28),text(785,487,'0',BLUE,28),line((680,410),(680,505)),line((830,410),(830,505)),line((680,410),(690,410)),line((680,505),(690,505)),line((820,410),(830,410)),line((820,505),(830,505)),text(50,560,'一般规则：AB 的第 j 列 = A(B eⱼ) = A × B 的第 j 列。',GOLD,23)])
    save('01-composition-columns.svg',s)

if __name__=='__main__':
    uniqueness();linearity();columns();composition()

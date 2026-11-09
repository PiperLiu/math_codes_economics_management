"""Deterministic SVG scenes for three pseudoinverse teaching loops."""
from math import cos,sin,pi
from html import escape
B='#71c9ff';G='#f8d174';R='#ff8d83';W='#e6edf4';S='#a7bacb'
def text(x,y,s,c=W,size=23):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(s)}</text>'
def line(p,q,c=S,dash=False,width=3):return f'<path d="M{p[0]},{p[1]} L{q[0]},{q[1]}" stroke="{c}" stroke-width="{width}" fill="none"'+(' stroke-dasharray="7 6"' if dash else '')+'/>'
def dot(p,c):return f'<circle cx="{p[0]}" cy="{p[1]}" r="6" fill="{c}"/>'
def xy(x,y,right=False):return (125+520*right+70*x,390-70*y)
def axes(s,right=False,input=False):
 for k in range(-1,5):
  s.append(line(xy(k,-1,right),xy(k,3,right),'#20394d',width=1))
 for k in range(-1,4):s.append(line(xy(-1,k,right),xy(4,k,right),'#20394d',width=1))
 s.extend([line(xy(-1,0,right),xy(4,0,right)),line(xy(0,-1,right),xy(0,3,right)),text(410+520*right,415,'x₁' if input else 'y₁',S,20),text(95+520*right,165,'x₂' if input else 'y₂',S,20)])
 for k in [0,1,2,3]:s.append(text(119+520*right+70*k,414,str(k),S,16))
def begin(title,desc):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="570" viewBox="0 0 1000 570"><title>{escape(title)}</title><desc>{escape(desc)}</desc><rect width="1000" height="570" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(28,40,title,size=28)]
def end(s):return ''.join(s)+'</g></svg>'
def travel(t):
 # Pauses at a distant candidate and at the minimum; seam is stationary.
 knots=[(0,-1.4),(.12,-1.4),(.35,0),(.53,0),(.74,1.4),(.82,1.4),(1,-1.4)]
 for (a,x),(b,y) in zip(knots,knots[1:]):
  if a<=t<=b:return x+(y-x)*(1-cos(pi*(t-a)/(b-a)))/2
 return -1.4

def projection(t):
 u=travel(t);q=(2+u,0);b=(2,1)
 s=begin('① 先选输出：哪一个可达点离读数最近？','D(x1,x2)=(x1+x2,0)。固定读数 b=(2,1)，候选输出沿横轴往返；距离在 p=(2,0) 处最小。')
 s.extend([text(28,83,'固定读数 b = (2,1)；蓝色横轴是 D 的全部可达输出。',S),text(40,131,'输出空间',B)])
 axes(s)
 s.extend([line(xy(-1,0),xy(4,0),B,width=4),line(xy(*q),xy(*b),R),line(xy(2,0),xy(*b),S,True),dot(xy(*b),R),dot(xy(2,0),B),dot(xy(*q),G),text(280,305,'b = (2,1)',R),text(250,445,'p = (2,0)',B),text(560,170,'金点 q：正在比较的候选输出',G),text(560,230,f'q = ({q[0]:.2f}, 0)'),text(560,290,f'距离平方 = 1 + (q₁ − 2)² = {1+u*u:.2f}',R),text(560,355,'最小值为 1，在 q = p 时取得。',B),text(560,420,'原读数不在横轴上，不能精确到达。'),text(28,505,'这一步只在输出空间选点，还没有决定用哪一份输入产生 p。',G),text(28,546,'固定坐标；往返只用于比较候选点，不是反复应用矩阵。',S,20)])
 return end(s)
def minimum(t):
 u=travel(t);x=(1+u,1-u)
 s=begin('② 再选输入：同样好的输出，选最短的来源','输入解直线 x1+x2=2 上的候选点全部映到右侧 p=(2,0)。从原点到候选输入的长度在 x=(1,1) 时最短。')
 s.extend([text(28,83,'输入 x = (1+t, 1−t)；改变 t，输出始终是 (2,0)。',S),text(40,131,'输入空间：比较输入长度',B),text(560,131,'输出空间：预测保持不变',B)])
 axes(s,input=True);axes(s,right=True)
 s.extend([line(xy(-.8,2.8),xy(2.8,-.8),B,width=4),line(xy(0,0),xy(*x),G,width=4),dot(xy(1,1),B),dot(xy(*x),G),text(225,240,'最短点 (1,1)',B,20),text(445,275,'D →',W,24),line(xy(-1,0,True),xy(4,0,True),B,width=4),dot(xy(2,0,True),G),dot(xy(2,1,True),R),line(xy(2,0,True),xy(2,1,True),R),text(805,312,'b',R),text(805,379,'p',G),text(40,490,f't = {u:.2f}；长度平方 = 2 + 2t² = {2+2*u*u:.2f}',G),text(560,490,'残差平方始终等于 1。',R),text(28,546,'蓝斜线上的输入都最小化残差；只有 (1,1) 同时具有最小输入长度。',S,20)])
 return end(s)
def mapping(t):
 b=(2+cos(2*pi*t),sin(2*pi*t));p=(b[0],0);x=(b[0]/2,b[0]/2)
 s=begin('③ 合起来看：D⁺ 把每份读数送到最短输入','读数 b 在输出空间中绕圈。每帧独立计算 p=(b1,0) 和 D+ b=(b1/2,b1/2)；右侧最短输入沿对角线移动。')
 s.extend([text(28,83,'D⁺b = (b₁/2, b₁/2)：先投到横轴，再平均分配总量。',S),text(40,131,'输出空间：给定读数 b',B),text(560,131,'输入空间：选出的 D⁺b',B)])
 axes(s);axes(s,right=True,input=True)
 s.extend([line(xy(-1,0),xy(4,0),B,width=4),f'<circle cx="{xy(2,0)[0]}" cy="390" r="70" fill="none" stroke="#486073" stroke-dasharray="5 6"/>',line(xy(*b),xy(*p),R),dot(xy(*b),R),dot(xy(*p),B),line(xy(-.7,-.7,True),xy(2.8,2.8,True),B),line(xy(0,0,True),xy(*x,True),G,width=4),dot(xy(*x,True),G),text(445,275,'D⁺ →',W,23),text(690,170,'x₁ = x₂：最短输入方向',G,20),text(40,490,f'b = ({b[0]:.2f}, {b[1]:.2f})',R),text(560,490,f'D⁺b = ({x[0]:.2f}, {x[1]:.2f})',G),text(28,546,'再乘 D 只回到 p，不一定回到 b；伪逆给出选择，不能补回丢失的信息。',S,20)])
 return end(s)

"""Quadratic forms and constrained optimization: fixed teaching examples."""
from math import sin,cos,pi
from pathlib import Path
from html import escape
B='#71c9ff';G='#f8d174';R='#ff8d83';W='#e6edf4';S='#a7bacb'
def text(x,y,s,c=W,size=22):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(s)}</text>'
def line(p,q,c=S,w=2,dash=False):return f'<path d="M{p[0]},{p[1]} L{q[0]},{q[1]}" fill="none" stroke="{c}" stroke-width="{w}"'+(' stroke-dasharray="6 5"' if dash else '')+'/>'
def dot(p,c):return f'<circle cx="{p[0]}" cy="{p[1]}" r="6" fill="{c}"/>'
def curve(ps,c=B):return '<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in ps)+f'" fill="none" stroke="{c}" stroke-width="2"/>'
def start(title,desc):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600" viewBox="0 0 1000 600"><title>{escape(title)}</title><desc>{escape(desc)}</desc><rect width="1000" height="600" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(25,42,title,size=28)]
def end(s):return ''.join(s)+'</g></svg>'
def surfaces():
 s=start('二次型：抬头看曲面，低头看每个方向的高度','三幅固定曲面分别为2x²+y²、x²、x²-y²；三维平行投影用于表达形状，屏幕角度不代表空间角度。')
 for i,(name,f,note) in enumerate([('正定：2x² + y²',lambda x,y:2*x*x+y*y,'离开原点，所有方向都上升'),('半正定：x²',lambda x,y:x*x,'沿 y 方向平坦，最低点成一条线'),('不定：x² − y²',lambda x,y:x*x-y*y,'沿 x 上升，沿 y 下降')]):
  ox=170+330*i
  def p(x,y):return(ox+58*x+28*y,345+18*x-23*y-32*f(x,y))
  s.append(text(30+330*i,125,name,B,23))
  for j in range(-6,7):
   a=j/5
   s.extend([curve([p(a,k/20) for k in range(-24,25)],'#41657d'),curve([p(k/20,a) for k in range(-24,25)],'#41657d')])
  s.extend([curve([p(k/20,0) for k in range(-24,25)],G),curve([p(0,k/20) for k in range(-24,25)],R),dot(p(0,0),W),text(22+330*i,460,note,W,18)])
 s.extend([text(25,535,'金色截线：x 方向；红色截线：y 方向；白点：原点。',S),text(25,578,'图为三维结构的二维平行投影。高度是函数值，不是矩阵把输入送到的位置。',S,20)])
 return end(s)
def directions(t):
 a=pi*(1-cos(2*pi*t))/2;co=cos(a);si=sin(a);ks=[2*co*co+si*si,co*co,co*co-si*si]
 s=start('换一条经过原点的直线，看截面是碗、平线还是倒碗','三个矩阵固定，蓝色单位方向 d 转动；下方绘制 q(td)=(dᵀHd)t²。动画不是优化轨迹。')
 for i,(name,k) in enumerate(zip(['H = diag(2,1)','H = diag(1,0)','H = diag(1,−1)'],ks)):
  ox=170+330*i
  s.extend([text(30+330*i,110,name,B,22),line((ox-60,205),(ox+60,205)),line((ox,265),(ox,145)),line((ox,205),(ox+52*co,205-52*si),B,4),dot((ox+52*co,205-52*si),B),text(30+330*i,300,f'dᵀHd = {k:.2f}',G,23),line((ox-120,420),(ox+120,420)),line((ox,485),(ox,325)),curve([(ox+80*u/40,420-18*k*(u/40)**2) for u in range(-60,61)],G),text(ox+125,425,'t',S,18)])
 s.extend([text(25,540,'上图蓝线是方向 d；下图横轴 t 表示沿该方向走几份，纵轴是函数值。',S),text(25,578,'同一方向的正反两侧给出同一截面；往返考察全部直线方向。',S,20)])
 return end(s)
def chord(t):
 tau=(1-cos(2*pi*t))/2;x=-1+3*tau;z=x*x;chord=1+3*tau
 s=start('凸性：曲线始终在连接两端点的弦下方','固定函数 f(x)=x²，端点为(-1,1)和(2,4)，移动的横坐标是两端横坐标的凸组合。')
 def p(x,y):return(220+100*x,465-75*y)
 s.extend([line(p(-1.5,0),p(2.5,0)),line(p(0,-.2),p(0,4.6)),curve([p(k/50,(k/50)**2) for k in range(-65,111)],B),line(p(-1,1),p(2,4),G,3),line(p(x,z),p(x,chord),R,3),dot(p(x,z),B),dot(p(x,chord),G),text(560,155,'蓝点：先混合位置，再算高度',B),text(560,220,'金点：先算两端高度，再混合',G),text(560,300,f'混合比例 θ = {tau:.2f}'),text(560,360,f'弦高度 − 曲线高度 = {chord-z:.2f}',R),text(560,430,'始终非负；端点处等于零。'),text(25,545,'本图展示一个凸函数；一般定义要求任意两点及所有 0≤θ≤1 都成立。',S),text(25,580,'横轴为输入 x，纵轴为 f(x)；动画只改变比较位置，不改变函数。',S,20)])
 return end(s)
def constraint(t):
 a=1+1.2*sin(2*pi*t);b=2-a
 s=start('加上约束后：只能沿可行直线移动','最小化x²+y²，约束x+y=2；移动点始终可行，最优点(1,1)处梯度非零且垂直于可行直线。')
 def p(x,y):return(155+95*x,440-95*y)
 s.append('<defs><clipPath id="plot"><rect x="25" y="125" width="480" height="385"/></clipPath></defs><g clip-path="url(#plot)">')
 for radius in [1,2**.5,2,2.5]:s.append(f'<circle cx="155" cy="440" r="{95*radius}" stroke="#35586c" fill="none"/>')
 s.extend([line(p(-.5,0),p(3,0)),line(p(0,-.5),p(0,3)),line(p(-.4,2.4),p(2.4,-.4),B,4),line(p(0,0),p(a,b),G,3),dot(p(a,b),G),dot(p(1,1),R),line(p(1,1),p(1.7,1.7),R,4),text(335,270,'梯度方向',R,18),'</g>',text(560,145,'蓝线：所有满足 x+y=2 的点',B),text(560,220,f'当前点 = ({a:.2f}, {b:.2f})',G),text(560,280,f'目标 x²+y² = {a*a+b*b:.2f}'),text(560,355,'最小值 2，在 (1,1) 处取得。',R),text(560,420,'梯度非零，但可行方向上无法再下降。'),text(25,550,'圆是等高线；原点是无约束最优点，但不满足 x+y=2。',S),text(25,582,'红段只表示最优点处的梯度方向，长度经缩短以便显示；金点是候选，不是迭代。',S,19)])
 return end(s)
def sensors():
 s=start('传感器融合：三个读数，如何分配权重？','三个无偏误差互不相关的传感器，误差方差1、4、9。非负权重和为1。最优权重36/49、9/49、4/49。')
 for i,(v,num,c) in enumerate([(1,36,B),(4,9,G),(9,4,R)]):
  y=160+i*115;s.extend([text(35,y,f'传感器 {i+1}：误差方差 {v}',c,24),f'<rect x="380" y="{y-28}" width="{500*num/49}" height="35" fill="{c}"/>',text(380,y+42,f'权重 {num}/49 ≈ {num/49:.3f}',c,21)])
 s.extend([text(35,520,'权重与方差的倒数成比例：更稳定的读数获得更大权重。'),text(35,565,'融合误差方差 36/49 ≈ 0.735；这依赖无偏、协方差已知及模型约束。',S,21)])
 return end(s)
if __name__=='__main__':
 out=Path(__file__).resolve().parents[1]/'images';out.mkdir(exist_ok=True)
 for name,fn in [('surfaces',surfaces),('sensors',sensors)]: (out/('05-'+name+'.svg')).write_text(fn(),encoding='utf-8')

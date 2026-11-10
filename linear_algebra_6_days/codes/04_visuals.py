"""DAY 4 geometry: deterministic SVG scenes, standard library only."""
from math import sin,cos,pi,sqrt
from pathlib import Path
from html import escape
B='#71c9ff';G='#f8d174';R='#ff8d83';W='#e6edf4';S='#a7bacb'
def text(x,y,s,c=W,size=22):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(s)}</text>'
def line(p,q,c=S,w=2,dash=False):return f'<path d="M{p[0]},{p[1]} L{q[0]},{q[1]}" stroke="{c}" stroke-width="{w}" fill="none"'+(' stroke-dasharray="6 5"' if dash else '')+'/>'
def dot(p,c,r=5):return f'<circle cx="{p[0]}" cy="{p[1]}" r="{r}" fill="{c}"/>'
def pos(v,o=(270,320),k=65):return(o[0]+k*v[0],o[1]-k*v[1])
def arrow(v,o=(270,320),k=65,c=G):
 p=pos(v,o,k);return line(o,p,c,4)+f'<circle cx="{p[0]}" cy="{p[1]}" r="5" fill="{c}"/>'
def rot(v,a):return(cos(a)*v[0]-sin(a)*v[1],sin(a)*v[0]+cos(a)*v[1])
def start(title,desc):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600" viewBox="0 0 1000 600"><title>{escape(title)}</title><desc>{escape(desc)}</desc><rect width="1000" height="600" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(25,40,title,size=28)]
def end(s):return ''.join(s)+'</g></svg>'
def axes(s,o,k=65,r=3):
 for j in range(-r,r+1):s.extend([line(pos((j,-r),o,k),pos((j,r),o,k),'#22394a',1),line(pos((-r,j),o,k),pos((r,j),o,k),'#22394a',1)])
 s.extend([line(pos((-r,0),o,k),pos((r,0),o,k)),line(pos((0,-r),o,k),pos((0,r),o,k))])
def curve(points,c=B):return '<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+f'" fill="none" stroke="{c}" stroke-width="2"/>'
def eigen(t):
 a=2*pi*t+pi/4;v=(cos(a),sin(a));av=(2*v[0]+v[1],v[0]+2*v[1]);s=start('① 特征方向：箭头变长，却留在原来的直线上','固定矩阵 S=[[2,1],[1,2]]。金色单位输入绕圈，红色输出每帧由 S 计算；蓝色斜线是特征方向。')
 axes(s,(270,320),65,3)
 for sign in [1,-1]:s.append(line(pos((-2.2,-2.2*sign)),pos((2.2,2.2*sign)),B,2,True))
 s.extend([curve([pos((cos(i*pi/90),sin(i*pi/90))) for i in range(181)],S),arrow(av,c=R),arrow(v,c=G),text(560,130,'固定规则：S(x,y) = (2x+y, x+2y)',size=22),text(560,200,'金色：输入 v（长度为 1）',G),text(560,250,'红色：输出 Sv',R),text(560,320,'右上方向：Sv = 3v',B),text(560,370,'右下方向：Sv = v',B),text(560,440,'多数方向：红、金箭头不共线。'),text(25,555,'只观察两根箭头是否在同一条过原点的直线上；不是不断重复乘 S。',S),text(25,585,'坐标固定、等比例。每帧更换输入方向，矩阵始终不变。',S,20)])
 return end(s)
def signs(t):
 # A fixed input; phase interpolates only for illustrating endpoint transformations.
 s=start('② 特征值的符号：同向、反向，还是消失','三幅图用同一输入 v=(1,0)。每幅在输入与各自输出之间往返显示，最终倍数为2、-1、0。')
 u=max(0,min(1,1.4*(1-cos(2*pi*t))/2-.2))
 s.append(text(25,85,f'演示进度：{100*u:.0f}%（100% 时彩色箭头等于 λv）',S,21))
 for i,(lam,label) in enumerate([(2,'λ = 2：同向拉长'),(-1,'λ = −1：反向'),(0,'λ = 0：压到原点')]):
  o=(170+330*i,320);axes(s,o,65,2)
  s.extend([line(o,pos((1,0),o),S,6,True),arrow((1+u*(lam-1),0),o,65,[G,R,B][i]),text(35+330*i,140,label,[G,R,B][i],23)])
 s.extend([text(25,520,'灰色参考段：原输入。彩色端点：用插值展示变化；终点才是 λv。',S),text(25,565,'负号翻转箭头；零值可以对应非零特征向量，但输出没有方向。',W)])
 return end(s)
def svd(t):
 v=(cos(2*pi*t),sin(2*pi*t));funcs=[lambda x:x,lambda x:rot(x,-pi/4),lambda x:(2*rot(x,-pi/4)[0],.5*rot(x,-pi/4)[1]),lambda x:rot((2*rot(x,-pi/4)[0],.5*rot(x,-pi/4)[1]),pi/6)]
 s=start('③ SVD：读入方向 → 分轴伸缩 → 放到输出方向','固定 A=R30 diag(2,0.5) R(-45)。四图使用固定等比例坐标，同一个单位输入每帧经三个阶段变换。')
 for i,(f,title) in enumerate(zip(funcs,['输入 x','Vᵀ：转 −45°','Σ：乘 2 与 0.5','U：转 +30°'])):
  o=(130+245*i,315);axes(s,o,45,2)
  s.extend([text(30+245*i,140,title,B,21),curve([pos(f((cos(j*pi/90),sin(j*pi/90))),o,45) for j in range(181)],B),arrow(f(v),o,45,G)])
 s.extend([text(25,480,'蓝色轮廓：所有单位输入的去向。金点：同一支输入在各阶段的位置。',S),text(25,530,'最后椭圆半轴长是 2、0.5；输入主轴与输出主轴可以不是同一方向。',W),text(25,575,'这里三段矩阵固定；动画改变的是输入，不是在反复累乘 A。',S,20)])
 return end(s)
def points():return [((a-b)/sqrt(2),(a+b)/sqrt(2)) for a in [-3,-1,1,3] for b in [-1,1]]
def pca(t):
 angle=pi/4+pi*sin(2*pi*t)/2;q=(cos(angle),sin(angle));data=points();var=sum((x*q[0]+y*q[1])**2 for x,y in data)/7
 s=start('④ PCA：转动尺子，寻找投影最分散的方向','八个固定、中心为零的教学点。转动一维投影方向，金点为正交投影，右侧显示样本投影方差。')
 o=(255,325);axes(s,o,56,3)
 s.append(line(pos((-3.5*q[0],-3.5*q[1]),o,56),pos((3.5*q[0],3.5*q[1]),o,56),B,3))
 for x,y in data:
  c=x*q[0]+y*q[1];p=(c*q[0],c*q[1]);s.extend([line(pos((x,y),o,56),pos(p,o,56),'#496478',1),dot(pos((x,y),o,56),S),dot(pos(p,o,56),G)])
 s.extend([text(545,145,'灰点：固定数据；金点：投影',S),text(545,210,f'方向角 = {angle*180/pi:.1f}°',B),text(545,270,f'投影方差 = {var:.3f}',G),f'<rect x="545" y="300" width="{340*var/(40/7):.2f}" height="24" fill="{G}"/>',text(545,365,'最大：40/7，沿右上方向',B),text(545,420,'第一主轴保留方差比例 = 5/6'),text(25,550,'投影越分散，保留的变化越多；同时，灰点到直线的总平方距离越小。',W),text(25,585,'教学构造，非真实传感器数据；每根轴单位相同。',S,20)])
 return end(s)
def boundaries():
 s=start('不是每个矩阵，都有足够的特征方向','左侧九十度旋转没有实特征方向；右侧错切只有水平方向的特征向量，不能组成二维基。')
 for i,(title,fn,v) in enumerate([('旋转 90°：没有实特征向量',lambda p:(-p[1],p[0]),(1,0)),('错切：只有一条特征直线',lambda p:(p[0]+p[1],p[1]),(0,1))]):
  o=(240+i*510,330);axes(s,o,65,2);s.extend([text(35+i*510,130,title,B,24),arrow(v,o,65,G),arrow(fn(v),o,65,R)])
 s.extend([text(30,505,'旋转后的非零箭头总与原箭头垂直。'),text(540,505,'水平箭头不变；竖直箭头变斜。'),text(30,565,'金色为输入，红色为输出。寻找同方向特征向量失败时，仍可使用 SVD。',S)])
 return end(s)
def ellipsoid():
 s=start('⑤ 从二维点云到三维：方向看特征向量，半轴看标准差','三维教学协方差 diag(9,4,1) 的一标准差尺度椭球，半轴为3、2、1。以平行投影绘制，非概率覆盖保证。')
 def project(x,y,z):return(310+52*x+27*y,350+16*x-23*y-65*z)
 for zangle in [-pi/3,0,pi/3]:
  s.append(curve([project(3*cos(zangle)*cos(j*pi/90),2*cos(zangle)*sin(j*pi/90),sin(zangle)) for j in range(181)],B))
 for a in [0,pi/4,pi/2,3*pi/4]:s.append(curve([project(3*cos(j*pi/90)*cos(a),2*cos(j*pi/90)*sin(a),sin(j*pi/90)) for j in range(181)],'#466d86'))
 for v,c,label in [((3,0,0),G,'3'),((0,2,0),R,'2'),((0,0,1),B,'1')]:
  p=project(*v);s.extend([line(project(0,0,0),p,c,4),text(p[0]+9,p[1],label,c)])
 s.extend([text(600,160,'协方差特征值：9、4、1'),text(600,225,'方差的单位是长度²。',S),text(600,300,'椭球半轴长：3、2、1',G),text(600,365,'半轴 = 特征值的平方根'),text(600,430,'朝向由对应的单位特征向量决定。',size=20),text(25,545,'这里是三维结构的二维平行投影；屏幕夹角不等于真实空间夹角。',S),text(25,580,'这是离散程度的示意，不声称所有点都在椭球内，也不是置信区域。',S,20)])
 return end(s)
if __name__=='__main__':
 out=Path(__file__).resolve().parents[1]/'images';out.mkdir(exist_ok=True)
 for name,f in [('boundaries',boundaries),('ellipsoid',ellipsoid)]: (out/('04-'+name+'.svg')).write_text(f(),encoding='utf-8')

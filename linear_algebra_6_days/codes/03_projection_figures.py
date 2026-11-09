"""Four static teaching diagrams; Python 3.9+ standard library only."""
from pathlib import Path
from html import escape
B='#71c9ff'; R='#ff8d83'; G='#f8d174'; W='#e6edf4'; S='#a7bacb'
def txt(x,y,t,c=W,size=22):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(t)}</text>'
def line(x,y,X,Y,c=S,dash=False,width=3):return f'<path d="M{x},{y} L{X},{Y}" fill="none" stroke="{c}" stroke-width="{width}"'+(' stroke-dasharray="8 6"' if dash else '')+'/>'
def dot(x,y,c=G):return f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>'
def start(title,desc):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="620" viewBox="0 0 1100 620"><title>{escape(title)}</title><desc>{escape(desc)}</desc><rect width="1100" height="620" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',txt(30,45,title,size=29)]
def finish(s):return ''.join(s)+ '</g></svg>'
def projection():
 s=start('直线投影：沿垂线抵达最近点','固定二维等比例坐标。a=(1,1)，b=(3,1)，p=(2,2)，q=(0.5,0.5)。红线是残差，蓝线为可达直线。')
 def xy(x,y):return 90+105*x,485-105*y
 for k in range(5):
  s.extend([line(*xy(k,0),*xy(k,4),'#263c50',width=1),line(*xy(0,k),*xy(4,k),'#263c50',width=1)])
 s.extend([line(*xy(0,0),*xy(4.3,0)),line(*xy(0,0),*xy(0,4.1)),txt(535,510,'x'),txt(65,65,'y'),line(*xy(0,0),*xy(3.8,3.8),B),line(*xy(.5,.5),*xy(3,1),S,True),line(*xy(2,2),*xy(3,1),R),line(*xy(2,2),*xy(.5,.5),G)])
 # right-angle corner in data coordinates
 s.extend([line(*xy(1.84,1.84),*xy(2,1.68),W,width=2),line(*xy(2,1.68),*xy(2.16,1.84),W,width=2)])
 for x,y,label,c,dx,dy in [(0,0,'0',S,-20,25),(.5,.5,'q',G,-25,10),(2,2,'p = (2,2)',B,-100,-20),(3,1,'b = (3,1)',R,15,0)]:s.extend([dot(*xy(x,y),c),txt(xy(x,y)[0]+dx,xy(x,y)[1]+dy,label,c)])
 s.extend([txt(625,135,'蓝线：所有可达点 ca',B),txt(625,195,'红段：残差 b − p，与蓝线垂直',R),txt(625,255,'黄段：换一个候选点所多走的路',G),txt(625,330,'距离平方 = 红段² + 黄段²'),txt(625,385,'只要 q ≠ p，黄段就非零。'),txt(625,440,'所以 p 是唯一最近点。'),txt(30,575,'坐标等比例；网格间隔为 1。灰色虚线连接另一个候选点 q 与目标 b。',S)])
 return finish(s)
def plane():
 s=start('最近可达输出：留下的差必须垂直于列空间','左侧是穿过目标与垂足的截面示意，不是三维坐标图。右侧列出 M 与读数 b 对应的真实坐标。')
 s.extend([txt(30,90,'几何截面示意（不按右侧坐标绘制）',S),line(60,430,510,430,B,width=5),dot(280,430,B),dot(280,175,R),dot(420,430,G),line(280,430,280,175,R),line(420,430,280,175,S,True),line(280,410,300,410,W,width=2),line(300,410,300,430,W,width=2),txt(260,468,'p',B),txt(285,150,'b',R),txt(425,465,'y',G),txt(90,510,'列空间与截面的交线',B),txt(160,290,'残差 r',R),txt(600,135,'三维算例：y₃ = y₁ + y₂',B,26),txt(600,205,'目标 b = (2, 1, 4)',R),txt(600,275,'最近点 p = (7/3, 4/3, 11/3)',B),txt(600,345,'残差 r = (−1/3, −1/3, 1/3)',R),txt(600,415,'p 在平面内；r 垂直于两列。'),txt(600,485,'输入估计 x̂ = (7/3, 4/3)',G),txt(30,580,'最近输出 p 在三维读数空间；估计输入 x̂ 在二维输入空间。',S)])
 return finish(s)
def trajectory():
 s=start('轨迹拟合：三次位置差，组成一个残差向量','教学数据：时间 -1,0,1 秒，位置 0,1,3 米。拟合直线 s=4/3+3t/2；红段为同一时刻的竖直位置差。')
 def xy(t,v):return 300+175*t,455-95*v
 for k in range(4):s.extend([line(85,455-95*k,510,455-95*k,'#263c50',width=1),txt(52,462-95*k,str(k),S,18)])
 s.extend([line(85,455,530,455),line(85,505,85,100),txt(40,90,'位置 / 米',S),txt(400,535,'时间 / 秒',S),line(*xy(-1.1,4/3-1.65),*xy(1.1,4/3+1.65),B)])
 for t,v in [(-1,0),(0,1),(1,3)]:
  pred=4/3+1.5*t
  s.extend([line(*xy(t,v),*xy(t,pred),R,width=5),dot(*xy(t,v),G),txt(xy(t,v)[0]-10,490,str(t),S,18)])
 s.extend([txt(600,130,'左图：固定时间，只比较位置',G,25),txt(600,190,'金点：读数     蓝线：匀速模型'),txt(600,245,'红段：竖直位置差，不是斜距',R),txt(600,330,'读数空间：每个时刻占一根轴',B,25),txt(600,390,'r = (1/6, −1/3, 1/6)'),txt(600,445,'r ⟂ (1,1,1)，r ⟂ (−1,0,1)'),txt(600,500,'垂直的是残差与整个模型平面。'),txt(30,585,'同一组数据：左图画三个点；读数空间把三个位置合成一个三维点。',S)])
 return finish(s)
def qr():
 s=start('QR：扣除已有方向，再保留新的垂直方向','在列空间自身的 q1,q2 正交坐标中画出 a1=(sqrt2,0)、a2=(1/sqrt2,sqrt(3/2))。红色竖段是 u2，黄色横段是投影。')
 from math import sqrt
 def xy(x,y):return 110+230*x,465-230*y
 s.extend([txt(30,90,'此图使用 q₁、q₂ 坐标，保持长度与夹角',S),line(*xy(0,0),*xy(1.7,0),B),line(*xy(0,0),*xy(0,1.45),B),txt(500,495,'q₁',B),txt(65,125,'q₂',B),line(*xy(0,0),*xy(sqrt(2),0),B,width=4),line(*xy(0,0),*xy(1/sqrt(2),0),G,width=6),line(*xy(0,0),*xy(1/sqrt(2),sqrt(1.5)),W),line(*xy(1/sqrt(2),0),*xy(1/sqrt(2),sqrt(1.5)),R,width=4),dot(*xy(sqrt(2),0),G),dot(*xy(1/sqrt(2),sqrt(1.5)),W),txt(395,445,'a₁',G),txt(285,165,'a₂'),txt(285,330,'u₂',R),txt(100,520,'黄色段：a₂ 沿 q₁ 的投影',G),txt(610,155,'a₁ = √2 q₁',G,26),txt(610,225,'a₂ = (1/√2) q₁ + √(3/2) q₂',W,23),txt(610,310,'Q：把新基 q₁、q₂ 排成列',B),txt(610,380,'R：把这两份坐标排成列',G),txt(610,450,'原列 = 新基 × 坐标，即 M = QR'),txt(30,580,'剩余向量 u₂ 与 q₁ 正交；将 u₂ 除以长度，得到单位向量 q₂。',S)])
 return finish(s)
if __name__=='__main__':
 out=Path(__file__).resolve().parents[1]/'images';out.mkdir(exist_ok=True)
 for name,fn in [('line-projection',projection),('plane-residual',plane),('trajectory-fit',trajectory),('qr-basis',qr)]:
  (out/('03-'+name+'.svg')).write_text(fn(),encoding='utf-8')

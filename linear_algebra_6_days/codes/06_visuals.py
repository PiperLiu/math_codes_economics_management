"""DAY 6 deterministic teaching diagrams; standard library only."""
from math import sin, cos, pi, sqrt
from pathlib import Path
from html import escape
B='#71c9ff'; G='#f8d174'; R='#ff8d83'; W='#e6edf4'; S='#a7bacb'; GREEN='#83d9b0'
def text(x,y,s,c=W,size=22):
    return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(s)}</text>'
def line(p,q,c=S,w=2,dash=False):
    return f'<path d="M{p[0]:.3f},{p[1]:.3f} L{q[0]:.3f},{q[1]:.3f}" fill="none" stroke="{c}" stroke-width="{w}"'+(' stroke-dasharray="6 5"' if dash else '')+'/>'
def dot(p,c,size=6):return f'<circle cx="{p[0]:.3f}" cy="{p[1]:.3f}" r="{size}" fill="{c}"/>'
def curve(ps,c=B,w=2):return '<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in ps)+f'" fill="none" stroke="{c}" stroke-width="{w}"/>'
def start(title,desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600" viewBox="0 0 1000 600"><title>{escape(title)}</title><desc>{escape(desc)}</desc><rect width="1000" height="600" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(25,44,title,size=28)]
def end(s):return ''.join(s)+'</g></svg>'
def matrix(s,x,y,rows,color=W,step=82):
    height=len(rows)*48
    s.extend([line((x-15,y-24),(x-15,y+height-33),color),line((x+len(rows[0])*step-20,y-24),(x+len(rows[0])*step-20,y+height-33),color)])
    for edge,sign in [(x-15,1),(x+len(rows[0])*step-20,-1)]:
        for yy in [y-24,y+height-33]:s.append(line((edge,yy),(edge+sign*9,yy),color))
    for i,row in enumerate(rows):
        for j,value in enumerate(row):s.append(text(x+j*step,y+i*48,str(value),color,24))
def cone():
    s=start('矩阵空间：半正定矩阵组成一个凸锥','二阶对称矩阵用(v,r,u)三个坐标表示；半正定条件u≥√(v²+r²)。图为截断后的三维平行投影。')
    def p(v,r,u):return(270+100*v+55*r,480+30*v-40*r-145*u)
    for h in [.4,.8,1,1.4,1.8,2.1]:
        s.append(curve([p(h*cos(k*pi/80),h*sin(k*pi/80),h) for k in range(161)],G if h==1 else '#41657d',3 if h==1 else 1))
    for j in range(12):s.append(line(p(0,0,0),p(2.1*cos(j*pi/6),2.1*sin(j*pi/6),2.1),'#41657d',1))
    for dest,label in [(p(1.4,0,0),'v'),(p(0,2.7,0),'r'),(p(0,0,2.6),'u')]:
        s.extend([line(p(0,0,0),dest),text(dest[0]+6,dest[1],label,S,20)])
    s.extend([dot(p(0,0,0),W),text(560,145,'X = [[u+v, r], [r, u−v]]',B,24),text(560,210,'λ = u ± √(v²+r²)'),text(560,275,'半正定：u ≥ √(v²+r²)',GREEN,24),text(560,345,'金色圆周：u=1 的截面边界',G,22),text(560,392,'圆周内部也包含在可行集合中。',S,20),text(560,455,'锥顶：零矩阵，秩为 0。',W,22),text(25,550,'空间中的点代表矩阵；不是矩阵作用于输入后得到的点。',S),text(25,583,'只画到 u=2.1；真正的锥无限延伸。投影角度不代表空间中的真实角度。',S,19)])
    return end(s)
def slice_scene(t):
    rho=.4+1.1*(1+cos(2*pi*t))/2;v=.6*rho;r=.8*rho
    s=start('固定迹为 2：圆盘内的点才是半正定矩阵','矩阵X=[[1+v,r],[r,1-v]]，点沿固定射线往返；特征值为1±√(v²+r²)。')
    def p(v,r):return(245+135*v,340-135*r)
    s.extend([f'<circle cx="245" cy="340" r="135" fill="#163849" stroke="{B}" stroke-width="2"/>',line(p(-1.5,0),p(1.6,0)),line(p(0,-1.1),p(0,1.65)),text(465,350,'v',S),text(253,110,'r',S),line(p(0,0),p(v,r),G,3),dot(p(v,r),G),text(50,530,'蓝色圆盘：v²+r² ≤ 1',B,23),text(565,125,f'v = {v:.2f}    r = {r:.2f}',G,24)])
    matrix(s,600,185,[[f'{1+v:.2f}',f'{r:.2f}'],[f'{r:.2f}',f'{1-v:.2f}']],step=125)
    for j,val in enumerate([1+rho,1-rho]):
        y=320+80*j
        s.extend([text(550,y+6,f'λ{j+1}',W),line((705,y),(705+80*val,y),GREEN if val>=0 else R,16),line((705,y-22),(705,y+22),S,1),text(550,y+42,f'{val:+.2f}',GREEN if val>=0 else R,22)])
    s.extend([text(550,515,'正定：所有方向都有正高度' if rho<1 else '不定：存在负高度方向',GREEN if rho<1 else R,22),text(25,583,'动画改变矩阵条目；圆周上最小特征值为零，非零矩阵的秩降为 1。',S,20)])
    return end(s)
def gram(t):
    phi=2*pi*t;c=.36+.64*cos(phi)
    def p(x,y,z):return(210+140*x+70*y,355+40*x-50*y-105*z)
    origin=p(0,0,0);u1=p(1,0,0);u2=p(.6,.8,0);u3=p(.6,.8*cos(phi),.8*sin(phi))
    s=start('相关系数是内积：三支单位向量必须能同时摆出来','第一支固定，第二支与第一支内积0.6，第三支绕第一支旋转；第三对内积c=0.36+0.64cosφ。')
    s.append(curve([p(.6,.8*cos(k*pi/80),.8*sin(k*pi/80)) for k in range(161)],'#41657d'))
    for q in [p(1.5,0,0),p(0,1.5,0),p(0,0,1.5)]:s.append(line(origin,q,'#35586c',1))
    for dest,col in [(u1,B),(u2,R),(u3,G)]:s.extend([line(origin,dest,col,4),dot(dest,col)])
    s.extend([dot(origin,W),line(u3,p(.6,0,0),G,1,True),text(45,160,'灰色椭圆：圆形轨迹的投影',S,21),text(45,460,'第一轴方向分量固定为 0.6',G,22),text(550,135,'蓝：u₁    红：u₂    金：u₃',W,23),text(550,200,'u₁·u₂ = u₁·u₃ = 0.6',B,24),text(550,265,f'φ = {phi*180/pi:.0f}°',G,23),text(550,330,'c = 0.36 + 0.64 cos φ'),text(550,390,f'c = {c:.3f}',G,30),line((570,455),(920,455),B,5),dot((570+(c+.28)/1.28*350,455),G),text(545,491,'−0.28',S,19),text(910,491,'1',S,19),text(25,550,'两支向量都向第一支靠拢后，彼此再反向也存在限度。',S),text(25,583,'图为三维平行投影；φ 是绕第一轴的转角，不是 u₂ 与 u₃ 的夹角。',S,20)])
    return end(s)
def repair(t):
    t=t%1
    if t<.1:p=0
    elif t<.4:p=(1-cos(pi*(t-.1)/.3))/2
    elif t<.6:p=1
    elif t<.9:p=(1+cos(pi*(t-.6)/.3))/2
    else:p=0
    c=-.8+.52*p;eigs=[1+c/2-.5*sqrt(c*c+2.88),1-c,1+c/2+.5*sqrt(c*c+2.88)]
    s=start('只修改第三对相关性：走到最近的合法边界','观测c=-0.8，保持其余条目；最近PSD值为c=-0.28。路径为演示用插值，不是求解器迭代。')
    s.append(text(65,130,'候选相关矩阵 R(c)',B,24))
    matrix(s,85,205,[['1','0.6','0.6'],['0.6','1',f'{c:.2f}'],['0.6',f'{c:.2f}','1']],step=120)
    s.extend([text(60,400,f'改动幅度 = {c+.8:.3f}',G,24),line((60,465),(460,465),S,2),line((204,465),(460,465),GREEN,7),dot((60+(c+1)*200,465),G),text(45,500,'−1',S,18),text(175,500,'−0.28',GREEN,18),text(452,500,'1',S,18),text(560,130,'三个特征值（未按大小排序）',S,20)])
    for j,val in enumerate(eigs):
        y=205+85*j
        s.extend([line((710,y),(710+90*max(val,0) if val>=0 else 710+90*val,y),GREEN if val>=-1e-10 else R,17),line((710,y-22),(710,y+22),S,1),text(570,y+8,f'{0 if abs(val)<1e-10 else val:+.3f}',GREEN if val>=-1e-10 else R,25)])
    s.extend([text(560,470,'已到达半正定边界' if p==1 else '仍有负特征值，尚不可行',GREEN if p==1 else R,24),text(25,550,'绿色区间是合法 c：−0.28 ≤ c ≤ 1；金点是当前候选。',S),text(25,583,'往返插值用于比较修复前后；只有端点 −0.28 合法，不是算法运行轨迹。',S,19)])
    return end(s)
def choices():
    s=start('同一份数据，不同约束，对应不同修复结果','原矩阵[[1,1.2],[1.2,1]]；仅PSD修复为全1.1，单位对角线加PSD修复为全1。')
    s.append(text(25,105,'原矩阵 A = [[1, 1.2], [1.2, 1]]；特征值 2.2、−0.2',S,22))
    for x,title,rows,detail in [(35,'只要求半正定',[['1.1','1.1'],['1.1','1.1']],'截断负特征值；对角线变为 1.1'),(525,'半正定 + 对角线为 1',[['1','1'],['1','1']],'对角线必须保留；改变两处非对角项')]:
        s.extend([f'<rect x="{x}" y="145" width="440" height="340" rx="16" fill="#163044"/>',text(x+20,198,title,B,25)])
        matrix(s,x+105,280,rows,step=100)
        s.append(text(x+20,402,detail,W,20))
    s.extend([text(55,450,'全部条目的平方改动量：0.04',G,21),text(545,450,'全部条目的平方改动量：0.08',G,21),text(25,545,'增加约束后，允许的候选更少，最近距离可能变大。',S),text(25,582,'把左图对角线直接改回 1，会重新得到不定矩阵。',R,21)])
    return end(s)
def roadmap():
    s=start('六天收束：从读懂矩阵，到选择矩阵','六个阶段：空间变换、秩、投影、特征分解、凸二次优化、半正定规划。')
    cards=[('01  空间变换','列记录基本方向的去向','输入怎样组合，输出就怎样组合'),('02  秩与零空间','哪些区别被保留或压掉','秩看输出；零空间找丢失方向'),('03  投影与最小二乘','在可达范围内寻找最近点','先找最佳预测，再区分输入解'),('04  特征分解与 SVD','沿特殊方向分开理解','倍数、方差和压缩各有含义'),('05  二次型与凸优化','给每个方向检查曲率','凸性与可行方向共同决定最优'),('06  半正定规划','让矩阵本身成为未知量','选择目标，写清约束，核对结果')]
    for i,(title,body,sub) in enumerate(cards):
        x=30+(i%2)*485;y=100+(i//2)*145
        s.extend([f'<rect x="{x}" y="{y}" width="455" height="125" rx="12" fill="#163044"/>',text(x+18,y+35,title,G,24),text(x+18,y+72,body,W,22),text(x+18,y+105,sub,S,19)])
    s.append(text(30,575,'共同问题：未知量是什么？哪些方向重要？哪些条件必须满足？怎样检验？',S,21))
    return end(s)
if __name__=='__main__':
    out=Path(__file__).resolve().parents[1]/'images';out.mkdir(exist_ok=True)
    for name,fn in [('cone',cone),('repair-choices',choices),('roadmap',roadmap)]:
        (out/f'06-{name}.svg').write_text(fn(),encoding='utf-8')

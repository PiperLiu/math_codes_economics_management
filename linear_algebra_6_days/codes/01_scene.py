"""Deterministic SVG scene, authored for lesson 1; SVG contract follows svg-to-gif.
Animation interpolates I and A; each frame transforms ORIGINAL coordinates.
"""
import math
from pathlib import Path

FONT = 'PingFang SC, Microsoft YaHei, Arial, sans-serif'

def header(title, desc, width=800, height=500):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><title>{title}</title><desc>{desc}</desc><rect width="100%" height="100%" fill="#101d2b"/><g font-family="{FONT}" fill="#e6edf4">'

def line(p,q,color,width=1,dash=''):
    return f'<line x1="{p[0]:.3f}" y1="{p[1]:.3f}" x2="{q[0]:.3f}" y2="{q[1]:.3f}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'

def label(x,y,value,color='#e6edf4',size=19):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{value}</text>'

def svg_frame(t):
    # Endpoint holds, smooth travel, exact periodicity.
    phase=t%1
    if phase < .12: s=0
    elif phase < .42: s=(1-math.cos(math.pi*(phase-.12)/.30))/2
    elif phase < .58: s=1
    elif phase < .88: s=(1+math.cos(math.pi*(phase-.58)/.30))/2
    else: s=0
    def p(x,y): return 330+52*((1+s)*x+s*y), 300-52*y
    def base(x,y): return 330+52*x,300-52*y
    out=[header('矩阵怎样改变网格','固定世界坐标，红蓝箭头追踪两个基向量，黄色点追踪 (1,1)。'),
         '<defs><clipPath id="plot"><rect x="20" y="90" width="760" height="330"/></clipPath></defs>',
         label(30,36,'01 / 跟着基向量，看空间怎样变化', '#a7bacb',18), label(535,36,f'变形进度 s = {s:.2f}', '#f8d174',20),
         label(30,70,f'A(s) = [[{1+s:.2f}, {s:.2f}], [0, 1]]',size=24),'<g clip-path="url(#plot)">']
    for k in range(-8,9):
        out += [line(base(k,-8),base(k,8),'#273748'),line(base(-8,k),base(8,k),'#273748')]
    for k in range(-8,9):
        out += [line(p(k,-8),p(k,8),'#43677a'),line(p(-8,k),p(8,k),'#43677a')]
    out += [line(base(-8,0),base(8,0),'#8193a5',2),line(base(0,-8),base(0,8),'#8193a5',2)]
    pts=' '.join(f'{x:.2f},{y:.2f}' for x,y in [p(0,0),p(1,0),p(1,1),p(0,1)])
    out += [f'<polygon points="{pts}" fill="#358eac" fill-opacity=".25"/>']
    for v,col,name,dy in [((1,0),'#ff8d83','A e1',26),((0,1),'#71c9ff','A e2',-12)]:
        q=p(*v); o=p(0,0)
        out.append(line(o,q,col,4))
        angle=math.atan2(q[1]-o[1],q[0]-o[0]); a=angle+.45;b=angle-.45
        out += [line(q,(q[0]-12*math.cos(a),q[1]-12*math.sin(a)),col,4),line(q,(q[0]-12*math.cos(b),q[1]-12*math.sin(b)),col,4),label(q[0]+10,q[1]+dy,name,col)]
    x,y=p(1,1)
    out += [f'<circle cx="{x}" cy="{y}" r="6" fill="#f8d174"/>',label(x+12,y-16,'A (1,1)', '#f8d174'),label(315,325,'0'),label(752,325,'x'),label(342,110,'y'),'</g>',label(30,458,'红色向量 + 蓝色向量 = 黄色点的位置向量', '#f8d174',21),label(30,486,'坐标轴固定；每帧将当前矩阵作用于原始坐标一次', '#a7bacb',17),'</g></svg>']
    return ''.join(out)

def cube_svg():
    out=[header('三维立方体的线性变换','左图为单位立方体，右图先沿 x 放大两倍，再绕 z 旋转90度；二维平行投影仅用于显示。',1000,470),label(30,40,'02 / 三维物体：矩阵的列仍然记录基向量的去向',size=25)]
    out += [label(75,82,'原始单位立方体',size=21),label(580,82,'沿 x 轴放大两倍，再绕 z 轴旋转 90°',size=21)]
    vertices=[(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    edges=[(a,b) for i,a in enumerate(vertices) for b in vertices[i+1:] if sum(x!=y for x,y in zip(a,b))==1]
    for ox,changed in [(200,False),(760,True)]:
        def project(v):
            x,y,z=v
            return ox+95*x-60*y,350-35*x-45*y-110*z
        def transform(v):
            x,y,z=v
            return (-y,2*x,z) if changed else v
        for axis,name,col in [((1.55,0,0),'x','#ff8d83'),((0,2.4,0),'y','#71c9ff'),((0,0,1.65),'z','#99dfb0')]:
            o=project((0,0,0));q=project(axis)
            out += [line(o,q,'#637386',1),label(q[0]+5,q[1],name,col)]
        for a,b in edges:
            if changed: out.append(line(project(a),project(b),'#546375',1,'5 5'))
            out.append(line(project(transform(a)),project(transform(b)),'#bbcddd',2))
        for axis,col in [((1,0,0),'#ff8d83'),((0,1,0),'#71c9ff'),((0,0,1),'#99dfb0')]:
            out.append(line(project((0,0,0)),project(transform(axis)),col,5))
        q=project(transform((1,1,1)))
        out += [f'<circle cx="{q[0]}" cy="{q[1]}" r="5" fill="#f8d174"/>',label(q[0]-48,q[1]-16,'(-1,2,1)' if changed else '(1,1,1)','#f8d174'),label(ox-125,408,'Rz S : (x,y,z) → (-y,2x,z)' if changed else 'I : (x,y,z) → (x,y,z)',size=20)]
    out += [label(30,452,'平行投影仅用于展示三维结构；虚线表示原始立方体。', '#a7bacb',19),'</g></svg>']
    return ''.join(out)

if __name__ == '__main__':
    images=Path(__file__).resolve().parents[1]/'images'
    (images/'01-cube-transform.svg').write_text(cube_svg(),encoding='utf-8')
    (images/'01-grid-endpoint.svg').write_text(svg_frame(.5),encoding='utf-8')

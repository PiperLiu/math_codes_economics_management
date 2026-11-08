"""Visual explanation of redundant and contradictory constraints. Stdlib only."""
from pathlib import Path
from html import escape
BLUE='#71c9ff';GOLD='#f8d174';RED='#ff8d83';TEXT='#e6edf4';GRAY='#a7bacb'
def text(x,y,s,c=TEXT,size=23):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}">{escape(s)}</text>'
def box(x,y,w,h,c):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{c}" fill-opacity=".07" stroke="{c}" stroke-width="2"/>'
def svg():
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="690" viewBox="0 0 1100 690"><title>消元：从汇总记录中剔除已有信息</title><desc>第一读数 x1+x3=2，第二读数 x2+x3=1，其和必为 x1+x2+2x3=3。第三条减去前两条后，若汇总为3则得到0=0，若汇总为4则得到0=1。前者是冗余，后者是矛盾。</desc><rect width="1100" height="690" fill="#101d2b"/><g font-family="PingFang SC, Microsoft YaHei, Arial, sans-serif">',text(30,43,'消元：第三条记录还剩多少新信息？',size=29),text(30,81,'先读等式的含义，再把同样的操作写进矩阵。',GRAY,21)]
 for x,title,eq,c in [(30,'① 第一个显示器','x₁ + x₃ = 2',BLUE),(400,'② 第二个显示器','x₂ + x₃ = 1',BLUE),(770,'③ 应有的汇总','x₁ + x₂ + 2x₃ = 3',GOLD)]:
  s.extend([box(x,120,300,140,c),text(x+22,163,title,c,23),text(x+22,219,eq,size=24)])
 s.extend([text(350,205,'+',GRAY,30),text(721,205,'=',GRAY,30),text(30,311,'③ 的左侧是 ①、② 左侧之和，因此右侧也必须等于 2 + 1。',size=23),text(30,352,'保留 ①、②，把 ③ 改写为：③ − ① − ②。',GOLD,24)])
 for x,c,title,calc,conclusion in [(30,BLUE,'汇总记录为 3','3 − 2 − 1 = 0','0 = 0：没有新增限制'),(590,RED,'汇总记录为 4','4 − 2 − 1 = 1','0 = 1：没有输入能够满足')]:
  s.extend([box(x,387,480,202,c),text(x+24,428,title,c,25),text(x+24,472,'左侧：变量项全部抵消，剩下 0',size=21),text(x+24,513,'右侧：'+calc,size=23),text(x+24,560,conclusion,c,25)])
 s.extend([text(30,634,'一致时，(2,1,0) 与 (1,0,1) 都能产生读数 (2,1,3)。',GRAY,22),text(30,670,'第三条只是汇总，仍无法区分这两份输入。',GRAY,22),'</g></svg>'])
 return ''.join(s)
if __name__=='__main__':
 (Path(__file__).resolve().parents[1]/'images/02-elimination-constraints.svg').write_text(svg(),encoding='utf-8')

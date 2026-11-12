# Generates the two figures for "The Mug, the Doughnut and the DAO".
# Usage: python3 docs/diagrams/the-mug-the-doughnut-and-the-dao.py images/the-mug-the-doughnut-and-the-dao
# Style notes: docs/diagram-style.md
import math
import sys, os
OUT=(sys.argv[1] if len(sys.argv)>1 else '.').rstrip('/')+'/'
BG='#F6F8FD'; DOT='#C8D2EC'; INK='#1F3FD1'; SOFT='#7D93E6'; F1='#FFFFFF'; F2='#E4EAFC'; F3='#C3D0F7'; F4='#9DB1F1'; ACC='#FF5A1F'
FONT='ui-monospace, SFMono-Regular, Menlo, Consolas, monospace'
def head(w,h,title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
<defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.3" fill="{DOT}"/></pattern></defs>
<rect width="{w}" height="{h}" fill="{BG}"/><rect width="{w}" height="{h}" fill="url(#dots)"/>
<text x="40" y="42" font-size="14" fill="{INK}" letter-spacing="2.5">{title}</text>
<path d="M40 54 H{w-40}" stroke="{INK}" stroke-width="1"/>
'''
def t(x,y,s,size=11,fill=INK,anchor='middle',ls=1.5,halo=True):
    h=f' stroke="{BG}" stroke-width="5" stroke-linejoin="round" paint-order="stroke"' if halo else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}"{h}>{s}</text>\n'
def ey(rx,ry,dx): return ry*math.sqrt(max(0,1-(dx/rx)**2))
def arrow_h(x1,x2,y,col=INK,dash=False):
    d=' stroke-dasharray="5 5"' if dash else ''
    return f'<path d="M{x1} {y} H{x2}" stroke="{col}" stroke-width="1.5"{d}/><path d="M{x2-9} {y-6} L{x2} {y} L{x2-9} {y+6}" fill="none" stroke="{col}" stroke-width="1.5"/>\n'

# ---------- FIG 1 ----------
W,H=1200,520; s=head(W,H,'FIG. 1 — SAME THING, DIFFERENT SHAPE')
SW='stroke="%s" stroke-width="1.5"'%INK
# mug
cx,ty,by,rx,ry=225,170,330,66,24
hx,hy=cx+rx+16,250
s+=f'<ellipse cx="{hx}" cy="{hy}" rx="38" ry="52" fill="{F3}" {SW}/>\n'
s+=f'<ellipse cx="{hx+6}" cy="{hy}" rx="17" ry="29" fill="{BG}" stroke="{ACC}" stroke-width="2"/>\n'
s+=f'<path d="M{cx-rx} {ty} V{by} A{rx} {ry} 0 0 0 {cx+rx} {by} V{ty} Z" fill="{F2}" {SW}/>\n'
dx=rx*0.45
s+=f'<path d="M{cx+dx:.1f} {ty+ey(rx,ry,dx):.1f} V{by+ey(rx,ry,dx):.1f} A{rx} {ry} 0 0 0 {cx+rx} {by} V{ty} A{rx} {ry} 0 0 1 {cx+dx:.1f} {ty+ey(rx,ry,dx):.1f} Z" fill="{F3}"/>\n'
s+=f'<path d="M{cx-rx} {ty} V{by} A{rx} {ry} 0 0 0 {cx+rx} {by} V{ty}" fill="none" {SW}/>\n'
s+=f'<ellipse cx="{cx}" cy="{ty}" rx="{rx}" ry="{ry}" fill="{F1}" {SW}/>\n'
s+=f'<ellipse cx="{cx}" cy="{ty+3}" rx="{rx-9}" ry="{ry-6}" fill="{F4}" stroke="{INK}" stroke-width="1"/>\n'
for i in range(5): s+=f'<path d="M{cx-rx+12+i*7} {ty+35+i*4} V{by-10}" stroke="{F1}" stroke-width="1" opacity=".7"/>\n'
# intermediate: torus + stub
c2,cy2,R,Ry=610,262,95,52
s+=f'<ellipse cx="{c2}" cy="{cy2}" rx="{R}" ry="{Ry}" fill="{F2}" {SW}/>\n'
s+=f'<path d="M{c2-R} {cy2} A{R} {Ry} 0 0 0 {c2+R} {cy2} A{R} {Ry*0.62:.1f} 0 0 1 {c2-R} {cy2} Z" fill="{F3}"/>\n'
s+=f'<ellipse cx="{c2}" cy="{cy2}" rx="{R}" ry="{Ry}" fill="none" {SW}/>\n'
hx2=c2+28
s+=f'<ellipse cx="{hx2}" cy="{cy2-4}" rx="34" ry="15" fill="{BG}" stroke="{ACC}" stroke-width="2"/>\n'
s+=f'<path d="M{hx2-34} {cy2-4} A34 15 0 0 1 {hx2+34} {cy2-4} A34 9 0 0 0 {hx2-34} {cy2-4} Z" fill="{F4}"/>\n'
sx,st,sb,srx,sry=c2-48,200,236,36,13
s+=f'<path d="M{sx-srx} {st} V{sb} A{srx} {sry} 0 0 0 {sx+srx} {sb} V{st} Z" fill="{F2}" {SW}/>\n'
s+=f'<ellipse cx="{sx}" cy="{st}" rx="{srx}" ry="{sry}" fill="{F1}" {SW}/>\n'
s+=f'<ellipse cx="{sx}" cy="{st+2}" rx="{srx-7}" ry="{sry-4}" fill="{F4}" stroke="{INK}" stroke-width="1"/>\n'
# doughnut
c3,cy3,R,Ry=980,262,128,66
s+=f'<ellipse cx="{c3}" cy="{cy3}" rx="{R}" ry="{Ry}" fill="{F2}" {SW}/>\n'
s+=f'<path d="M{c3-R} {cy3} A{R} {Ry} 0 0 0 {c3+R} {cy3} A{R} {Ry*0.6:.1f} 0 0 1 {c3-R} {cy3} Z" fill="{F3}"/>\n'
s+=f'<ellipse cx="{c3}" cy="{cy3}" rx="{R}" ry="{Ry}" fill="none" {SW}/>\n'
s+=f'<ellipse cx="{c3}" cy="{cy3-6}" rx="46" ry="19" fill="{BG}" stroke="{ACC}" stroke-width="2"/>\n'
s+=f'<path d="M{c3-46} {cy3-6} A46 19 0 0 1 {c3+46} {cy3-6} A46 11 0 0 0 {c3-46} {cy3-6} Z" fill="{F4}"/>\n'
s+=f'<path d="M{c3-80} {cy3-38} Q{c3-30} {cy3-58} {c3+30} {cy3-54}" fill="none" stroke="{F1}" stroke-width="3" stroke-linecap="round" opacity=".9"/>\n'
# arrows + labels
s+=arrow_h(385,455,262)+arrow_h(745,815,262)
s+=t(420,248,'STRETCH',10,SOFT)+t(780,248,'SQUASH',10,SOFT)
for (px,py,lx,ly) in [(hx+6,hy-29,hx+50,150),(hx2+20,cy2-15,hx2+60,165),(c3+20,cy3-22,c3+70,160)]:
    s+=f'<path d="M{px} {py} L{lx} {ly+6}" stroke="{ACC}" stroke-width="1"/><circle cx="{px}" cy="{py}" r="3" fill="{ACC}"/>\n'+t(lx+4,ly,'HOLE',10,ACC,'start')
for x,lab in [(240,'A. COFFEE MUG'),(610,'B. SOMEWHERE BETWEEN'),(980,'C. DOUGHNUT')]:
    s+=t(x,385,lab,12,INK)
s+=f'<path d="M150 412 V422 H1110 V412" fill="none" stroke="{INK}" stroke-width="1"/>\n'
s+=f'<rect x="330" y="440" width="540" height="30" fill="{INK}"/>'+t(600,460,'INVARIANT: ONE HOLE. NO TEARING, NO GLUING.',12,'#FFFFFF',halo=False)
s+=t(1160,505,'CC-BY Rufus Pollock · rufuspollock.com · openrevolution.net',10,SOFT,'end',1)
open(OUT+'mug-to-doughnut.svg','w').write(s+'</svg>\n')

# ---------- FIG 2 (isometric) ----------
W,H=1200,700; s=head(W,H,'FIG. 2 — AIRBNB IS A MARKET SQUARE')
SC=34
def P(o,x,y,z=0): return (o[0]+(x-y)*0.866*SC, o[1]+(x+y)*0.5*SC-z*SC)
def poly(pts,fill,stroke=INK,sw=1.2,extra=''):
    return '<path d="M'+' L'.join(f'{a:.1f} {b:.1f}' for a,b in pts)+f' Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"{extra}/>\n'
def box(o,x0,y0,x1,y1,z0,z1,top=F1,fx=F2,fy=F3):
    r=poly([P(o,x1,y0,z0),P(o,x1,y1,z0),P(o,x1,y1,z1),P(o,x1,y0,z1)],fx)
    r+=poly([P(o,x0,y1,z0),P(o,x1,y1,z0),P(o,x1,y1,z1),P(o,x0,y1,z1)],fy)
    r+=poly([P(o,x0,y0,z1),P(o,x1,y0,z1),P(o,x1,y1,z1),P(o,x0,y1,z1)],top); return r
def cyl(o,x,y,r,z0,z1,top=F1,side=F2):
    cx,cyb=P(o,x,y,z0); _,cyt=P(o,x,y,z1); rx=1.2247*r*SC; ry=0.7071*r*SC
    return (f'<path d="M{cx-rx:.1f} {cyt:.1f} V{cyb:.1f} A{rx:.1f} {ry:.1f} 0 0 0 {cx+rx:.1f} {cyb:.1f} V{cyt:.1f} Z" fill="{side}" stroke="{INK}" stroke-width="1.2"/>\n'
            f'<ellipse cx="{cx:.1f}" cy="{cyt:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{top}" stroke="{INK}" stroke-width="1.2"/>\n')
def person(o,x,y,ghost=False):
    op=' opacity="0.45"' if ghost else ''
    r=cyl(o,x,y,0.28,0,0.75,F2,F3)
    hx,hy=P(o,x,y,1.05); r+=f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{0.27*SC:.1f}" fill="{F1}" stroke="{INK}" stroke-width="1.2"/>\n'
    return f'<g{op}>{r}</g>\n'
def stall(o,x,y):
    r=box(o,x-0.7,y-0.45,x+0.7,y+0.45,0,0.6)
    for (a,b) in [(x-0.8,y-0.55),(x+0.8,y-0.55),(x+0.8,y+0.55),(x-0.8,y+0.55)]:
        p1=P(o,a,b,0.6);p2=P(o,a,b,1.25); r+=f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f}" stroke="{INK}" stroke-width="1.2"/>\n'
    r+=box(o,x-0.85,y-0.6,x+0.85,y+0.6,1.25,1.4,F1,F3,F4); return r
def house(o,x,y):
    x0,x1,y0,y1,h,hr,ym=x-0.7,x+0.7,y-0.55,y+0.55,0.8,1.5,y
    r=box(o,x0,y0,x1,y1,0,h)
    r+=poly([P(o,x0,y0,h),P(o,x1,y0,h),P(o,x1,ym,hr),P(o,x0,ym,hr)],F3)
    r+=poly([P(o,x0,y1,h),P(o,x1,y1,h),P(o,x1,ym,hr),P(o,x0,ym,hr)],F4)
    r+=poly([P(o,x1,y0,h),P(o,x1,y1,h),P(o,x1,ym,hr)],F2)
    d=[P(o,x1,y-0.15,0),P(o,x1,y+0.15,0),P(o,x1,y+0.15,0.45),P(o,x1,y-0.15,0.45)]; r+=poly(d,F4,INK,1); return r
def ground_curve(o,pts,col,dash=False,heads=(True,True)):
    d=' stroke-dasharray="5 5"' if dash else ''
    sp=[P(o,*p,0.02) for p in pts]
    r='<path d="M'+' L'.join(f'{a:.1f} {b:.1f}' for a,b in sp)+f'" fill="none" stroke="{col}" stroke-width="1.6"{d}/>\n'
    def head_at(a,b):
        ang=math.atan2(a[1]-b[1],a[0]-b[0]); L=10
        p1=(a[0]-L*math.cos(ang-0.45),a[1]-L*math.sin(ang-0.45)); p2=(a[0]-L*math.cos(ang+0.45),a[1]-L*math.sin(ang+0.45))
        return f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{a[0]:.1f} {a[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="1.6"/>\n'
    if heads[1]: r+=head_at(sp[-1],sp[-2])
    if heads[0]: r+=head_at(sp[0],sp[1])
    return r
def bez(a,c,b,n=24): return [((1-t)**2*a[0]+2*(1-t)*t*c[0]+t*t*b[0],(1-t)**2*a[1]+2*(1-t)*t*c[1]+t*t*b[1]) for t in [i/n for i in range(n+1)]]
def label(o,x,y,z,text,col=INK,dy=-46):
    a=P(o,x,y,z); b=(a[0],a[1]+dy)
    return f'<path d="M{a[0]:.1f} {a[1]:.1f} V{b[1]+4:.1f}" stroke="{col}" stroke-width="1" stroke-dasharray="2 3"/><circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="2.5" fill="{col}"/>\n'+t(b[0],b[1],text,11,col)
def ground_path(o,pts,col,dash=False,heads=(True,True)):
    d=' stroke-dasharray="5 5"' if dash else ''
    sp=[P(o,*p) for p in pts]
    r='<path d="M'+' L'.join(f'{a:.1f} {b:.1f}' for a,b in sp)+f'" fill="none" stroke="{col}" stroke-width="1.6"{d}/>\n'
    def head_at(a,b):
        ang=math.atan2(a[1]-b[1],a[0]-b[0]); L=10
        p1=(a[0]-L*math.cos(ang-0.45),a[1]-L*math.sin(ang-0.45)); p2=(a[0]-L*math.cos(ang+0.45),a[1]-L*math.sin(ang+0.45))
        return f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{a[0]:.1f} {a[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="1.6"/>\n'
    if heads[1]: r+=head_at(sp[-1],sp[-2])
    if heads[0]: r+=head_at(sp[0],sp[1])
    return r
def office(o,x,y,z):
    r=box(o,x-0.6,y-0.6,x+0.6,y+0.6,z,z+1.7)
    for k in range(3):
        for j in range(2):
            zz=z+0.35+k*0.45; yy=y-0.35+j*0.45
            r+=poly([P(o,x+0.6,yy,zz),P(o,x+0.6,yy+0.25,zz),P(o,x+0.6,yy+0.25,zz+0.25),P(o,x+0.6,yy,zz+0.25)],F4,INK,0.8)
    return r
def bigperson(o,x,y,z):
    r=cyl(o,x,y,0.34,z,z+1.0,F2,F3)
    hx,hy=P(o,x,y,z+1.35); r+=f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{0.33*SC:.1f}" fill="{F1}" stroke="{INK}" stroke-width="1.2"/>\n'
    return r
def panel(o,kind):
    T=0.45
    # the owned ground: a thick slab
    r=box(o,0,0,10,5,-T,0,'#EEF2FD',F2,F3)
    for i in range(1,10): a=P(o,i,0);b=P(o,i,5); r+=f'<path d="M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f}" stroke="{DOT}" stroke-width="1"/>\n'
    for j in range(1,5): a=P(o,0,j);b=P(o,10,j); r+=f'<path d="M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f}" stroke="{DOT}" stroke-width="1"/>\n'
    a,b,c,d=P(o,0,0),P(o,10,0),P(o,10,5),P(o,0,5)
    r+=f'<path d="M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f} L{c[0]:.1f} {c[1]:.1f} L{d[0]:.1f} {d[1]:.1f} Z" fill="none" stroke="{INK}" stroke-width="1.2"/>\n'
    # goods/money between the two sides, on the ground
    r+=ground_path(o,[(*q,0.02) for q in bez((2.6,2.6),(5.6,4.2),(8.5,2.9))],INK)
    # fee: from sellers, over the front edge, to the owner standing outside
    a=P(o,1.5,3.0,0.02); b=P(o,3.4,6.3,(2.05 if kind=='market' else 1.85)-T); c=(a[0]+5,b[1]-10)
    q=bez(a,c,b); r+='<path d="M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in q)+f'" fill="none" stroke="{ACC}" stroke-width="1.6"/>\n'
    ang=math.atan2(q[-1][1]-q[-2][1],q[-1][0]-q[-2][0]); L=10; e=q[-1]
    r+=f'<path d="M{e[0]-L*math.cos(ang-0.45):.1f} {e[1]-L*math.sin(ang-0.45):.1f} L{e[0]:.1f} {e[1]:.1f} L{e[0]-L*math.cos(ang+0.45):.1f} {e[1]-L*math.sin(ang+0.45):.1f}" fill="none" stroke="{ACC}" stroke-width="1.6"/>\n'
    if kind=='market':
        r+=stall(o,1.2,0.9); r+=stall(o,1.3,2.2); r+=stall(o,4.2,0.9)
    else:
        r+=house(o,1.2,0.9); r+=house(o,1.3,2.2); r+=house(o,4.2,0.9)
    r+=person(o,9.6,1.2,True)+person(o,8.8,2.3)
    if kind=='market': r+=bigperson(o,3.6,6.7,-T)
    else: r+=office(o,3.6,6.9,-T)
    names={'market':('STALLHOLDERS','SHOPPERS','PITCH FEE','GOODS ⇄ MONEY','MARKET OWNER','OWNS THE SQUARE'),
           'airbnb':('HOSTS (LISTINGS)','GUESTS','COMMISSION','ROOM ⇄ MONEY','AIRBNB','OWNS THE PLATFORM')}[kind]
    r+=label(o,1.3,0.9,1.5,names[0],INK,-40)
    r+=label(o,8.8,2.3,1.35,names[1],INK,-40)
    r+=t(a[0]-6,(a[1]+b[1])/2+4,names[2],10,ACC,'end')
    a=P(o,5.6,4.0); r+=t(a[0]+10,a[1]+18,names[3],11,INK,'start')
    a=P(o,3.6,6.7 if kind=='market' else 6.9,-T); r+=t(a[0],a[1]+(30 if kind=='market' else 40),names[4],11,INK)
    # bracket showing ownership of the slab's front edge
    e1=P(o,0,5.25,-T); e2=P(o,10,5.25,-T)
    k1=P(o,0,5.45,-T); k2=P(o,10,5.45,-T)
    r+=f'<path d="M{e1[0]:.1f} {e1[1]:.1f} L{k1[0]:.1f} {k1[1]:.1f} L{k2[0]:.1f} {k2[1]:.1f} L{e2[0]:.1f} {e2[1]:.1f}" fill="none" stroke="{SOFT}" stroke-width="1"/>\n'
    m=P(o,8.2,5.45,-T); r+=t(m[0]-4,m[1]+22,names[5],10,SOFT,'end')
    return r
oA=(250,190); oB=(850,190)
s+=t(65,100,'A. MARKET SQUARE, c. 1300',12,SOFT,'start')+t(665,100,'B. AIRBNB, 2008',12,SOFT,'start')
s+=panel(oA,'market')+panel(oB,'airbnb')
s+=f'<g stroke="{ACC}" stroke-width="2.5" fill="none"><path d="M584 280 q8 -9 16 0 t16 0"/><path d="M584 294 H616 M584 306 H616"/></g>\n'
# table
y0=508; s+=f'<rect x="40" y="{y0}" width="1120" height="160" fill="#FFFFFF" stroke="{INK}" stroke-width="1"/>\n'
s+=f'<rect x="40" y="{y0}" width="1120" height="32" fill="{INK}"/>\n'
s+=f'<path d="M40 {y0+64} H1160 M40 {y0+96} H1160 M40 {y0+128} H1160 M400 {y0} V{y0+160} M780 {y0} V{y0+160}" stroke="{F3}" stroke-width="1"/>\n'
for x,v in [(56,'INVARIANT'),(416,'MARKET SQUARE'),(796,'AIRBNB')]: s+=t(x,y0+21,v,12,'#FFFFFF','start',2,halo=False)
for i,(a,b,c) in enumerate([('SIDES','2: sellers, buyers','2: hosts, guests'),('WHO OWNS THE GROUND','the market owner','Airbnb'),('WHO PAYS THE OWNER','sellers (pitch fee)','mostly hosts (commission)'),('OWNER PROVIDES','order, trust, a place to meet','reviews, search, payments')]):
    yy=y0+54+i*32; s+=t(56,yy,a,12,INK,'start',1,halo=False)+t(416,yy,b,12,INK,'start',0.5,halo=False)+t(796,yy,c,12,INK,'start',0.5,halo=False)
s+=t(1160,688,'CC-BY Rufus Pollock · rufuspollock.com · openrevolution.net',10,SOFT,'end',1)
open(OUT+'airbnb-market-square.svg','w').write(s+'</svg>\n')

import json,os,sys,urllib.request as R
U=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33);KG=(-17,-16,-15,-1,1,15,16,17);DG=(-17,-15,15,17);RT=(-16,-1,1,16)
A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
T=[(A.index(c)-32)*2 for c in "ggggjllWjdbggggqjjltllqv5555ggggHMRRMWgjRjloRgoqRjoqRgloMWggHMRRWbbbbjggblllbgllbjjlbgjlbgggWbbbgggjdgggdgggdgggdgggdgggjlllggggWbbdbgjgbjjjggjjdgjjbgjjbgggWbbdqvlgqqggbWWWWRRMRMMHRMMHRMMHRMMH"]
B=[0]*128;C=[0];KL={};CR=[0];EP=[-1];WK=[0];BK=[0];BM=[0]
SQ=[s for s in range(128)if s&136==0]
P=[0]*1664
for p in range(1,7):
 for s in SQ:
  f=min(s&7,7-(s&7));r=s>>4;P[(p+6)*128+s]=V[p]+T[(p-1)*32+r*4+f];P[(6-p)*128+s]=-V[p]-T[(p-1)*32+(7-r)*4+f]
LM=60000
class X(Exception):pass
def atk(s,w):
 p=1 if w else-1
 for v,oo in((1,(-15,-17)if w else(15,17)),(2,KN),(6,KG)):
  for o in oo:
   t=s+o
   if t&136==0 and B[t]==v*p:return 1
 for d in DG+RT:
  t=s+d
  while t&136==0:
   x=B[t]
   if x:
    if x*p>0 and(abs(x)==5 or abs(x)==3+(d in RT)):return 1
    break
   t+=d
 return 0
def pu(mv,s,t):
 if abs(B[s])==1 and t>>4 in(0,7):
  for q in(5,2,4,3):mv.append(s|(t<<7)|(q<<14))
 else:mv.append(s|(t<<7))
def gen(w):
 mv=[]
 for s in SQ:
  p=B[s]
  if p==0 or(p>0)!=w:continue
  a=abs(p)
  if a==1:
   d=16 if w else-16
   for o in(d,d-1,d+1):
    f=s+o
    if f&136:continue
    if o==d:
     if B[f]==0:
      pu(mv,s,f)
      if(s>>4)==(1 if w else 6)and B[s+2*d]==0:mv.append(s|((s+2*d)<<7))
    elif B[f]and(B[f]>0)!=w:pu(mv,s,f)
    elif f==EP[0]:mv.append(s|(f<<7))
  elif a==2 or a==6:
   for o in KN if a==2 else KG:
    f=s+o
    if f&136==0 and(B[f]==0 or(B[f]>0)!=w):mv.append(s|(f<<7))
  else:
   for d in DG if a==3 else RT if a==4 else DG+RT:
    f=s+d
    while f&136==0 and B[f]==0:mv.append(s|(f<<7));f+=d
    if f&136==0 and(B[f]>0)!=w:mv.append(s|(f<<7))
 for kf,rf,kt,bt in((4,7,6,1),(4,0,2,2),(116,119,118,4),(116,112,114,8)):
  if(kf<16)==w and CR[0]&bt and not any(B[x] for x in range(min(kf,rf)+1,max(kf,rf))):
   st=1 if kt>kf else-1
   if all(atk(x,not w)==0 for x in(kf,kf+st,kt)):mv.append(kf|(kt<<7))
 return mv
def val(w):
 s=0;wb=0;bb=0
 for q in SQ:
  p=B[q]
  if p:
   if p==3:wb+=1
   elif p==-3:bb+=1
   s+=P[(p+6)*128+q]
 s+=30*(wb>1);s-=30*(bb>1)
 return s if w else-s
def sco(m,pl):
 t=m>>7&127;v=B[t]
 if v or m>>14:return 10000+V[abs(v)]*10+(9000 if m>>14 else 0)-V[abs(B[m&127])]
 return 5000 if m in KL.get(pl,()) else 0
def sr(w,d,a,be,pl):
 C[0]+=1
 if C[0]>LM:raise X
 ck=atk(WK[0] if w else BK[0],not w)
 if d<=0:
  s=val(w)
  if s>=be:return be
  if s>a:a=s
 elif ck:d+=1
 mv=gen(w);mv.sort(key=lambda m:sco(m,pl),reverse=True);best=-30000;bm=0
 for m in mv:
  if d<=0 and ck==0 and B[m>>7&127]==0 and m>>14==0:
   if abs(B[m&127])!=1 or(m&7)==((m>>7)&7)or(m>>7&127)!=EP[0]:continue
  f=m&127;t=m>>7&127;p=m>>14;pc=B[f];cp=B[t]
  sv=B[:]+[CR[0],EP[0],WK[0],BK[0]]
  if abs(pc)==1 and t==EP[0] and cp==0:B[t-16 if w else t+16]=0
  if abs(pc)==6 and abs(t-f)==2:
   a=(112 if not w else 0)+(7 if t>f else 0);b=a-2 if t>f else a+3;B[b]=B[a];B[a]=0
  B[f]=0;B[t]=(p if w else-p)if p else pc
  if abs(pc)==6:(WK if w else BK)[0]=t
  if abs(pc)==6:CR[0]&=12 if w else 3
  for q,mm in((7,1),(0,2),(119,4),(112,8)):
   if f==q or t==q:CR[0]&=~mm
  EP[0]=(f+t)//2 if abs(pc)==1 and abs(t-f)==32 else-1
  if atk(WK[0] if w else BK[0],not w):
   B[:]=sv[:128];CR[0],EP[0],WK[0],BK[0]=sv[128:];continue
  s=-sr(not w,d-1,-be,-a,pl+1)
  B[:]=sv[:128];CR[0],EP[0],WK[0],BK[0]=sv[128:]
  if s>best:
   best=s;bm=m
   if pl==0:BM[0]=m
   if s>a:a=s
   if a>=be:
    if d>0 and B[m>>7&127]==0 and m>>14==0:
     k=KL.setdefault(pl,[0,0]);k[1]=k[0];k[0]=m
    break
 if best==-30000:return -29999+pl if ck else(0 if d>0 else a)
 return best if d>0 else a
def ps(fen):
 b=[0]*128;sp=fen.split();s=0
 for c in sp[0]:
  if c.isdigit():s+=int(c)
  elif c!="/":b[(7-s//8)*16+s%8]=("PNBRQK".index(c.upper())+1)*(1 if c.isupper() else-1);s+=1
 w=sp[1]=="w";ep=-1
 if sp[3]!="-":ep=ord(sp[3][0])-97+(int(sp[3][1])-1)*16
 return b,w,sp[2],ep
def uc(m):
 f=m&127;t=m>>7&127;p=m>>14
 return"%c%d%c%d%s"%(97+(f&7),(f>>4)+1,97+(t&7),(t>>4)+1,"nbrq"[p-2]if p else"")
def ch(fen,legal):
 b,w,ca,ep=ps(fen)
 B[:]=b
 CR[0]=sum(1<<i for i,c in enumerate("KQkq")if c in ca)
 EP[0]=ep
 WK[0]=B.index(6);BK[0]=B.index(-6)
 C[0]=0;BM[0]=0
 od=gen(w)
 if len(od)==1:return uc(od[0])
 od.sort(key=lambda m:sco(m,0),reverse=True);best=0
 try:
  d=1
  while C[0]<LM:
   sr(w,d,-30000,30000,0)
   if BM[0]:
    best=BM[0];od.remove(best);od.insert(0,best)
   d+=1
 except X:pass
 if best==0:best=od[0]
 u=uc(best)
 return u if u in legal else legal[0]
def pt(p,bo):
 r=R.Request(U+p,data=json.dumps(bo).encode(),headers={"content-type":"application/json"})
 try:
  with R.urlopen(r)as s:return json.load(s)
 except Exception:sys.exit(1)
while True:
 g=pt("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  try:mv=ch(g["fen"],g["legal_moves"])
  except Exception:mv=g["legal_moves"][0]
  g=pt("/move",{"game":g["game"],"move":mv})

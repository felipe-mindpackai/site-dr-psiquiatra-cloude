from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont
import pathlib
W,H=3240,4050
base=pathlib.Path("social")
out=pathlib.Path("mosaico-v1-minimal"); out.mkdir(exist_ok=True)

# re-render v1 master fresh from its HTML
url=(base/"mosaico-denner-master.html").resolve().as_uri()
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":W,"height":H},device_scale_factor=1)
    pg.goto(url); pg.wait_for_timeout(1800)
    pg.screenshot(path=str(out/"mosaico-v1-master.png"),clip={"x":0,"y":0,"width":W,"height":H})
    b.close()

m=Image.open(out/"mosaico-v1-master.png").convert("RGB")
m.resize((1080,1350),Image.LANCZOS).save(out/"PREVIEW-v1-limpo.jpg",quality=92)

# slice 9 tiles
cw,ch=W//3,H//3; n=1
for r in range(3):
    for c in range(3):
        m.crop((c*cw,r*ch,(c+1)*cw,(r+1)*ch)).save(out/f"tile-{n}.jpg",quality=95,subsampling=0); n+=1

# numbered guide
tw,th,gut,pad,header,footer=360,450,18,70,150,170
gridw,gridh=tw*3+gut*2,th*3+gut*2
GW=gridw+pad*2; GH=header+gridh+footer+pad
NAVY=(18,38,58);GOLD=(176,141,87);PAPER=(251,250,247);WHITE=(255,255,255)
img=Image.new("RGB",(GW,GH),PAPER);d=ImageDraw.Draw(img)
def fnt(s,b=True):
    for nm in (["arialbd.ttf"] if b else ["arial.ttf"]):
        try:return ImageFont.truetype(nm,s)
        except:pass
    return ImageFont.load_default()
def ct(cx,y,t,f,fill,ls=0):
    if ls:
        tot=sum(d.textlength(c,font=f)+ls for c in t)-ls;x=cx-tot/2
        for c in t:d.text((x,y),c,font=f,fill=fill,anchor="lm");x+=d.textlength(c,font=f)+ls
    else:d.text((cx,y),t,font=f,fill=fill,anchor="mm")
ct(GW//2,pad+30,"GUIA DE POSTAGEM - MOSAICO V1 (MINIMAL)",fnt(38),NAVY,ls=2)
ct(GW//2,pad+90,"como o grid fica no seu perfil  (1080 x 1350 cada)",fnt(26,False),(90,108,124))
gx0,gy0=pad,pad+header
for i in range(9):
    r,c=divmod(i,3);x=gx0+c*(tw+gut);y=gy0+r*(th+gut)
    t=Image.open(out/f"tile-{i+1}.jpg").resize((tw,th),Image.LANCZOS);img.paste(t,(x,y))
    d.rectangle([x,y,x+tw-1,y+th-1],outline=WHITE,width=6)
    d.rectangle([x+14,y+14,x+100,y+100],fill=NAVY)
    d.text((x+57,y+57),str(i+1),font=fnt(54),fill=WHITE,anchor="mm")
fy=gy0+gridh+60
ct(GW//2,fy,"ORDEM DE POSTAGEM  (publique de tras pra frente)",fnt(30),GOLD,ls=1)
ct(GW//2,fy+58,"9  >  8  >  7  >  6  >  5  >  4  >  3  >  2  >  1",fnt(46),NAVY,ls=4)
ct(GW//2,fy+110,"o tile 1 e o ULTIMO a postar  (fica no topo-esquerda)",fnt(24,False),(90,108,124))
img.save(out/"GUIA-postagem.png")
print("v1 recriado em:", out.resolve())

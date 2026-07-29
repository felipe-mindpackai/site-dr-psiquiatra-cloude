from PIL import Image, ImageDraw, ImageFont
import pathlib
out = pathlib.Path("social")

# small thumbs from tiles
tw, th = 360, 450          # thumb size (4:5)
gut = 18                   # gutter
pad = 70                   # outer padding
header = 150
footer = 170
gridw = tw*3 + gut*2
gridh = th*3 + gut*2
W = gridw + pad*2
H = header + gridh + footer + pad

NAVY=(18,38,58); GOLD=(176,141,87); PAPER=(251,250,247); WHITE=(255,255,255)
img = Image.new("RGB",(W,H),PAPER)
d = ImageDraw.Draw(img)

def font(sz,bold=True):
    for n in (["arialbd.ttf","Arialbd.ttf"] if bold else ["arial.ttf"]):
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()

def ctext(cx,y,txt,fnt,fill,anchor="mm",ls=0):
    if ls:
        # manual letter spacing
        widths=[d.textlength(c,font=fnt)+ls for c in txt]
        total=sum(widths)-ls
        x=cx-total/2
        for c in txt:
            d.text((x,y),c,font=fnt,fill=fill,anchor="lm")
            x+=d.textlength(c,font=fnt)+ls
    else:
        d.text((cx,y),txt,font=fnt,fill=fill,anchor=anchor)

# header
ctext(W//2, pad+30, "GUIA DE POSTAGEM — MOSAICO DR. DENNER", font(40), NAVY, ls=2)
ctext(W//2, pad+90, "como o grid fica no seu perfil  (1080 x 1350 cada)", font(26,False), (90,108,124))

gx0 = pad; gy0 = pad+header
for i in range(9):
    r,c = divmod(i,3)
    x = gx0 + c*(tw+gut); y = gy0 + r*(th+gut)
    t = Image.open(out/f"tile-{i+1}.jpg").resize((tw,th), Image.LANCZOS)
    img.paste(t,(x,y))
    d.rectangle([x,y,x+tw-1,y+th-1], outline=WHITE, width=6)
    # number badge
    bw=86
    d.rectangle([x+14,y+14,x+14+bw,y+14+bw], fill=NAVY)
    d.text((x+14+bw/2, y+14+bw/2), str(i+1), font=font(54), fill=WHITE, anchor="mm")

# footer: posting order
fy = gy0 + gridh + 60
ctext(W//2, fy, "ORDEM DE POSTAGEM  (publique de tras pra frente)", font(30), GOLD, ls=1)
ctext(W//2, fy+58, "9  ›  8  ›  7  ›  6  ›  5  ›  4  ›  3  ›  2  ›  1", font(46), NAVY, ls=4)
ctext(W//2, fy+110, "o tile 1 e o ULTIMO a postar  (fica no topo-esquerda)", font(24,False), (90,108,124))

img.save(out/"GUIA-postagem.png")
print("saved", img.size)

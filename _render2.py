from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
import pathlib
W,H=3240,4050
out=pathlib.Path("social")
url=(out/"mosaico-denner-v2.html").resolve().as_uri()
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":W,"height":H},device_scale_factor=1)
    pg.goto(url); pg.wait_for_timeout(1800)
    pg.screenshot(path=str(out/"mosaico-denner-v2-master.png"),clip={"x":0,"y":0,"width":W,"height":H})
    b.close()
m=Image.open(out/"mosaico-denner-v2-master.png").convert("RGB")
m.resize((1080,1350),Image.LANCZOS).save(out/"PREVIEW-v2-limpo.jpg",quality=92)
ov=m.copy(); d=ImageDraw.Draw(ov,"RGBA"); g=14
for i in (1,2):
    x=W*i//3; d.rectangle([x-g,0,x+g,H],fill=(255,255,255,235))
    y=H*i//3; d.rectangle([0,y-g,W,y+g],fill=(255,255,255,235))
ov.resize((1080,1350),Image.LANCZOS).save(out/"PREVIEW-v2-grid.jpg",quality=92)
print("done")

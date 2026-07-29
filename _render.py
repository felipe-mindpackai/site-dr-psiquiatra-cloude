from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
import pathlib

W,H = 3240,4050
out = pathlib.Path("social")
url = (out/"mosaico-denner-master.html").resolve().as_uri()

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":W,"height":H}, device_scale_factor=1)
    pg.goto(url)
    pg.wait_for_timeout(1800)  # fonts/images
    pg.screenshot(path=str(out/"mosaico-denner-master.png"), clip={"x":0,"y":0,"width":W,"height":H})
    b.close()

# clean downscaled preview
master = Image.open(out/"mosaico-denner-master.png").convert("RGB")
master.resize((1080,1350), Image.LANCZOS).save(out/"PREVIEW-mosaico-limpo.jpg", quality=92)

# grid-overlay preview: gutters + cut lines to simulate IG grid
ov = master.copy()
d = ImageDraw.Draw(ov,"RGBA")
gut = 14
for i in (1,2):
    x = W*i//3
    d.rectangle([x-gut, 0, x+gut, H], fill=(255,255,255,235))
    y = H*i//3
    d.rectangle([0, y-gut, W, y+gut], fill=(255,255,255,235))
ov.resize((1080,1350), Image.LANCZOS).save(out/"PREVIEW-mosaico-grid.jpg", quality=92)
print("done", master.size)

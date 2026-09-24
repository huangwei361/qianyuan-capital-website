"""把 P.12 渲染成图片对比看问题"""
import pypdfium2 as pdfium, sys
sys.stdout.reconfigure(encoding='utf-8')

PDF = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v8.pdf'
OUT = r'C:\Users\64549\.minimax\金融财富公司成立\website\_preview-p12-v8.png'

pdf = pdfium.PdfDocument(PDF)
page = pdf[11]  # 0-indexed, P.12 = index 11
bitmap = page.render(scale=1.5)
pil_image = bitmap.to_pil()
pil_image.save(OUT)
print(f'Saved: {OUT}')
print(f'Size: {pil_image.size}')
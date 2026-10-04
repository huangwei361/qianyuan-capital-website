"""渲染 P.9 和 P.10 看效果"""
import pypdfium2 as pdfium, sys
sys.stdout.reconfigure(encoding='utf-8')

PDF = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v9.pdf'

pdf = pdfium.PdfDocument(PDF)
for idx, name in [(8, 'p9-cases'), (9, 'p10-skill')]:
    page = pdf[idx]
    bitmap = page.render(scale=1.5)
    img = bitmap.to_pil()
    out = rf'C:\Users\64549\.minimax\金融财富公司成立\website\_preview-{name}.png'
    img.save(out)
    print(f'Saved: {out} ({img.size})')
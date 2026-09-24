import pdfplumber, os
f = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v5.pdf'
with pdfplumber.open(f) as pdf:
    print(f'Pages: {len(pdf.pages)}')
    print(f'Size: {os.path.getsize(f)/1024:.0f} KB')
    print()
    # 重点看 P5（信条页）
    p5 = pdf.pages[4] if len(pdf.pages) >= 5 else None
    if p5:
        text = p5.extract_text() or ''
        print(f'P5 ({len(text)} chars):')
        print(text[:800])
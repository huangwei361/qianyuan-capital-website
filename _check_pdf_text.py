import pdfplumber
f = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v2.pdf'
with pdfplumber.open(f) as pdf:
    print(f'Pages: {len(pdf.pages)}')
    print(f'Size: {__import__("os").path.getsize(f)} bytes')
    print()
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ''
        title = text.split('\n')[0] if text else '(empty)'
        print(f'P{i+1}: {len(text)} chars | {title[:50]}')
import pdfplumber, os, sys
sys.stdout.reconfigure(encoding='utf-8')
f = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v6.pdf'
with pdfplumber.open(f) as pdf:
    print(f'Pages: {len(pdf.pages)}')
    print(f'Size: {os.path.getsize(f)/1024:.0f} KB')
    print()
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ''
        title = text.split('\n')[0] if text else '(empty)'
        print(f'P{i+1}: {len(text):>4} chars | {title[:60]}')
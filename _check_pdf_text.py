import pdfplumber
with pdfplumber.open(r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure.pdf') as pdf:
    print(f'Pages: {len(pdf.pages)}')
    for i, page in enumerate(pdf.pages[:3]):
        text = page.extract_text() or ''
        print(f'\n--- Page {i+1} (len={len(text)}) ---')
        print(text[:300])
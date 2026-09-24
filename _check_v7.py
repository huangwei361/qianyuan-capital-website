"""验证 PDF v7 的页数和每页内容"""
import pdfplumber, sys
sys.stdout.reconfigure(encoding='utf-8')

with pdfplumber.open(r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v7.pdf') as pdf:
    print(f'总页数: {len(pdf.pages)}')
    print()
    for i, page in enumerate(pdf.pages, 1):
        text = page.extract_text() or ''
        text = text.strip().replace('\n', ' / ')
        # 取每页前 80 字符
        snippet = text[:80] if text else '(空)'
        print(f'--- P.{i:02d} (共 {len(text)} 字符) ---')
        print(f'    {snippet}')
        print()
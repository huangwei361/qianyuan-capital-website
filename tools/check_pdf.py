import os
f = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure.pdf'
data = open(f, 'rb').read()
print(f'Size: {len(data)} bytes ({len(data)/1024:.1f} KB)')
print(f'Pages: {data.count(b"/Type /Page")}')
kw = '乾元'.encode('utf-8')
print(f'Has 乾元: {kw in data}')
kw2 = 'BUSINESS BROCHURE'.encode('utf-8')
print(f'Has BUSINESS BROCHURE: {kw2 in data}')
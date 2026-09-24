import shutil, os
src = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v8.pdf'
dst = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure.pdf'
shutil.move(src, dst)
print(f'OK: {os.path.getsize(dst)} bytes')
import os, shutil
src = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v9.pdf'
dst = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure.pdf'

# 检查谁在锁
try:
    import psutil
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for f in proc.open_files() or []:
                if f.path.lower() == dst.lower():
                    print(f'Killing PID {proc.info["pid"]} ({proc.info["name"]})')
                    proc.kill()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
except ImportError:
    pass

if os.path.exists(dst):
    try:
        os.remove(dst)
    except PermissionError:
        print('Still locked. Waiting 2s...')
        import time
        time.sleep(2)
        os.remove(dst)
shutil.move(src, dst)
print(f'Final: {os.path.getsize(dst)} bytes')
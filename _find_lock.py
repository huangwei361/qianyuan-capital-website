"""用 psutil 找占用 PDF 的进程"""
import os, subprocess
# 用 handle.exe 或 openfiles 找占用
target = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure.pdf'

# 尝试 openfiles 命令（需要管理员），不行就用 psutil 扫进程
try:
    import psutil
    found = []
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            files = proc.info['open_files'] or []
            for f in files:
                if f.path.lower() == target.lower():
                    found.append((proc.info['pid'], proc.info['name'], f.path))
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    if found:
        for pid, name, path in found:
            print(f'LOCKED BY: pid={pid} name={name}')
            print(f'  Path: {path}')
    else:
        print('No process is locking the file via psutil')
        # 试一下重启 explorer 或看是否有 Sysinternals
        print('Possibly a Windows handle cache. Try waiting 30s.')
except ImportError:
    print('psutil not available')
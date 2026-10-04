"""验证 HTML 里所有相对路径资源都能 200"""
import re, sys
from pathlib import Path
import urllib.request, urllib.error
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r'C:\Users\64549\.minimax\金融财富公司成立\website')
BASE = 'http://localhost:8000'

all_html = sorted(ROOT.rglob('*.html'))
total_links = 0
total_errors = 0

for html in all_html:
    rel = html.relative_to(ROOT)
    # HTML 在 server 上的 URL 路径
    url_path = '/' + str(rel).replace('\\', '/')
    src_url = BASE + url_path

    # 读取 HTML
    content = html.read_text(encoding='utf-8')

    # 提取 href 和 src 里的本地文件引用
    pattern = re.compile(r'(?:href|src)="([^"]+)"')
    file_links = set()
    for m in pattern.finditer(content):
        link = m.group(1)
        # 跳过外部 / 锚点 / 协议
        if link.startswith(('http://', 'https://', '#', 'mailto:', 'tel:', 'data:', 'javascript:')):
            continue
        if not link:
            continue
        # 跳过纯锚点链接（如 #section）
        if link.startswith('#'):
            continue
        file_links.add(link)

    print(f'\n[{rel}] {len(file_links)} unique links:')
    for link in sorted(file_links):
        total_links += 1
        # 解析相对路径
        # HTML 在 server 上的目录
        html_dir = url_path.rsplit('/', 1)[0]
        if html_dir.endswith('/' + html.name):
            html_dir = html_dir[:-len(html.name)]
        # link 是相对于 HTML 文件的（不是相对于它的 URL）
        # 比如 HTML 在 /invest/index.html，引 "../index.html"
        # 我们要从 HTML 所在的文件系统目录算
        html_fs_dir = str(rel.parent).replace('\\', '/')
        if html_fs_dir == '.':
            html_fs_dir = ''

        # link 是相对路径，用文件系统方式解析
        target_fs = (ROOT / html_fs_dir / link).resolve()
        # 转成 URL 路径
        try:
            target_rel = target_fs.relative_to(ROOT)
            target_url = BASE + '/' + str(target_rel).replace('\\', '/')
        except ValueError:
            print(f'  ERR  {link}  (无法解析)')
            total_errors += 1
            continue

        try:
            req = urllib.request.Request(target_url, method='HEAD')
            resp = urllib.request.urlopen(req, timeout=5)
            status = resp.status
        except urllib.error.HTTPError as e:
            status = e.code
        except Exception as e:
            status = f'ERR: {e}'

        marker = 'OK ' if status == 200 else 'ERR'
        if status != 200:
            total_errors += 1
        print(f'  {marker} {status:>3}  {link} -> {target_url.replace(BASE, "")}')

print()
print(f'=== Total: {total_links} links, {total_errors} errors ===')
sys.exit(0 if total_errors == 0 else 1)
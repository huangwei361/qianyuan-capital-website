"""website/ 按 1+5 架构拆分子目录"""
import os, shutil, re
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r'C:\Users\64549\.minimax\金融财富公司成立\website')

# ============ 1. 文件移动映射（src -> dest，相对 ROOT）============
HTML_MOVES = {
    # 投融资规划和管理（顶级集群 + 子集群 + 下挂）
    'invest.html': 'invest/index.html',
    'invest-plan.html': 'invest/plan.html',
    'invest-brochure.html': 'invest/brochure.html',
    'qifu.html': 'invest/qifu/index.html',
    'asset.html': 'invest/asset/index.html',
    # 黄金
    'gold.html': 'gold/index.html',
    'gold-dashboard.html': 'gold/dashboard.html',
    # 出海
    'global.html': 'global/index.html',
    'global-shop.html': 'global/shop.html',
    # 量化
    'quant.html': 'quant/index.html',
    'quant-trading.html': 'quant/trading.html',
    'quant-rd.html': 'quant/rd.html',
    # 租赁
    'rental.html': 'rental/index.html',
}

CSS_MOVES = {
    'quant-rd.css': 'quant/rd.css',
    'quant-trading.css': 'quant/trading.css',
    # _sub.css 留根
}

TOOL_FILES = [
    'check_pdf', 'check_pdf_text', 'check_table', 'check_v7',
    'clean', 'find_lock', 'fix_table', 'fix_table2', 'fix_v7',
    'gen', 'gen_docx', 'gen_pdf', 'make_poster', 'md2docx',
    'preview_p910', 'preview_rd', 'publish', 'publish_v9',
    'render_p12', 'restructure', 'verify',
]

# ============ 2. 链接映射（旧名 -> 新相对 ROOT 路径）============
LINK_RENAMES = {
    '_sub.css': '_sub.css',                    # 留根
    'index.html': 'index.html',                # 主站留根
    'gold.html': 'gold/index.html',
    'gold-dashboard.html': 'gold/dashboard.html',
    'global.html': 'global/index.html',
    'global-shop.html': 'global/shop.html',
    'quant.html': 'quant/index.html',
    'quant-trading.html': 'quant/trading.html',
    'quant-rd.html': 'quant/rd.html',
    'invest.html': 'invest/index.html',
    'invest-plan.html': 'invest/plan.html',
    'invest-brochure.html': 'invest/brochure.html',
    'qifu.html': 'invest/qifu/index.html',
    'asset.html': 'invest/asset/index.html',
    'rental.html': 'rental/index.html',
}


def compute_relative(source_dir, target_path):
    """从 source_dir (相对 ROOT) 到 target_path (相对 ROOT) 的相对路径"""
    src_parts = source_dir.replace('\\', '/').split('/') if source_dir else []
    tgt_full = target_path.replace('\\', '/')
    tgt_dir = str(Path(tgt_full).parent).replace('\\', '/')
    tgt_parts = tgt_dir.split('/') if tgt_dir != '.' else []
    tgt_name = Path(tgt_full).name

    # 公共前缀
    common = 0
    for s, t in zip(src_parts, tgt_parts):
        if s == t:
            common += 1
        else:
            break

    up = len(src_parts) - common
    down = tgt_parts[common:]

    prefix = '../' * up
    if down:
        return prefix + '/'.join(down) + '/' + tgt_name
    else:
        return prefix + tgt_name


def process_html(html_path):
    """替换 HTML 文件里的链接"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    rel = html_path.relative_to(ROOT)
    src_dir = str(rel.parent).replace('\\', '/')
    if src_dir == '.':
        src_dir = ''

    changes = 0
    log = []

    def replace_link(match):
        nonlocal changes
        attr = match.group(1)
        old_path = match.group(2)

        # 跳过外部 URL / 锚点 / 特殊协议
        if old_path.startswith(('http://', 'https://', '#', 'mailto:', 'tel:', 'data:', 'javascript:')):
            return match.group(0)
        if not old_path:
            return match.group(0)
        # 已经是相对路径的（含 ../ 或 ./）跳过（理论上不该有）
        if old_path.startswith(('./', '../')):
            return match.group(0)

        # 查纯文件名
        basename = Path(old_path).name

        if basename in LINK_RENAMES:
            new_target = LINK_RENAMES[basename]
            # 计算相对路径
            new_link = compute_relative(src_dir, new_target)

            # 如果是自身链接（指向自己当前所在文件的"新位置"）
            # 比如 quant.html 里引 quant.html（自己），分目录后 quant/index.html 引自己 = index.html
            # 但 quant.html 引 quant.html 的实际是 "📊 总览" 链接，指向 quant 集群入口
            # 分目录后 quant 集群入口就是 quant/index.html，自己 = index.html → 指向自己
            # 所以这种链接保持指向自己即可
            if old_path == basename:
                # 旧链接是纯文件名（不带目录前缀），需要看是否是自身
                # 检查：自身 = 当前 HTML 文件对应的新位置
                current_new_pos = str(rel).replace('\\', '/')
                if new_target == current_new_pos:
                    # 指向自己 → 用 ./ 或 index.html
                    new_link = 'index.html'

            changes += 1
            log.append(f'  {old_path} -> {new_link}')
            return f'{attr}="{new_link}"'
        return match.group(0)

    pattern = re.compile(r'(href|src)="([^"]+)"')
    new_content = pattern.sub(replace_link, content)

    if changes > 0:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes, log


def main():
    print('=== 1. 创建子目录 ===')
    for dest in HTML_MOVES.values():
        Path(ROOT / dest).parent.mkdir(parents=True, exist_ok=True)
        print(f'  MKDIR: {Path(ROOT / dest).parent.relative_to(ROOT)}')
    for dest in CSS_MOVES.values():
        Path(ROOT / dest).parent.mkdir(parents=True, exist_ok=True)
    Path(ROOT / 'tools').mkdir(exist_ok=True)
    print(f'  MKDIR: tools')

    print()
    print('=== 2. 移动 HTML ===')
    for src, dest in HTML_MOVES.items():
        src_path = ROOT / src
        dest_path = ROOT / dest
        if src_path.exists():
            shutil.move(str(src_path), str(dest_path))
            print(f'  MOVE: {src} -> {dest}')

    print()
    print('=== 3. 移动 CSS ===')
    for src, dest in CSS_MOVES.items():
        src_path = ROOT / src
        dest_path = ROOT / dest
        if src_path.exists():
            shutil.move(str(src_path), str(dest_path))
            print(f'  MOVE: {src} -> {dest}')

    print()
    print('=== 4. 移动工具脚本到 tools/ ===')
    for name in TOOL_FILES:
        src_path = ROOT / f'_{name}.py'
        dest_path = ROOT / 'tools' / f'{name}.py'
        if src_path.exists():
            shutil.move(str(src_path), str(dest_path))
            print(f'  MOVE: _{name}.py -> tools/{name}.py')

    # 删除 _commit_msg.txt 等临时文件（这些不应该到 GitHub）
    print()
    print('=== 5. 清理临时文件 ===')
    temp_files = ['_commit_msg.txt', '_check_out.txt', '_check_v7_out.txt',
                  '_gen_out.txt', '_gen9.txt', '_poster_out.txt', '_preview9.txt']
    for tf in temp_files:
        p = ROOT / tf
        if p.exists():
            p.unlink()
            print(f'  DEL: {tf}')

    print()
    print('=== 6. 替换所有 HTML 链接 ===')
    all_html = sorted(ROOT.rglob('*.html'))
    for html_path in all_html:
        changes, log = process_html(html_path)
        if changes > 0:
            print(f'\n[{html_path.relative_to(ROOT)}] {changes} changes:')
            for line in log:
                print(line)

    print()
    print('=== 7. 处理 README.md（待用户手动更新）===')
    # README 由用户手动更新
    
    print()
    print('=== Done ===')


if __name__ == '__main__':
    main()
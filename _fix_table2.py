"""修复 markdown 表格中包含 | 的单元格 - 用全角竖线 ｜"""
import re
SRC = r'C:\Users\64549\.minimax\金融财富公司成立\乾元量化·因子全谱·研发参考.md'
with open(SRC, 'r', encoding='utf-8') as f:
    md = f.read()

# 改回原值
md = md.replace('`\\|Up - Down - 1\\|`', '`|Up - Down - 1|`')
md = md.replace('`Sum(\\|Ret\\|, 20) / Sum(Amount, 20)`', '`Sum(|Ret|, 20) / Sum(Amount, 20)`')
md = md.replace('`\\|Ret\\| / Amount`', '`|Ret| / Amount`')

# 然后在表格行内部，把 | (非分隔符) 替换为 ｜ (全角)
lines = md.split('\n')
new_lines = []
in_table = False
for line in lines:
    if line.startswith('|'):
        if not in_table:
            in_table = True
        # 表格行：把内部的 | 替换为 ｜
        # 但保留首尾的 | 作为分隔符
        # 简单做法：第一个和最后一个 | 保留，中间的 | 替换
        if line.count('|') >= 2:
            stripped = line.rstrip('\n')
            # 第一个 |
            first = stripped.find('|')
            last = stripped.rfind('|')
            head = stripped[:first+1]
            tail = stripped[last:]
            middle = stripped[first+1:last]
            middle_safe = middle.replace('|', '｜')
            new_line = head + middle_safe + tail
            new_lines.append(new_line)
            continue
    else:
        if in_table:
            in_table = False
    new_lines.append(line)

with open(SRC, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print('OK')
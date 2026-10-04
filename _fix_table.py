"""修复 markdown 表格中包含 | 的单元格"""
import re
SRC = r'C:\Users\64549\.minimax\金融财富公司成立\乾元量化·因子全谱·研发参考.md'
with open(SRC, 'r', encoding='utf-8') as f:
    md = f.read()

# 用 regex 把 `|xxx|` 这种代码块里的 | 转义
# 实际上更稳的做法是 escape 所有 markdown 表格 cell 内的 | (除了用作分隔符的)
# 但代码块 ``..`` 内的内容需要保留 |
# 简单做法：把 ``|Up - Down - 1|`` 转成 ``\|Up - Down - 1\|`` 之类

# 替换已知问题
fixes = [
    ('`|Up - Down - 1|`', '`\\|Up - Down - 1\\|`'),
    ('`Sum(|Ret|, 20) / Sum(Amount, 20)`', '`Sum(\\|Ret\\|, 20) / Sum(Amount, 20)`'),
    ('`|Ret| / Amount`', '`\\|Ret\\| / Amount`'),
]
for old, new in fixes:
    if old in md:
        md = md.replace(old, new)
        print(f'Fixed: {old}')

with open(SRC, 'w', encoding='utf-8') as f:
    f.write(md)
print('OK')
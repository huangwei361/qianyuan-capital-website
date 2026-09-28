"""检查 markdown 表格的列数一致性"""
import re
import os

SRC = r'C:\Users\64549\.minimax\金融财富公司成立\乾元量化·因子全谱·研发参考.md'
with open(SRC, 'r', encoding='utf-8') as f:
    md = f.read()

in_table = False
tbl = []
for line in md.split('\n'):
    if line.startswith('|'):
        if not in_table:
            in_table = True
            tbl = []
        tbl.append(line)
    else:
        if in_table:
            in_table = False
            rows = []
            for l in tbl:
                if re.match(r'^\|[\s\-:|]+\|$', l):
                    continue
                cells = [c for c in l.strip().strip('|').split('|')]
                rows.append((len(cells), l))
            if len(set(r[0] for r in rows)) > 1:
                print('BAD TABLE:')
                for cnt, l in rows:
                    print(f'  [{cnt}] {l!r}')
                print()
            tbl = []
print('Done.')
"""验证修复后的 brochure 结构"""
import re
with open('invest-brochure.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('=== HTML .b-page* 出现位置 ===')
seen = {}
for m in re.finditer(r'"b-page(5a|5b|\d+)"', html):
    key = 'b-page' + m.group(1)
    seen[key] = seen.get(key, 0) + 1
    print(f'  pos {m.start():5d}: .{key}  (第{seen[key]}次)')
print()
print('=== class 出现统计 ===')
for k in sorted(seen):
    print(f'  .{k}: {seen[k]} 次')

print()
print('=== 页脚页码 ===')
for m in re.finditer(r'P\. (\d{2}) / (\d{2})', html):
    print(f'  P. {m.group(1)} / {m.group(2)}')

print()
print('=== Page 注释 ===')
for m in re.finditer(r'<!-- =+\s*Page (5a|5b|\d+):', html):
    print(f'  Page {m.group(1)}')
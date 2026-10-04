"""批量清洗：去武汉 / 去（筹备）/ 副业→业务"""
import os
import sys

# 强制 UTF-8 输出
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\64549\.minimax\金融财富公司成立\website'
files = [
    'index.html',
    'global-shop.html',
    'quant.html',
    'quant-trading.html',
    'quant-rd.html',
]

# 替换规则
replacements = [
    # === 武汉 ===
    ('一个长期主义的武汉发起人', '一个长期主义的发起人'),
    ('坐标湖北武汉，主业稳定，', '坐标湖北，主业稳定，'),
    ('坐标湖北武汉，', '坐标湖北，'),
    ('湖北武汉，', '湖北，'),
    ('湖北武汉。', '湖北。'),
    ('湖北 · 武汉', '湖北'),
    (',武汉', ','),
    ('>武汉<', '><'),
    (',乾元系,长期主义,黄金投资,AI外贸,武汉', ',乾元系,长期主义,黄金投资,AI外贸'),
    ('content="乾元资本,乾元系,长期主义,黄金投资,AI外贸,武汉"', 'content="乾元资本,乾元系,长期主义,黄金投资,AI外贸"'),

    # === 副业 → 业务 ===
    ('5-10 万副业实操', '5-10 万小资金实操'),
    ('5 年内副业主力方向', '5 年内主营业务方向'),
    ('5 年内主攻副业方向', '5 年内主攻业务方向'),
    ('纯个人副业', '纯个人研究'),
    ('个人副业·纯研究', '个人研究·纯探索'),
    ('个人副业试水', '个人研究试水'),
    ('副业试水 3', '业务试水 3'),
    ('🟢 副业试水', '🟢 业务试水'),
    ('🟢 副业主力', '🟢 主营业务'),
    ('🟡 副业主力', '🟡 主营业务'),
    ('🟢 副业</div>', '🟢 业务</div>'),
    ('🟡 副业</div>', '🟡 业务</div>'),
    ('副业试水', '业务试水'),
    ('副业主力', '主营业务'),
    ('先做副业', '先做业务'),
    ('+ 副业 +', '+ 业务 +'),
    ('副业，', '业务，'),
    ('副业。', '业务。'),
    ('副业（', '业务（'),
    ('）副业', '）业务'),
    ('副业：', '业务：'),
    ('副业?', '业务?'),
    ('"副业"', '"业务"'),
    ('>副业<', '>业务<'),
    (' 副业 ', ' 业务 '),

    # === 筹备（删括号 / 换词）===
    ('（筹备）', ''),
    ('5-6 年 筹备期', '5-6 年 起步期'),
    ('5-6 年 筹备', '5-6 年 起步'),
    ('7-8 年 筹备', '7-8 年 起步'),
    ('8 年后 筹备', '8 年后 起步'),
    ('集团第 5 家筹备公司', '集团第 5 家规划中公司'),
    ('全在筹备中', '全在建设中'),
    ('5 年内为筹备期', '5 年内为建设期'),
    ('筹备中，', '建设中，'),
]

for fname in files:
    fpath = os.path.join(base, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    total = 0
    for old, new in replacements:
        if old in content:
            cnt = content.count(old)
            content = content.replace(old, new)
            total += cnt
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  [DONE] {fname}  total {total} replacements')
    else:
        print(f'  [SKIP] {fname}  no changes')
print('\nAll done!')

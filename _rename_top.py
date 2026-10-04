"""改 3 个 HTML 的标题/hero/description 为新口径（乾元投融资子公司）"""
from pathlib import Path
ROOT = Path(r'C:\Users\64549\.minimax\金融财富公司成立\website')

EDITS = {
    'invest.html': [
        ('乾元投融资规划和管理 · 乾元系',
         '乾元投融资子公司 · 乾元系'),
        ('<meta name="description" content="乾元资本集团旗下 乾元投融资规划和管理 · 集团级业务集群 · 投融资主业 + 企服 + 资产处理">',
         '<meta name="description" content="乾元资本集团旗下 乾元投融资子公司（投融资管理公司）· 投融资 + 企服两大版块 + 资产处理下挂">'),
        ('乾元资本集团旗下 · 乾元投融资规划和管理',
         '乾元资本集团旗下 · 乾元投融资子公司（投融资管理公司）'),
        ('<span class="hl">乾元投融资规划和管理</span>',
         '<span class="hl">乾元投融资子公司</span>'),
        ('<span class="sm">集团级业务集群 · 投融资主业 + 企服 + 资产处理</span>',
         '<span class="sm">集团级业务集群 · 投融资 + 企服 两大版块 · 资产处理下挂</span>'),
    ],
    'qifu.html': [
        ('乾元企服 · 乾元系',
         '乾元投融资子公司 · 企服版块 · 乾元系'),
        ('<meta name="description" content="乾元资本集团旗下 乾元企服 · 集团内部资金中心 · 8 大职能">',
         '<meta name="description" content="乾元资本集团旗下 乾元投融资子公司 · 企服版块 · 集团内部资金中心 · 8 大职能">'),
        ('乾元资本集团旗下 · 乾元企服',
         '乾元资本集团旗下 · 乾元投融资子公司 · 企服版块'),
        ('<span class="hl">乾元企服</span>',
         '<span class="hl">乾元投融资子公司 · 企服版块</span>'),
    ],
    'asset.html': [
        ('乾元资产处理 · 乾元系',
         '乾元投融资子公司 · 资产处理 · 乾元系'),
        ('<meta name="description" content="乾元资本集团旗下 乾元资产处理 · 法拍房 / 不良债权处置">',
         '<meta name="description" content="乾元资本集团旗下 乾元投融资子公司 · 资产处理 · 法拍房 / 不良债权处置">'),
        ('乾元资本集团旗下 · 乾元资产处理',
         '乾元资本集团旗下 · 乾元投融资子公司 · 资产处理'),
        ('<span class="hl">乾元资产处理</span>',
         '<span class="hl">乾元投融资子公司 · 资产处理</span>'),
    ],
}

total = 0
for fname, edits in EDITS.items():
    path = ROOT / fname
    content = path.read_text(encoding='utf-8')
    n = 0
    for old, new in edits:
        if old in content:
            content = content.replace(old, new)
            n += 1
    if n:
        print(f'{fname}: {n}/{len(edits)} 处替换')
        path.write_text(content, encoding='utf-8')
        total += n

print(f'\n=== Total: {total} 处替换 ===')
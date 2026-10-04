"""重命名 index.html 架构：1+7 → 1+5（投融资合并企服+资产处理）"""
import os
import re

base = r'C:\Users\64549\.minimax\金融财富公司成立\website'
fpath = os.path.join(base, 'index.html')

with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. meta description
content = content.replace(
    'content="乾元资本· 1 集团 + 7 家子公司 · 5-8 年长期主义规划"',
    'content="乾元资本· 1 集团 + 5 大业务集群 · 5-8 年长期主义规划"'
)

# 2. Hero sm
content = content.replace(
    '<span class="sm">1 集团 + 7 家子公司· 5-8 年长期主义</span>',
    '<span class="sm">1 集团 + 5 大业务集群· 5-8 年长期主义</span>'
)

# 3. Hero sub - 7 家 -> 5 大, 含黄金 / 出海 / 量化 / 投融资 / 租赁
content = content.replace(
    '下设 <strong>7 家全资子公司</strong>，覆盖<strong>黄金 / 出海 / 量化 / 投资 / 租赁 / 资产处理</strong>等长期方向。',
    '下设 <strong>5 大业务集群</strong>，覆盖<strong>黄金 / 出海 / 量化 / 投融资 / 租赁</strong>等长期方向。'
)

# 4. Hero CTA - 7 家子公司架构 → 5 大业务集群
content = content.replace(
    '<a href="#vision" class="btn btn-primary">看 7 家子公司架构 →</a>',
    '<a href="#vision" class="btn btn-primary">看 5 大业务集群架构 →</a>'
)

# 5. Hero stats - 1+7 → 1+5
content = content.replace(
    '<div class="num">1+7</div>\n          <div class="lbl">集团架构</div>',
    '<div class="num">1+5</div>\n          <div class="lbl">集团架构</div>'
)

# 6. 架构图标题
content = content.replace(
    '乾元资本集团 · 1 集团 + 8 家子公司 · 全在建设中',
    '乾元资本集团 · 1 集团 + 5 大业务集群 · 全在建设中'
)

# 7. 架构图副标题
content = content.replace(
    '以下 <strong>1 集团 + 8 家子公司</strong>目前都是个人研究方向 + 业务试水。',
    '以下 <strong>1 集团 + 5 大业务集群</strong>目前都是个人研究方向 + 业务试水。'
)

# 8. 架构图 av-meta
content = content.replace(
    '下设 <strong style="color:var(--gold);">7 家全资子公司</strong><br>每家都是独立子站',
    '下设 <strong style="color:var(--gold);">5 大业务集群</strong><br>每个集群下挂多家业务公司'
)

# 9. 架构图卡片调整：删除企服和资产处理独立卡片，重编号
old_arch = '''<a href="qifu.html" class="arch-item" data-link="qifu">
        <div class="ai-row"><div class="ai-num">1</div><h4>乾元企服</h4></div>
        <span class="ai-tag">集团内部服务</span>
        <p>集团资金中心（8 大职能）：归集/调度/融资/投资/税务/福利/风险/合规。</p>
        <span class="ai-go">进入企服官网 →</span>
      </a>
      <a href="gold.html" class="arch-item" data-link="gold">
        <div class="ai-row"><div class="ai-num">2</div><h4>乾元黄金</h4></div>'''

new_arch = '''<a href="gold.html" class="arch-item" data-link="gold">
        <div class="ai-row"><div class="ai-num">1</div><h4>乾元黄金</h4></div>'''

content = content.replace(old_arch, new_arch)

old_arch2 = '''<a href="invest.html" class="arch-item" data-link="invest">
        <div class="ai-row"><div class="ai-num">5</div><h4>乾元投资</h4></div>
        <span class="ai-tag">投融资规划 🟡</span>
        <p>找钱 + 用钱 + 循环。<br>融资 / 投资 / 业绩 / 信用 飞轮闭环。</p>
        <span class="ai-go">进入投资官网 →</span>
      </a>
      <a href="rental.html" class="arch-item" data-link="rental">
        <div class="ai-row"><div class="ai-num">6</div><h4>乾元租赁</h4></div>
        <span class="ai-tag">自营 4 套 ⚪</span>
        <p>房产租赁 / 代运营 / 物业服务。已有 4 套公寓，自营为主。</p>
        <span class="ai-go">进入租赁官网 →</span>
      </a>
      <a href="asset.html" class="arch-item" data-link="asset">
        <div class="ai-row"><div class="ai-num">7</div><h4>乾元资产处理</h4></div>
        <span class="ai-tag">学习阶段 ⚪</span>
        <p>不良资产价值重塑：法拍房 / 不良债权 / 困境企业重组。</p>
        <span class="ai-go">进入资产处理官网 →</span>
      </a>'''

new_arch2 = '''<a href="invest.html" class="arch-item" data-link="invest">
        <div class="ai-row"><div class="ai-num">3</div><h4>乾元投融资规划和管理</h4></div>
        <span class="ai-tag">🟡 业务集群 · 3 大业务</span>
        <p>集团级业务集群，下挂 <strong>投融资主业 / 乾元企服 / 乾元资产处理</strong>。<br>融资 + 投资 + 业绩 + 信用 飞轮闭环。</p>
        <span class="ai-go">进入投融资官网 →</span>
      </a>
      <a href="rental.html" class="arch-item" data-link="rental">
        <div class="ai-row"><div class="ai-num">4</div><h4>乾元租赁</h4></div>
        <span class="ai-tag">自营 4 套 ⚪</span>
        <p>房产租赁 / 代运营 / 物业服务。已有 4 套公寓，自营为主。</p>
        <span class="ai-go">进入租赁官网 →</span>
      </a>'''

content = content.replace(old_arch2, new_arch2)

# 10. 重新编号 global.html (3→2) 和 quant.html (4→3)
content = content.replace(
    '<a href="global.html" class="arch-item" data-link="global">\n        <div class="ai-row"><div class="ai-num">3</div><h4>乾元出海</h4></div>',
    '<a href="global.html" class="arch-item" data-link="global">\n        <div class="ai-row"><div class="ai-num">2</div><h4>乾元出海</h4></div>'
)
content = content.replace(
    '<a href="quant.html" class="arch-item" data-link="quant">\n        <div class="ai-row"><div class="ai-num">4</div><h4>乾元量化</h4></div>',
    '<a href="quant.html" class="arch-item" data-link="quant">\n        <div class="ai-row"><div class="ai-num">3</div><h4>乾元量化</h4></div>'
)

# 11. 集团发起人自述
content = content.replace(
    '<strong>乾元资本</strong>（集团母体）→ <strong>7 家乾元系子公司</strong>，覆盖金融 / 出海 / 不动产等长期方向。',
    '<strong>乾元资本</strong>（集团母体）→ <strong>5 大业务集群</strong>，覆盖金融 / 出海 / 不动产等长期方向。'
)

# 12. 集团旗下子站标题
content = content.replace(
    '1 集团 + 7 家子公司 · 7 个直链网页 · 全部入口',
    '1 集团 + 5 大业务集群 · 8 个直链网页 · 全部入口'
)

# 13. 子站区块副文
content = content.replace(
    '以下是乾元资本集团旗下 <strong>7 个独立子网页</strong>（7 家公司各 1 个）。<br>\n      乾元量化是 1 家公司，<strong>点入后再进入 2 个事业部子页</strong>（交易 / 研发）。<br>\n      点击直接进入对应子站。每个子站独立部署、独立管理。',
    '以下是乾元资本集团旗下 <strong>8 个独立子网页</strong>（5 大业务集群展开）。<br>\n      乾元量化是 1 家公司，<strong>点入后再进入 2 个事业部子页</strong>（交易 / 研发）。<br>\n      乾元投融资规划和管理是 1 个业务集群，<strong>下挂 3 个具体业务</strong>（投融资主业 / 企服 / 资产处理）。<br>\n      点击直接进入对应子站。每个子站独立部署、独立管理。'
)

# 14. 子站区块卡片调整：删除企服和资产处理独立卡片，合并投融资
old_sub = '''<a href="qifu.html" class="subsite-card">
        <div class="sc-num">1</div>
        <div class="sc-name">乾元企服</div>
        <div class="sc-tag">内部服务</div>
        <div class="sc-link">进入官网 →</div>
      </a>
      <a href="gold.html" class="subsite-card">
        <div class="sc-num">2</div>
        <div class="sc-name">乾元黄金</div>'''

new_sub = '''<a href="gold.html" class="subsite-card">
        <div class="sc-num">1</div>
        <div class="sc-name">乾元黄金</div>'''

content = content.replace(old_sub, new_sub)

old_sub2 = '''<a href="invest.html" class="subsite-card">
        <div class="sc-num">5</div>
        <div class="sc-name">乾元投资</div>
        <div class="sc-tag">🟡 投融资规划 · 找钱 + 用钱 + 循环</div>
        <div class="sc-link">进入官网 →</div>
      </a>
      <a href="rental.html" class="subsite-card">
        <div class="sc-num">6</div>
        <div class="sc-name">乾元租赁</div>
        <div class="sc-tag">⚪ 自营 4 套</div>
        <div class="sc-link">进入官网 →</div>
      </a>
      <a href="asset.html" class="subsite-card">
        <div class="sc-num">7</div>
        <div class="sc-name">乾元资产处理</div>
        <div class="sc-tag">⚪ 学习阶段</div>
        <div class="sc-link">进入官网 →</div>
      </a>'''

new_sub2 = '''<a href="invest.html" class="subsite-card subsite-card-with-shop">
        <a href="invest.html" class="sc-main">
          <div class="sc-num">3</div>
          <div class="sc-name">乾元投融资规划和管理</div>
          <div class="sc-tag">🟡 业务集群 · 下挂 3 大业务</div>
          <div class="sc-link">进入官网 →</div>
        </a>
        <div class="sc-sub-links">
          <a href="invest.html" class="sc-sub-link">📈 投融资主业</a>
          <a href="qifu.html" class="sc-sub-link">💼 乾元企服</a>
          <a href="asset.html" class="sc-sub-link">⚖️ 乾元资产处理</a>
        </div>
      </a>
      <a href="rental.html" class="subsite-card">
        <div class="sc-num">4</div>
        <div class="sc-name">乾元租赁</div>
        <div class="sc-tag">⚪ 自营 4 套</div>
        <div class="sc-link">进入官网 →</div>
      </a>'''

content = content.replace(old_sub2, new_sub2)

# 15. global.html 重编号 (3→2)
content = content.replace(
    '<a href="global.html" class="subsite-card">\n        <div class="sc-num">3</div>\n        <div class="sc-name">乾元出海</div>',
    '<a href="global.html" class="subsite-card">\n        <div class="sc-num">2</div>\n        <div class="sc-name">乾元出海</div>'
)
# 16. quant.html 重编号 (4→3)
content = content.replace(
    '<a href="quant.html" class="subsite-card">\n        <div class="sc-num">4</div>\n        <div class="sc-name">乾元量化</div>',
    '<a href="quant.html" class="subsite-card">\n        <div class="sc-num">3</div>\n        <div class="sc-name">乾元量化</div>'
)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html restructured: 1+7 → 1+5')
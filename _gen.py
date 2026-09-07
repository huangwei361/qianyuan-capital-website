"""批量生成 7 个乾元系子站"""
import os

# 子站配置：(目录, 品牌字, 品牌色, 名称, 副标题, hero描述, 业务定位, 内容, 5-8年规划)
SUBS = [
    {
        "dir": "housheng",
        "char": "厚",
        "color": "#FFD54F",
        "name": "厚生 HOUSHENG",
        "tagline": "集团主体业务 · 大健康品牌",
        "hero_sub": '集团旗下<strong style="color:#FFD54F;">主体业务品牌</strong>，<br>以"厚待众生"为 sologan，<br>5-8 年后期主业方向。',
        "stats": [("30年", "长期赛道"), ("3 大", "业务方向"), ("60+ 人口", "老龄化趋势")],
        "about_text": "厚生 HOUSHENG 是乾元资本集团<strong>主体业务品牌</strong>，定位<strong>大健康</strong>。\n        「厚生」二字取自《尚书》「厚生以养民」，意为<strong>丰厚民生、健康中国</strong>。",
        "sections": [
            ("🌿", "养生内容", "中医养生 / 食疗 / 季节性调养。<br>公众号 + 视频号矩阵，长期沉淀 IP。"),
            ("🛒", "健康选品", "产地直采的养生食材 / 茶饮 / 滋补品。<br>小红书种草 + 私域转化，<strong>信任驱动</strong>。"),
            ("🏥", "健康服务", "中医理疗 / 营养咨询 / 健康管理。<br>退休后考虑线下工作室或加盟模式。"),
        ],
        "stages": [
            ("🌱 5-6 年 试水期", "公众号 / 视频号 / 小红书内容矩阵"),
            ("🌿 6-7 年 选品期", "产地直采 + 私域电商"),
            ("🌳 7-8 年 服务期", "中医理疗 + 健康管理 + 线下店"),
        ],
    },
    {
        "dir": "qifu",
        "char": "服",
        "color": "#D4AF37",
        "name": "乾元企服",
        "tagline": "集团内部资金中心 · 8 大职能",
        "hero_sub": "集团内部的<strong>资金 + 服务</strong>中枢，<br>8 大职能模块支撑 9 家公司运转，<br>5-8 年后期才正式启动。",
        "stats": [("8", "大职能"), ("1+9", "服务架构"), ("5-8 年", "启动周期")],
        "about_text": "乾元企服是乾元资本集团旗下的<strong>内部资金中心</strong>，<br>负责集团内 9 家公司的资金归集、税务、福利、风险等核心职能。",
        "sections": [
            ("", "💰 资金归集", "集团账户体系 / 资金池管理 / 内部转账。"),
            ("", "📊 投资调度", "集团闲置资金理财 / 短期投资 / 流动性管理。"),
            ("", "💼 融资支持", "为各子公司对接融资渠道 / 银行贷款 / 股权融资。"),
            ("", "📋 税务福利", "集团税务筹划 / 员工福利 / 社保公积金代缴。"),
            ("", "⚖️ 风控合规", "集团整体风险监控 / 合规审查 / 内部审计。"),
            ("", "🔍 战略投资", "新业务孵化投资 / 战略并购 / 股权管理。"),
        ],
        "stages": [
            ("🌱 5-6 年 筹备期", "账户体系设计 + 制度建立"),
            ("🌿 7-8 年 试运营", "服务 2-3 家子公司"),
            ("🌳 8 年后 全面运营", "服务全部 9 家子公司"),
        ],
    },
    {
        "dir": "gold",
        "char": "金",
        "color": "#D4AF37",
        "name": "乾元黄金",
        "tagline": "实物黄金购销 / 积存金 / 旧金回收",
        "hero_sub": "黄金买卖+回收+品牌零售，<br>3 大核心价一目了然，<br>5 年内试水，5-8 年后期规模化。",
        "stats": [("3 大", "核心业务"), ("1 套", "金价看板"), ("8-15%", "目标毛利率")],
        "about_text": "乾元黄金是集团旗下的<strong>黄金业务事业部</strong>，<br>覆盖<strong>实物购销、积存金、旧金回收</strong>3 大业务方向。",
        "sections": [
            ("", "📥 进货采购", "上海金交所 Au99.99 / Au(T+D) 实时报价，<br>整批拿货可议 1.5-2.5 元/克折让。"),
            ("", "💰 零售挂牌", "对标周大福/老凤祥等头部品牌，<br>保持<strong>性价比 + 微涨</strong>节奏。"),
            ("", "♻ 旧金回收", "比主流品牌高 5-8 元/克回收，<br><strong>引流 + 复购</strong>入口业务。"),
            ("", "📊 银行积存金", "工/建/中/农/招/平 6 大行对比，<br>为客户代购代提服务。"),
            ("", "🛡️ 风控体系", "光谱仪检测 / 大额复核 / 库存风险敞口管理。"),
        ],
        "stages": [
            ("🟢 5 年内 试水", "个人 5-10 万副业实操"),
            ("🌿 5-6 年 工作室", "线下工作室 + 零售试点"),
            ("🌳 6-7 年 连锁", "2-3 家门店 + 加盟"),
        ],
    },
    {
        "dir": "global",
        "char": "出",
        "color": "#4FC3F7",
        "name": "乾元出海",
        "tagline": "AI 外贸 / Dropshipping 跨境 / 全球贸易",
        "hero_sub": "不备货、不压资金，<br><strong>AI 工具栈 + 1 平台打透</strong>，<br>5 年内主攻副业方向。",
        "stats": [("$1000", "月预算起步"), ("1 平台", "打透策略"), ("AI", "工具栈")],
        "about_text": "乾元出海是集团旗下的<strong>跨境电商事业部</strong>，<br>采用<strong>Dropshipping（无库存代发）</strong>模式，<br>用 AI 工具栈降低运营成本。",
        "sections": [
            ("", "🛒 选品方向", "家居 / 3C 配件 / 宠物 / 美妆 / 户外，<br>毛利率 > 50% 的细分品类。"),
            ("", "🌍 目标市场", "美国 / 欧洲 / 东南亚，<br>英语市场优先（流量大 + 客单价高）。"),
            ("", "🏪 平台选择", "Shopify / Amazon / TikTok Shop，<br>先 1 平台打透，再扩展。"),
            ("", "🤖 AI 工具栈", "选品调研 / 文案生成 / 图片处理 / 客服回复，<br>全部用 AI 提效。"),
            ("", "📊 运营节奏", "月预算 $200-500 起步，<br>前 6 个月验证模型，跑通再扩。"),
        ],
        "stages": [
            ("🟢 现在-1 年 学习", "课程 + 工具栈 + 跑通模型"),
            ("🌿 1-3 年 主攻", "月利润 $1000-3000 稳定"),
            ("🌳 3-5 年 规模化", "月利润 $5000+，团队化"),
        ],
    },
    {
        "dir": "invest",
        "char": "投",
        "color": "#FFD54F",
        "name": "乾元投资",
        "tagline": "战略投资 / 财务投资 / 多元资产配置",
        "hero_sub": "<strong>只投不运营</strong>，<br>5-8 年后期大资金阶段，<br>长期复利，慢就是快。",
        "stats": [("只投", "不运营"), ("5-8 年", "启动期"), ("复利", "核心策略")],
        "about_text": "乾元投资是集团旗下的<strong>战略投资业务</strong>，<br>负责集团外部投资 + 内部资产配置，<br><strong>只投资、不亲自运营</strong>。",
        "sections": [
            ("", "📈 战略投资", "对外部有潜力的企业做股权投资，<br>不参与日常运营，只做股东。"),
            ("", "💼 财务投资", "在公开市场做多资产配置：<br>股票 / 债券 / REITs / 商品 / 海外。"),
            ("", "🏢 不动产投资", "商业地产 / 写字楼 / 物流仓储，<br>稳定现金流 + 长期升值。"),
            ("", "🌐 海外配置", "QDII 基金 / 美股 / 港股 / 加密资产，<br>分散单一市场风险。"),
            ("", "🛡️ 风控原则", "单笔不超过总资产 10%，<br>行业分散 + 时间分散 + 地域分散。"),
        ],
        "stages": [
            ("🌱 5-6 年 筹备", "5 年清债 + 现金储备"),
            ("🌿 7 年 试投", "小资金开始财务投资"),
            ("🌳 8 年后 战略", "对外股权 + 不动产 + 多元资产"),
        ],
    },
    {
        "dir": "rental",
        "char": "租",
        "color": "#D4AF37",
        "name": "乾元租赁",
        "tagline": "房产租赁 / 代运营 / 物业服务",
        "hero_sub": "已持有 4 套公寓，<br>自营 + 代运营双模式，<br>5-8 年后期考虑加盟连锁。",
        "stats": [("4 套", "现有公寓"), ("2 模式", "自营+代运营"), ("5-10%", "年化收益")],
        "about_text": "乾元租赁是集团旗下的<strong>不动产租赁业务</strong>，<br>目前已有 4 套自营公寓，<br>5-8 年后期可考虑代运营/加盟。",
        "sections": [
            ("", "🏠 自营公寓", "已持有 4 套，<br>长租 + 短租结合，月入 1.5-2 万。"),
            ("", "🔧 代运营服务", "为业主提供：<br>招租 / 保洁 / 维修 / 账务全套服务，<br>收取 8-10% 服务费。"),
            ("", "📋 物业管理", "对接物业 / 维修 / 保洁供应商，<br>标准化流程，<strong>提升出租率</strong>。"),
            ("", "📊 租客运营", "筛选优质租客 / 长期维护关系，<br>降低空置率，提升续租率。"),
            ("", "💼 加盟连锁", "5-8 年后期：<br>输出品牌 + 系统 + 培训，<br>面向个人投资者加盟。"),
        ],
        "stages": [
            ("🟢 当前 自营", "4 套公寓全自营"),
            ("🌿 5-6 年 代运营", "接 5-10 套外部房源"),
            ("🌳 7-8 年 加盟", "区域加盟 + 品牌输出"),
        ],
    },
    {
        "dir": "asset",
        "char": "处",
        "color": "#90A4AE",
        "name": "乾元资产处理",
        "tagline": "法拍房 / 不良债权 / 价值重塑",
        "hero_sub": "不良资产<strong>价值重塑</strong>，<br>5 年内学习阶段，<br>6-7 年才正式进入。",
        "stats": [("3 大", "业务方向"), ("学习期", "当前阶段"), ("6-7 年", "正式启动")],
        "about_text": "乾元资产处理是集团旗下的<strong>特殊资产业务</strong>，<br>覆盖法拍房 / 不良债权 / 困境企业重组等，<br><strong>5 年内只学习不实操</strong>。",
        "sections": [
            ("", "🏛️ 法拍房", "捡漏司法拍卖的不动产，<br>需要：尽调 + 资金 + 处置能力。"),
            ("", "💳 不良债权", "从 AMC / 银行收购不良贷款，<br>通过催收 / 重整 / 诉讼变现。"),
            ("", "🏭 困境企业", "收购经营困难但有价值的企业，<br>重组团队 + 业务 + 财务后退出。"),
            ("", "📚 学习路径", "司法拍卖流程 / 尽调方法 / 资金募集 / 处置渠道，<br>前期通过读书 + 课程 + 圈内交流积累。"),
            ("", "⚖️ 风险提示", "不良资产<strong>专业门槛极高</strong>，<br>水很深，<strong>没有 3-5 年学习不要碰</strong>。"),
        ],
        "stages": [
            ("📚 5-6 年 学习", "读书 + 课程 + 圈内交流"),
            ("🌱 7 年 试水", "小资金参与 1-2 单"),
            ("🌳 8 年后 规模化", "团队化 + 系统化运作"),
        ],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} · 乾元系（筹备）</title>
  <meta name="description" content="乾元资本集团旗下 {name}（筹备）· {tagline}">
  <link rel="stylesheet" href="_sub.css">
  <style>
    :root {{
      --brand: {color};
      --brand-light: {color_light};
      --brand-dim: {color_dim};
    }}
  </style>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='45' fill='{color}'/><text x='50' y='62' font-size='40' text-anchor='middle' fill='%230A2540' font-family='serif' font-weight='800'>{char}</text></svg>">
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="brand">
      <div class="brand-mark">{char}</div>
      <span>{name} · 乾元系</span>
    </a>
    <ul class="nav-menu">
      <li><a href="#about">业务介绍</a></li>
      <li><a href="#content">核心内容</a></li>
      <li><a href="#plan">5-8 年规划</a></li>
      <li><a href="index.html" class="back-link">← 乾元资本主站</a></li>
    </ul>
  </div>
</nav>

<header class="hero">
  <div class="container">
    <div class="hero-tag">乾元资本集团（筹备）旗下 · {name}</div>
    <h1>
      <span class="hl">{name}</span>
      <span class="sm">{tagline}</span>
    </h1>
    <p class="hero-sub">{hero_sub}</p>
    <div class="hero-stats">
      {stats_html}
    </div>
  </div>
</header>

<section class="about" id="about" style="background: var(--navy-deep);">
  <div class="container">
    <div class="section-tag">业 务 定 位</div>
    <h2 class="section-title">关于 {name}</h2>
    <p class="section-sub">{about_text}</p>
  </div>
</section>

<section class="content" id="content">
  <div class="container">
    <div class="section-tag">核 心 内 容</div>
    <h2 class="section-title">{name} 业务模块</h2>
    <div class="card-grid cols-3" style="margin-top: 24px;">
      {cards_html}
    </div>
  </div>
</section>

<section class="plan" id="plan" style="background: var(--navy-deep);">
  <div class="container">
    <div class="section-tag">5-8 年 规 划</div>
    <h2 class="section-title">三阶段推进</h2>
    <div class="card-grid cols-3" style="margin-top: 24px;">
      {stages_html}
    </div>
  </div>
</section>

<!-- 兄弟部门 -->
<section class="sibling">
  <div class="container">
    <div class="section-tag">乾 元 系 其 他 子 公 司</div>
    <div class="sibling-grid" style="margin-top: 16px;">
      <a href="index.html" class="sibling-link"><div class="sl-tag">集团总部</div><div class="sl-name">乾元资本</div></a>
      <a href="housheng.html" class="sibling-link"><div class="sl-tag">🌟 主体</div><div class="sl-name">厚生 HOUSHENG</div></a>
      <a href="qifu.html" class="sibling-link"><div class="sl-tag">内部服务</div><div class="sl-name">乾元企服</div></a>
      <a href="gold.html" class="sibling-link"><div class="sl-tag">🟢 副业</div><div class="sl-name">乾元黄金</div></a>
      <a href="global.html" class="sibling-link"><div class="sl-tag">🟢 副业</div><div class="sl-name">乾元出海</div></a>
      <div class="sibling-link sibling-link-quant">
        <div class="sl-tag">🟡 副业</div>
        <div class="sl-name">乾元量化</div>
        <div class="sl-subs">
          <a href="quant-trading.html">📈 交易</a>
          <a href="quant-rd.html">🔬 研发</a>
        </div>
      </div>
      <a href="invest.html" class="sibling-link"><div class="sl-tag">🟡 后期</div><div class="sl-name">乾元投资</div></a>
      <a href="rental.html" class="sibling-link"><div class="sl-tag">⚪ 自营</div><div class="sl-name">乾元租赁</div></a>
      <a href="asset.html" class="sibling-link"><div class="sl-tag">⚪ 学习</div><div class="sl-name">乾元资产处理</div></a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <p><strong style="color: var(--brand);">{name}（筹备）</strong> · 乾元资本集团旗下</p>
    <p><a href="index.html">← 乾元资本集团主站</a> · <a href="housheng.html">厚生 HOUSHENG</a></p>
    <p>© 2026 乾元资本（筹备）· 本网站为个人博客性质，不构成投资建议或商业承诺</p>
  </div>
</footer>

</body>
</html>'''

# Helper: lighten color
def lighten(hex_color, amount=0.3):
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)
    return f"#{r:02X}{g:02X}{b:02X}"

def hex_to_rgba(hex_color, alpha=0.15):
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"

# Build all 7 sub-sites
base = r'C:\Users\64549\.minimax\金融财富公司成立\website'
for sub in SUBS:
    color = sub['color']
    color_light = lighten(color, 0.3)
    color_dim = hex_to_rgba(color, 0.15)

    stats_html = ''.join([
        f'<div class="hero-stat"><div class="num" style="color: {color};">{n}</div><div class="lbl">{l}</div></div>'
        for n, l in sub['stats']
    ])

    cards_html = ''
    for icon, title, desc in sub['sections']:
        cards_html += f'''<div class="card">
        <div class="card-icon">{icon}</div>
        <h4>{title}</h4>
        <p>{desc}</p>
      </div>
'''

    stages_html = ''
    for stage, desc in sub['stages']:
        stages_html += f'''<div class="stage-card">
        <div class="stage">{stage}</div>
        <h4>{stage.split(' ', 1)[1] if ' ' in stage else stage}</h4>
        <p>{desc}</p>
      </div>
'''

    html = TEMPLATE.format(
        name=sub['name'],
        char=sub['char'],
        color=color,
        color_light=color_light,
        color_dim=color_dim,
        tagline=sub['tagline'],
        hero_sub=sub['hero_sub'],
        stats_html=stats_html,
        about_text=sub['about_text'],
        cards_html=cards_html,
        stages_html=stages_html,
    )

    target = os.path.join(base, f'{sub["dir"]}.html')
    with open(target, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  [OK] {sub["dir"]}.html ({len(html)} bytes)')

print('\nDone!')

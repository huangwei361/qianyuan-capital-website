"""生成乾元投融资规划和管理 业务方案 Word 文档"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r'C:\Users\64549\.minimax\金融财富公司成立\invest-plan.docx'

doc = Document()

# 设置默认字体（中文：宋体；英文：Times New Roman）
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
style.font.size = Pt(11)

# 设置页面边距
sections = doc.sections
for s in sections:
    s.top_margin = Cm(2.5)
    s.bottom_margin = Cm(2.5)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(2.5)

# === 标题颜色 ===
GOLD = RGBColor(0xB8, 0x86, 0x0B)
NAVY = RGBColor(0x0A, 0x25, 0x40)
GRAY = RGBColor(0x66, 0x66, 0x66)

def add_heading(text, level=1, color=NAVY):
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        run.font.color.rgb = color
        run.font.name = 'Microsoft YaHei'
        run.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    return p

def add_para(text, bold=False, color=None, size=11):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    if color: r.font.color.rgb = color
    r.font.name = 'Microsoft YaHei'
    r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    return p

def add_table_3col(headers, rows, widths=[Cm(4), Cm(8), Cm(4.5)]):
    table = doc.add_table(rows=1+len(rows), cols=3)
    table.style = 'Light Grid Accent 1'
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        for p in hdr[i].paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = GOLD
                r.font.size = Pt(11)
    for ri, row in enumerate(rows):
        cells = table.rows[ri+1].cells
        for ci, txt in enumerate(row):
            cells[ci].text = txt
            for p in cells[ci].paragraphs:
                for r in p.runs:
                    r.font.size = Pt(10.5)
    for i, w in enumerate(widths):
        for row in table.rows:
            row.cells[i].width = w
    return table

# ============================================================
# 封面
# ============================================================
cover = doc.add_paragraph()
cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
for _ in range(6): cover.add_run('\n')

cover.add_run().add_break()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('BUSINESS PLAN v1.0')
r.font.size = Pt(14)
r.font.color.rgb = GOLD
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('\n乾元投融资规划和管理\n')
r.font.size = Pt(36); r.font.bold = True; r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
r = p.add_run('业务方案\n')
r.font.size = Pt(36); r.font.bold = True; r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('投融资主业 + 乾元企服 + 乾元资产处理')
r.font.size = Pt(16); r.font.color.rgb = GRAY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

for _ in range(8): doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('乾元资本集团（筹备） · 集团级业务集群')
r.font.size = Pt(13); r.font.color.rgb = NAVY; r.font.bold = True
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('5-8 年长期主义 · 个人研究方向 · 5 年内不正式工商注册')
r.font.size = Pt(11); r.font.color.rgb = GRAY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('文档版本：v1.0 · 更新日期：2026-09-24')
r.font.size = Pt(11); r.font.color.rgb = GRAY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

doc.add_page_break()

# ============================================================
# §1 业务定位
# ============================================================
add_heading('§ 1  业务定位', level=1)
add_heading('集团级业务集群 · 下挂 3 大业务', level=2, color=GOLD)

add_para('乾元投融资规划和管理是乾元资本集团旗下的集团级业务集群（原"乾元投资"业务升级），整合：')
add_para('① 投融资主业（找钱 + 用钱 + 循环）', bold=True, color=GOLD)
add_para('② 乾元企服（内部资金中心 / 8 大职能）', bold=True, color=GOLD)
add_para('③ 乾元资产处理（不良资产价值重塑）', bold=True, color=GOLD)
add_para('')
add_para('核心理念：融资（找钱）+ 投资（用钱）+ 两者结合的循环，形成投融资一体化的飞轮——')
add_para('融到的钱投资产生业绩，业绩建立信用，信用反哺下一轮融资，每一轮都比上一轮更厚。', bold=True)

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('关键指标')
r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

add_table_3col(['指标', '说明', '数值'], [
    ['业务数', '下挂业务集群', '3'],
    ['规划周期', '5-8 年长期主义', '5-8 年'],
    ['融资规模门槛', '超过此规模需名下有资产', '3000 万+'],
    ['信贷杠杆', '信贷扩张公式倍数', '12 倍'],
])

doc.add_page_break()

# ============================================================
# §2 融资方法论
# ============================================================
add_heading('§ 2  融资方法论', level=1)
add_heading('3 要素 · 4 类型 · 3 策略 · 7 步法', level=2, color=GOLD)

add_para('融资不是"求人借钱"，而是用信用 + 身份 + 筹码撬动外部资金的系统工程。')
add_para('融资本质是经营 + 杠杆 + 复利的三位一体。', bold=True)
add_para('融资规模超过 3000 万，一定是有资产在名下——这是融资的硬规则。', bold=True, color=GOLD)

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('① 融资 3 要素')
r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

add_table_3col(['要素', '细分项', '说明'], [
    ['信用', '征信 / 流水 / 社保公积金 / 信贷记录', '融资的门票，没有信用连第一道门都进不去'],
    ['身份', '学历 / 户口 / 单位 / 房车', '融资的加分器，好身份可拿到更低利率'],
    ['筹码', '营收 / 名下资产 / 抵押物 / 经营年限', '融资的杠杆，筹码越多融资规模越大'],
])

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('② 4 大融资类型')
r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

add_table_3col(['类型', '产品', '门槛 / 规模'], [
    ['银行类', '营收贷 / 信用贷 / 抵押贷 / 按揭', '营收 100 万+ 可贷 100 万'],
    ['政策类', '创业基金 / 科创委 / 土地抵押 / 接力贷', '创业基金最高 50 万（3 月）/ 科创委最高 300 万（9 月）'],
    ['特殊类', '当铺 / 物业贷 / 连锁贷 / 股权质押', '1 万月息，质押快速放款'],
    ['民间类', '小额信贷 / 亲友拆借 / 联合众筹 / 股权出让', '小额灵活，适合早期'],
])

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('③ 3 大融资策略')
r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

add_table_3col(['策略', '方法', '适用场景'], [
    ['背书型', '用别人的资产给自己背书（借他人信用+资产作担保）', '早期无资产的创业者'],
    ['套现型', '评估价 2000 万的房子抵押 7-8 成 = 套出 1400-1600 万', '下行期买不良资产（评估价 1000 万，300 万拿下）'],
    ['杠杆型', '上浮 12% + 30 年接力贷，最小首付买最大的房', '长期看涨的资产（必须先评估下行风险）'],
])

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('④ 7 步融资法 · 案例：霸道总裁')
r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

add_para('前提：经营时间 > 2 年 + 月业绩 380 万 / 毛利 90 万 / 流水 100 万+ → 7 步融到 100 万')

add_table_3col(['步骤', '动作', '要点'], [
    ['1', '养流水', '个人卡走 100 万+ 流水'],
    ['2', '经营 2 年', '营业执照 + 实际经营'],
    ['3', '资产配置', '名下有房 / 车 / 保单'],
    ['4', '申请信用贷', '身份证 + 公积金'],
    ['5', '申请营收贷', '经营流水放大 100 倍'],
    ['6', '申请抵押贷', '评估价 7-8 成'],
    ['7', '循环放大', '业绩 → 信用 → 再贷'],
])

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('信贷扩张公式')
r.font.bold = True; r.font.size = Pt(12); r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('30 万 资产 + 信用产品经营 12 倍 = 360 万 融资')
r.font.bold = True; r.font.size = Pt(18); r.font.color.rgb = GOLD
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('30 万净资产 + 12 倍杠杆 = 360 万可融资规模')
r.font.size = Pt(11); r.font.color.rgb = GRAY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

doc.add_page_break()

# ============================================================
# §3 投资组合
# ============================================================
add_heading('§ 3  投资组合', level=1)
add_heading('4 大投资方向 · 多资产配置', level=2, color=GOLD)

add_para('融到的钱如何"用好"是关键。乾元投融资规划和管理的投资组合覆盖战略 / 财务 / 不动产 / 海外 4 大方向，')
add_para('通过分散配置降低单一资产风险，实现长期复利。')

add_table_3col(['方向', '投资方式', '预期收益 / 风险'], [
    ['战略投资', '对外部潜力企业做股权投资（不参与日常运营）', '中长期 3-10 倍 · 风险 🟡 中高'],
    ['财务投资', '公开市场多资产配置（股票 / 债券 / REITs / 商品）', '年化 8-15% · 风险 🟢 中低'],
    ['不动产', '商业地产 / 写字楼 / 物流仓储（稳定现金流）', '年化 5-10% + 增值 · 风险 🟢 中低'],
    ['海外配置', 'QDII 基金 / 美股 / 港股 / 海外房产', '分散单一市场风险 · 风险 🟡 中'],
])

add_para('⚖️ 风控原则：单笔不超过总资产 10% · 行业分散 + 时间分散 + 地域分散', bold=True, color=GOLD)

doc.add_page_break()

# ============================================================
# §4 商业飞轮
# ============================================================
add_heading('§ 4  商业飞轮', level=1)
add_heading('投融资循环 · 自我增强', level=2, color=GOLD)

add_para('乾元投融资不是"先融资再投资"的两段式，而是投融资一体化的飞轮：', bold=True)
add_para('融到的钱 → 投出去产生业绩 → 业绩建立信用 → 信用反哺下一轮融资', bold=True, color=GOLD)
add_para('每一轮循环都让飞轮转得更快、融得更多、投得更准。')

doc.add_paragraph()
add_table_3col(['环节', '动作', '输出'], [
    ['融资', '股权 / 债权 / 信用 / 众筹', '建立资金池'],
    ['投资', '战略 / 财务 / 不动产 / 海外', '产生业绩'],
    ['业绩', '真实回报记录', '建立信用'],
    ['信用', '信用升级', '反哺下一轮融资'],
])

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('核心逻辑：融资和投资不是两件事，而是同一件事的两面。')
r.font.bold = True; r.font.color.rgb = NAVY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('投得好 → 业绩好 → 信用好 → 融得更多 → 投得更大 → 业绩更好，复利增长。')
r.font.bold = True; r.font.color.rgb = GOLD
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

doc.add_page_break()

# ============================================================
# §5 5-8 年路线
# ============================================================
add_heading('§ 5  5-8 年路线图', level=1)
add_heading('三阶段推进 · 飞轮成型', level=2, color=GOLD)

add_para('5-8 年规划期内，不开公司、不正式工商注册，先以个人名义跑通模型。')
add_para('退休或找到合规合伙人后，再考虑落地实体公司。')

add_table_3col(['阶段', '时间', '核心动作 · 目标规模'], [
    ['信用积累', '5-6 年', '5 年清债 + 建立个人信用 + 养流水 + 小额试投 · 融资 10-30 万'],
    ['跑通小循环', '7 年', '完成 1-2 轮"融资 → 投资 → 业绩"小循环 · 融资 50-100 万'],
    ['飞轮放大', '8 年后', '扩大融资规模 + 多元投资组合 + 飞轮自转 · 融资 300 万+'],
])

doc.add_page_break()

# ============================================================
# §6 财务预测
# ============================================================
add_heading('§ 6  财务预测', level=1)
add_heading('三档情景预测（5 年后）', level=2, color=GOLD)

add_para('基于信用积累 → 跑通小循环 → 飞轮放大三阶段路径，对 5 年后的融资规模 + 投资收益做保守 / 中性 / 乐观三档预测。')
add_para('以下预测为个人研究方向估算，不构成任何投资承诺。', bold=True, color=GOLD)

doc.add_paragraph()
add_table_3col(['情景', '5 年后融资规模', '资产合计'], [
    ['保守', '150 万 · 年化收益 5%', '≈ 200 万'],
    ['中性', '500 万 · 年化收益 10%', '≈ 800 万'],
    ['乐观', '1500 万 · 年化收益 15%', '≈ 3000 万'],
])

doc.add_paragraph()
add_table_3col(['年度', '融资规模', '投资组合 · 累计收益'], [
    ['第 1 年', '5-10 万', '个人信用贷 + 小额试投 · 基本持平'],
    ['第 2 年', '20-50 万', '营收贷 + 财务投资 · +5-10%'],
    ['第 3 年', '100-200 万', '抵押贷 + 战略投资 · +15-30%'],
    ['第 4 年', '300-500 万', '联合众筹 + 海外配置 · +40-80%'],
    ['第 5 年', '500-1500 万', '飞轮自转 + 多资产组合 · +100-300%'],
])

doc.add_page_break()

# ============================================================
# §7 风险控制
# ============================================================
add_heading('§ 7  风险控制', level=1)
add_heading('5 大风险 + 应对策略', level=2, color=GOLD)

add_para('投融资是高风险业务，风险控制比收益更重要。')

add_table_3col(['风险', '具体表现', '应对策略'], [
    ['政策风险', '金融政策变动 / 利率上行 / 信贷收紧', '只做合规业务，杠杆率控制在 50% 以下'],
    ['市场风险', '股市 / 楼市 / 商品下行 / 黑天鹅', '多资产分散 + 时间分散 + 地域分散'],
    ['信用风险', '债务违约 / 抵押物贬值 / 担保链断裂', '单笔不超过总资产 10%，严控抵押率'],
    ['流动性风险', '资产无法快速变现 / 资金链紧张', '保留 20% 以上现金等价物'],
    ['合规风险', '5 年内不正式开公司', '5 年内仅以个人名义操作，退休或合规合伙人后再落地'],
])

doc.add_page_break()

# ============================================================
# §8 合作方式
# ============================================================
add_heading('§ 8  合作方式', level=1)
add_heading('3 种合作模式', level=2, color=GOLD)

add_para('5-8 年规划期内，乾元投融资规划和管理接受 3 种合作模式。')
add_para('5 年内为建设期，仅以个人名义小范围合作，不做大规模对外融资/承诺。')

add_table_3col(['合作模式', '合作方式', '分红 / 权益'], [
    ['联合投资', '项目跟投 / 联合众筹 / 战略合作 · 个人投资者 / 小型机构', '按出资比例分享收益'],
    ['顾问咨询', '融资方案咨询 / 投资组合建议 / 风险评估 · 有需求的企业或个人', '咨询费 + 业绩分成'],
    ['共建合作', '共建投资载体 / 共同发起基金 / 联合落地公司 · 5-8 年后期寻找合规合伙人', '股权 / 战略合作'],
])

doc.add_page_break()

# ============================================================
# §9 联系
# ============================================================
add_heading('§ 9  联系咨询', level=1)
add_heading('开启合作', level=2, color=GOLD)

add_para('5-8 年规划期内，仅以个人名义接受项目跟投 + 顾问咨询类合作。', bold=True)
add_para('不接受大额资金托管，不承诺保本收益，不构成任何投资建议。', bold=True, color=GOLD)

doc.add_paragraph()
add_table_3col(['方式', '联系方式', '说明'], [
    ['邮箱', 'qygc@163.com', '推荐 · 可附合作模式 + 出资规模'],
    ['WhatsApp', '139-7169-1656', '微信同号 · 国内外均可'],
    ['电话', '139-7169-1656', '工作时间'],
])

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('正式合作前请先沟通：合作模式 / 出资规模 / 项目类型 / 风险偏好')
r.font.italic = True; r.font.color.rgb = GRAY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

# 页脚声明
doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run('© 2026 乾元资本（筹备）· 本网站为个人博客性质，不构成投资建议或商业承诺')
r.font.size = Pt(9); r.font.color.rgb = GRAY
r.font.name = 'Microsoft YaHei'
r.element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

doc.save(OUT)
print(f'OK: {OUT}')
print(f'Size: {os.path.getsize(OUT)} bytes')
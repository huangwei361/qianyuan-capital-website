"""一次性修复 brochure 排版问题（CSS 类名重复 + P5 拆分）"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

SRC = r'C:\Users\64549\.minimax\金融财富公司成立\website\invest-brochure.html'
DST = r'C:\Users\64549\.minimax\金融财富公司成立\website\invest-brochure.html'

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 第 1 步：CSS 重命名（去重 + 重新编号 P6-P11）
# ============================================================
# 策略：CSS 是按行写的，先把整段 CSS 提取出来重命名，再插回去。

# 1.1 line 312-382 范围（承诺页样式，定义为 .b-page7）→ 改为 .b-page6
old_css_promise = """    .b-page7 { padding: 0; display: flex; flex-direction: column; background: #fff; }
    .b-page7-head { text-align: center; padding: 10mm 20mm 5mm; background: linear-gradient(180deg, #06182A 0%, #0A2540 100%); color: #fff; }
    .b-page7-head .tag { font-size: 9pt; color: #FFD54F; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page7-head h2 { font-size: 26pt; font-weight: 900; color: #fff; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page7-head .sub { font-size: 11pt; color: rgba(255,255,255,0.7); }
    .b-page7-body { padding: 6mm 20mm 8mm; flex: 1; }
    .b-section-tag-small {
      display: inline-block; font-size: 9pt; color: #FFD54F;
      letter-spacing: 3px; padding: 1.5mm 3mm;
      border: 0.5pt solid #FFD54F; border-radius: 2mm;
      margin-bottom: 3mm;
    }
    .b-section-title-small {
      font-size: 15pt; font-weight: 800;
      color: #06182A; letter-spacing: 1px;
      margin-bottom: 4mm;
    }
    .b-promise-row { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-bottom: 6mm; }
    .b-promise {
      padding: 5mm 5mm;
      background: linear-gradient(180deg, #FFFBEA 0%, #fff 100%);
      border-left: 3pt solid #FFD54F;
      border-radius: 2mm;
    }
    .b-promise-head { display: flex; align-items: center; gap: 2mm; margin-bottom: 2mm; }
    .b-promise-num {
      display: inline-block; font-size: 9pt; font-weight: 900;
      color: #FFD54F; background: rgba(255,213,79,0.15);
      padding: 0.5mm 2.5mm; border-radius: 3mm;
      letter-spacing: 1px;
    }
    .b-promise-title {
      font-size: 12pt; font-weight: 800;
      color: #06182A; letter-spacing: 1px;
    }
    .b-promise-text {
      font-size: 9pt; color: #555;
      line-height: 1.6;
    }
    .b-promise-text strong { color: #06182A; font-weight: 700; }
    .b-risk-section-title {
      font-size: 13pt; font-weight: 800;
      color: #06182A; letter-spacing: 2px;
      margin: 4mm 0 3mm; text-align: center;
      padding-top: 4mm;
      border-top: 0.5pt solid #E5E8EE;
    }
    .b-risk-row { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 3mm; }
    .b-risk-card {
      padding: 4mm 3mm; background: #06182A;
      color: #fff; border-radius: 3mm;
      text-align: center;
    }
    .b-risk-icon { font-size: 22pt; margin-bottom: 2mm; }
    .b-risk-title {
      font-size: 10pt; font-weight: 800;
      color: #FFD54F; letter-spacing: 1px;
      margin-bottom: 1.5mm;
    }
    .b-risk-text {
      font-size: 8pt; color: rgba(255,255,255,0.7);
      line-height: 1.5;
    }
    .b-page7-foot {
      padding: 4mm 20mm; background: #06182A;
      color: rgba(255,255,255,0.5);
      font-size: 8pt; letter-spacing: 1px;
      display: flex; justify-content: space-between;
    }
    .b-page7-foot strong { color: #FFD54F; }"""
new_css_promise = old_css_promise.replace('.b-page7-foot strong', '.b-page6-foot strong').replace('.b-page7-foot {', '.b-page6-foot {').replace('.b-page7-body', '.b-page6-body').replace('.b-page7-head', '.b-page6-head').replace('.b-page7 {', '.b-page6 {')
html = html.replace(old_css_promise, new_css_promise)
print('1.1 promise CSS 承诺页 .b-page7 → .b-page6 ✓')

# 1.2 line 384-460 范围（客户页样式，定义为 .b-page8）→ 改为 .b-page7
old_css_client = """    .b-page8 { padding: 0; display: flex; flex-direction: column; background: linear-gradient(180deg, #FFFBEA 0%, #fff 30%); }
    .b-page8-head { text-align: center; padding: 10mm 20mm 4mm; }
    .b-page8-head .tag { font-size: 9pt; color: #B8860B; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page8-head h2 { font-size: 26pt; font-weight: 900; color: #06182A; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page8-head .sub { font-size: 11pt; color: #666; }
    .b-client-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; padding: 0 20mm 5mm; }
    .b-client {
      padding: 5mm 5mm; background: #fff;
      border: 1pt solid #FFD54F;
      border-radius: 3mm;
    }
    .b-client-head { display: flex; align-items: center; gap: 3mm; margin-bottom: 3mm; }
    .b-client-avatar {
      width: 12mm; height: 12mm;
      background: linear-gradient(135deg, #FFD54F, #FFC107);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-size: 16pt;
      flex-shrink: 0;
    }
    .b-client-type {
      font-size: 11pt; font-weight: 800;
      color: #06182A; letter-spacing: 1px;
    }
    .b-client-tag {
      font-size: 8pt; color: #B8860B;
      letter-spacing: 1px;
    }
    .b-client-scenario {
      font-size: 9pt; color: #555;
      line-height: 1.6;
    }
    .b-client-scenario strong { color: #06182A; font-weight: 700; }
    .b-journey-title {
      font-size: 13pt; font-weight: 800;
      color: #06182A; letter-spacing: 2px;
      margin: 5mm 20mm 3mm;
      text-align: center;
    }
    .b-journey { padding: 0 20mm 8mm; }
    .b-journey-row { display: grid; grid-template-columns: repeat(5, 1fr); gap: 3mm; }
    .b-journey-step {
      padding: 4mm 3mm;
      background: #fff;
      border: 1pt solid #E5E8EE;
      border-radius: 3mm;
      text-align: center;
    }
    .b-journey-step .num {
      font-size: 16pt; font-weight: 900;
      color: #FFD54F; line-height: 1;
      margin-bottom: 1mm;
      font-family: "Georgia", serif;
    }
    .b-journey-step .stage {
      font-size: 8pt; color: #B8860B;
      letter-spacing: 1px; margin-bottom: 1mm;
    }
    .b-journey-step .name {
      font-size: 10pt; font-weight: 800;
      color: #06182A; letter-spacing: 1px;
      margin-bottom: 1.5mm;
    }
    .b-journey-step .desc {
      font-size: 8pt; color: #666;
      line-height: 1.5;
    }
    .b-page8-foot {
      padding: 5mm 20mm;
      background: #FFFBEA;
      color: #B8860B;
      font-size: 9pt; letter-spacing: 1px;
      text-align: center;
      border-top: 0.5pt solid #FFD54F;
    }
    .b-page8-foot strong { color: #06182A; }"""
new_css_client = old_css_client.replace('.b-page8-foot strong', '.b-page7-foot strong').replace('.b-page8-foot {', '.b-page7-foot {').replace('.b-page8-head', '.b-page7-head').replace('.b-page8 {', '.b-page7 {')
html = html.replace(old_css_client, new_css_client)
print('1.2 client CSS 客户页 .b-page8 → .b-page7 ✓')

# 1.3 line 462-479 范围（案例页样式，定义为 .b-page6）→ 改为 .b-page8
old_css_case = """    .b-page6 { padding: 0; display: flex; flex-direction: column; }
    .b-page6-head { padding: 12mm 20mm 5mm; text-align: center; }
    .b-page6-tag { font-size: 9pt; color: #B8860B; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page6-title { font-size: 26pt; font-weight: 900; color: #06182A; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page6-sub { font-size: 11pt; color: #666; }
    .b-case-row { flex: 1; padding: 4mm 20mm 14mm; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 5mm; }
    .b-case { background: #fff; border: 1pt solid #E5E8EE; border-radius: 4mm; padding: 6mm 5mm; display: flex; flex-direction: column; position: relative; overflow: hidden; }
    .b-case::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3mm; background: linear-gradient(90deg, #FFD54F 0%, #FFC107 100%); }
    .b-case-icon { font-size: 30pt; margin-top: 2mm; margin-bottom: 2mm; }
    .b-case-name { font-size: 16pt; font-weight: 800; color: #06182A; letter-spacing: 1px; margin-bottom: 1mm; }
    .b-case-role { font-size: 9pt; color: #B8860B; letter-spacing: 1px; margin-bottom: 3mm; }
    .b-case-num { display: inline-block; font-size: 10pt; font-weight: 800; color: #FFD54F; background: rgba(255,213,79,0.12); padding: 1.5mm 3mm; border-radius: 12mm; margin-bottom: 3mm; }
    .b-case-story { font-size: 9.5pt; line-height: 1.7; color: #555; }
    .b-case-story p { margin-bottom: 2mm; }
    .b-case-story strong { color: #06182A; font-weight: 700; }
    .b-page6-foot { padding: 5mm 20mm; background: #06182A; color: rgba(255,255,255,0.5); font-size: 8pt; letter-spacing: 1px; display: flex; justify-content: space-between; }
    .b-page6-foot strong { color: #FFD54F; }"""
new_css_case = old_css_case.replace('.b-page6-foot strong', '.b-page8-foot strong').replace('.b-page6-foot {', '.b-page8-foot {').replace('.b-page6-sub', '.b-page8-sub').replace('.b-page6-title', '.b-page8-title').replace('.b-page6-tag', '.b-page8-tag').replace('.b-page6-head', '.b-page8-head').replace('.b-page6 {', '.b-page8 {')
html = html.replace(old_css_case, new_css_case)
print('1.3 case CSS 案例页 .b-page6 → .b-page8 ✓')

# 1.4 line 482-495 范围（擅长页样式，定义为 .b-page7）→ 改为 .b-page9
old_css_skill = """    .b-page7 { padding: 0; display: flex; flex-direction: column; background: #06182A; color: #fff; }
    .b-page7-head { padding: 12mm 20mm 4mm; text-align: center; }
    .b-page7-tag { font-size: 9pt; color: #FFD54F; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page7-title { font-size: 26pt; font-weight: 900; color: #fff; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page7-sub { font-size: 11pt; color: rgba(255,255,255,0.6); }
    .b-skill-row { flex: 1; padding: 4mm 20mm 8mm; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; }
    .b-skill { padding: 6mm 5mm; background: rgba(255,255,255,0.04); border: 0.5pt solid rgba(255,213,79,0.25); border-radius: 4mm; color: #fff; }
    .b-skill-num { font-size: 32pt; font-weight: 900; color: #FFD54F; line-height: 1; margin-bottom: 2mm; font-family: "Georgia", serif; }
    .b-skill-title { font-size: 16pt; font-weight: 800; color: #fff; letter-spacing: 1px; margin-bottom: 1mm; }
    .b-skill-en { font-size: 8pt; color: rgba(255,255,255,0.4); letter-spacing: 2px; margin-bottom: 3mm; }
    .b-skill-desc { font-size: 9.5pt; color: rgba(255,255,255,0.8); line-height: 1.7; }
    .b-skill-desc strong { color: #FFD54F; }
    .b-page7-foot { padding: 5mm 20mm; background: rgba(0,0,0,0.3); color: rgba(255,255,255,0.5); font-size: 8pt; letter-spacing: 1px; display: flex; justify-content: space-between; border-top: 0.5pt solid rgba(255,213,79,0.2); }
    .b-page7-foot strong { color: #FFD54F; }"""
new_css_skill = old_css_skill.replace('.b-page7-foot strong', '.b-page9-foot strong').replace('.b-page7-foot {', '.b-page9-foot {').replace('.b-page7-sub', '.b-page9-sub').replace('.b-page7-title', '.b-page9-title').replace('.b-page7-tag', '.b-page9-tag').replace('.b-page7-head', '.b-page9-head').replace('.b-page7 {', '.b-page9 {')
html = html.replace(old_css_skill, new_css_skill)
print('1.4 skill CSS 擅长页 .b-page7 → .b-page9 ✓')

# 1.5 line 498-516 范围（生态页样式，定义为 .b-page8）→ 改为 .b-page10
old_css_eco = """    .b-page8 { background: #fff; }
    .b-page8-head { text-align: center; padding-bottom: 5mm; margin-bottom: 6mm; border-bottom: 0.5pt solid #E5E8EE; }
    .b-page8-tag { font-size: 9pt; color: #B8860B; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page8-title { font-size: 26pt; font-weight: 900; color: #06182A; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page8-sub { font-size: 11pt; color: #666; }"""
new_css_eco = old_css_eco.replace('.b-page8-sub', '.b-page10-sub').replace('.b-page8-title', '.b-page10-title').replace('.b-page8-tag', '.b-page10-tag').replace('.b-page8-head', '.b-page10-head').replace('.b-page8 {', '.b-page10 {')
# .b-page8-foot 改名 .b-page10-foot
old_eco_foot = """    .b-page8-foot { position: absolute; bottom: 8mm; left: 20mm; right: 20mm; display: flex; justify-content: space-between; font-size: 8pt; color: #999; letter-spacing: 1px; }
    .b-page8-foot strong { color: #B8860B; }"""
new_eco_foot = old_eco_foot.replace('.b-page8-foot strong', '.b-page10-foot strong').replace('.b-page8-foot {', '.b-page10-foot {')
html = html.replace(old_css_eco, new_css_eco)
html = html.replace(old_eco_foot, new_eco_foot)
print('1.5 eco CSS 生态页 .b-page8 → .b-page10 ✓')

# 1.6 line 519-540 范围（邀请页样式，定义为 .b-page9）→ 改为 .b-page11
old_css_inv = """    .b-page9 { padding: 0; display: flex; flex-direction: column; background: linear-gradient(135deg, #06182A 0%, #0A2540 100%); color: #fff; }
    .b-page9-top { padding: 14mm 20mm 8mm; flex: 1; }
    .b-page9-tag { font-size: 9pt; color: #FFD54F; letter-spacing: 4px; margin-bottom: 6mm; }
    .b-page9-title { font-size: 32pt; font-weight: 900; color: #fff; letter-spacing: 2px; line-height: 1.2; margin-bottom: 6mm; }
    .b-page9-title .accent { color: #FFD54F; }
    .b-page9-sub { font-size: 13pt; color: rgba(255,255,255,0.8); line-height: 1.7; letter-spacing: 1px; margin-bottom: 8mm; }
    .b-people { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; margin-bottom: 8mm; }
    .b-person { padding: 4mm 4mm; background: rgba(255,213,79,0.08); border: 0.5pt solid rgba(255,213,79,0.3); border-radius: 3mm; }
    .b-person-icon { font-size: 22pt; margin-bottom: 2mm; }
    .b-person-title { font-size: 11pt; font-weight: 800; color: #FFD54F; letter-spacing: 1px; margin-bottom: 1.5mm; }
    .b-person-desc { font-size: 8.5pt; color: rgba(255,255,255,0.7); line-height: 1.5; }
    .b-cta-box { padding: 7mm 7mm; background: linear-gradient(135deg, #FFD54F 0%, #FFC107 100%); color: #06182A; border-radius: 4mm; text-align: center; margin-bottom: 6mm; }
    .b-cta-box h3 { font-size: 17pt; font-weight: 900; letter-spacing: 2px; margin-bottom: 4mm; }
    .b-cta-box p { font-size: 10.5pt; color: #1a1a1a; line-height: 1.7; }
    .b-cta-box strong { font-weight: 800; }
    .b-contact-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; }
    .b-contact-cell { padding: 4mm 3mm; background: rgba(255,255,255,0.06); border: 0.5pt solid rgba(255,255,255,0.15); border-radius: 3mm; text-align: center; }
    .b-contact-cell-icon { font-size: 16pt; margin-bottom: 1mm; }
    .b-contact-cell-title { font-size: 8pt; font-weight: 800; color: #FFD54F; letter-spacing: 2px; margin-bottom: 1mm; }
    .b-contact-cell-value { font-size: 9pt; color: rgba(255,255,255,0.8); line-height: 1.4; font-weight: 700; }
    .b-page9-foot { padding: 5mm 20mm; background: rgba(0,0,0,0.3); font-size: 7.5pt; color: rgba(255,255,255,0.4); letter-spacing: 1px; border-top: 0.5pt solid rgba(255,213,79,0.2); }
    .b-page9-foot .disclaimer { font-size: 7.5pt; color: rgba(255,255,255,0.4); line-height: 1.5; }"""
new_css_inv = old_css_inv.replace('.b-page9-foot .disclaimer', '.b-page11-foot .disclaimer').replace('.b-page9-foot {', '.b-page11-foot {').replace('.b-page9-sub', '.b-page11-sub').replace('.b-page9-title .accent', '.b-page11-title .accent').replace('.b-page9-title', '.b-page11-title').replace('.b-page9-tag', '.b-page11-tag').replace('.b-page9-top', '.b-page11-top').replace('.b-page9 {', '.b-page11 {')
html = html.replace(old_css_inv, new_css_inv)
print('1.6 invitation CSS 邀请页 .b-page9 → .b-page11 ✓')

# ============================================================
# 第 2 步：P5 CSS 拆分为 P5a + P5b
# ============================================================
# 当前 P5 CSS（line 112-249）包含 3 相信 + 4 拒绝，全部要拆。
# 我们已经有完整的 .b-page5b CSS（line 251-310），所以只需要：
#   - 现有 .b-page5 CSS → 拆为 .b-page5a（3 相信，含 head + believe 区 + 删掉过渡和 reject 区）
#   - 现有 .b-page5b CSS → 已经是独立页样式，保留

# 改造 .b-page5 CSS：去掉 reject 相关，只留 head + believe
old_p5_css = """.b-page5 { padding: 0; display: flex; flex-direction: column; background: #fff; }
    .b-page5-head { text-align: center; padding: 10mm 20mm 5mm; background: linear-gradient(180deg, #FFFBEA 0%, #fff 100%); border-bottom: 0.5pt solid #FFD54F; }
    .b-page5-tag { font-size: 9pt; color: #B8860B; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page5-title { font-size: 26pt; font-weight: 900; color: #06182A; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page5-sub { font-size: 11pt; color: #666; }

    /* 3 个相信：上半页 */
    .b-page5-believe { padding: 6mm 20mm 5mm; background: #FFFBEA; }"""
new_p5_css = """.b-page5a { padding: 0; display: flex; flex-direction: column; background: #fff; min-height: 100vh; }
    .b-page5a-head { text-align: center; padding: 14mm 20mm 8mm; background: linear-gradient(180deg, #FFFBEA 0%, #fff 100%); border-bottom: 0.5pt solid #FFD54F; }
    .b-page5a-tag { font-size: 9pt; color: #B8860B; letter-spacing: 4px; margin-bottom: 2mm; }
    .b-page5a-title { font-size: 28pt; font-weight: 900; color: #06182A; letter-spacing: 1px; margin-bottom: 2mm; }
    .b-page5a-sub { font-size: 11pt; color: #666; }

    /* 3 个相信：整页米黄底 */
    .b-page5a-believe { flex: 1; padding: 8mm 20mm 10mm; background: #FFFBEA; }"""
html = html.replace(old_p5_css, new_p5_css)
print('2.1 P5 CSS → P5a CSS ✓')

# 改 P5 foot CSS
old_p5_foot_css = """    .b-page5-foot {
      padding: 4mm 20mm;
      background: rgba(0,0,0,0.4);
      color: rgba(255,255,255,0.5);
      font-size: 8pt; letter-spacing: 1px;
      display: flex; justify-content: space-between;
      border-top: 0.5pt solid rgba(255,213,79,0.2);
    }
    .b-page5-foot strong { color: #FFD54F; }"""
new_p5_foot_css = """    .b-page5a-foot {
      padding: 5mm 20mm;
      background: #06182A;
      color: rgba(255,255,255,0.5);
      font-size: 8pt; letter-spacing: 1px;
      display: flex; justify-content: space-between;
      border-top: 0.5pt solid rgba(255,213,79,0.2);
    }
    .b-page5a-foot strong { color: #FFD54F; }"""
html = html.replace(old_p5_foot_css, new_p5_foot_css)
print('2.2 P5 foot CSS → P5a foot CSS ✓')

# 改 P5b CSS 中的 class 名（在 line 251-310 已部分定义）
# 当前 .b-page5b 已存在，确认 class 名

# ============================================================
# 第 3 步：HTML 端 P5 拆分为 P5a + P5b
# ============================================================
# 当前 P5 HTML（line 763-891）：
# - 头部 .b-page5 .b-page5-head .b-page5-tag/title/sub
# - 上半 .b-page5-believe（3 个相信）
# - 中间过渡 .b-reject-intro
# - 下半 .b-page5-reject（4 个拒绝）
# - 页脚 .b-page5-foot

old_p5_html = '''<!-- ========== Page 5: 我们的信条（详细版）========== -->
<div class="b-page b-page5">
  <div class="b-page5-head">
    <div class="b-page5-tag">PHILOSOPHY · 我们的信条</div>
    <div class="b-page5-title">3 个相信 · 4 个拒绝 · 详细版</div>
    <div class="b-page5-sub">不是方法论，是判断标准</div>
  </div>

  <!-- 上半：3 个相信（米黄底） -->
  <div class="b-page5-believe">
    <div class="b-believe-head">
      <div class="b-believe-head-mark">✓</div>
      <div class="b-believe-head-title">我们相信的 3 件事</div>
      <div class="b-believe-head-en">WHAT WE BELIEVE</div>
    </div>
    <div class="b-belief-row">
      <div class="b-belief">
        <div class="b-belief-icon">🌀</div>
        <div class="b-belief-num">NO. 01</div>
        <div class="b-belief-title">飞轮之上</div>
        <div class="b-belief-en">THE FLYWHEEL</div>
        <div class="b-belief-text">
          <strong>每一轮比上一轮更厚</strong>，时间越长、复利越大。
        </div>
        <div class="b-belief-text-detail">
          我们不接受"一次赚够"的项目——那是赌博，不是飞轮。<br>
          <strong>实操：</strong>每一轮融资→投资的闭环都让<strong>信用资产</strong>增值，下一轮融资更便宜、更大。
          <span class="quote">"业绩 → 信用 → 再融资，每一轮都是下一轮的杠杆。"</span>
        </div>
      </div>
      <div class="b-belief">
        <div class="b-belief-icon">⏳</div>
        <div class="b-belief-num">NO. 02</div>
        <div class="b-belief-title">长期主义</div>
        <div class="b-belief-en">LONG-TERM</div>
        <div class="b-belief-text">
          <strong>5-8 年起步 · 30 年视角</strong>。
        </div>
        <div class="b-belief-text-detail">
          拒绝短期暴利诱惑。<br>
          <strong>实操：</strong>所有项目周期 &gt; 5 年；所有投资至少持有 3 年；<strong>复利曲线</strong>在前 3 年平缓，第 5 年开始陡峭。
          <span class="quote">"慢就是快，厚就是大，30 年磨一件事的人，最终会有重量。"</span>
        </div>
      </div>
      <div class="b-belief">
        <div class="b-belief-icon">🤝</div>
        <div class="b-belief-num">NO. 03</div>
        <div class="b-belief-title">共生共建</div>
        <div class="b-belief-en">CO-SHARING</div>
        <div class="b-belief-text">
          <strong>客户不是被服务者，是共建者</strong>。
        </div>
        <div class="b-belief-text-detail">
          业绩公开、信用互认、合作长期。<br>
          <strong>实操：</strong>每月业绩公开、季度客户回访、所有数据共享；<strong>每一方都得到真实回报</strong>，不是单边抽佣。
          <span class="quote">"长期复利不是一个人赚的钱，是一群人一起赚的。"</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 中间过渡语 -->
  <div class="b-reject-intro">
    <div class="b-reject-intro-text">
      所以我们 <span class="accent">拒绝</span> 4 类项目 ——<br>
      不是挑剔，是<strong>对长期复利的尊重</strong>
    </div>
  </div>

  <!-- 下半：4 个拒绝（深蓝底） -->
  <div class="b-page5-reject">
    <div class="b-reject-head">
      <div class="b-reject-head-mark">✕</div>
      <div class="b-reject-head-title">我们拒绝的 4 件事</div>
      <div class="b-reject-head-en">WHAT WE REFUSE</div>
    </div>
    <div class="b-reject-grid">
      <div class="b-reject-card">
        <div class="b-reject-num">01</div>
        <div class="b-reject-body">
          <div class="b-reject-title">承诺保本</div>
          <div class="b-reject-text">
            <strong>保本是幻觉</strong>。<br>
            真正稳的资产靠<strong>分散 + 长期 + 信用</strong>，不靠承诺。<br>
            <span style="color:rgba(255,213,79,0.7);font-size:8pt;">→ 见多了"保本"陷阱，2018 年 P2P / 2020 年银行理财亏损都是例子</span>
          </div>
        </div>
      </div>
      <div class="b-reject-card">
        <div class="b-reject-num">02</div>
        <div class="b-reject-body">
          <div class="b-reject-title">一年翻倍</div>
          <div class="b-reject-text">
            <strong>一年翻倍是赌博</strong>。<br>
            真正赚的是<strong>慢慢变厚</strong>，不是<strong>一年暴富</strong>。<br>
            <span style="color:rgba(255,213,79,0.7);font-size:8pt;">→ 巴菲特年化 20%，50 年复利 → 8000 倍。赌翻倍的人第 3 年就没了</span>
          </div>
        </div>
      </div>
      <div class="b-reject-card">
        <div class="b-reject-num">03</div>
        <div class="b-reject-body">
          <div class="b-reject-title">闷声发大财</div>
          <div class="b-reject-text">
            <strong>闷声的项目不可持续</strong>。<br>
            <strong>业绩公开</strong>才是真业绩。<br>
            <span style="color:rgba(255,213,79,0.7);font-size:8pt;">→ 我们承诺：所有业绩月度公开、季度复盘，所有合作方都能看到</span>
          </div>
        </div>
      </div>
      <div class="b-reject-card">
        <div class="b-reject-num">04</div>
        <div class="b-reject-body">
          <div class="b-reject-title">短期暴利诱惑</div>
          <div class="b-reject-text">
            <strong>短期暴利必有陷阱</strong>。<br>
            我们要的是<strong>5-8 年慢钱</strong>，不是 3 个月快钱。<br>
            <span style="color:rgba(255,213,79,0.7);font-size:8pt;">→ 历史上所有"短期暴利"产品 5 年后都归零，没有例外</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="b-page5-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 05 / 11</span>
  </div>
</div>'''

# 改写为 P5a（3 相信整页米黄）+ P5b（4 拒绝独立深蓝页）
new_p5_html = '''<!-- ========== Page 5a: 我们的信条-3相信（整页米黄） ========== -->
<div class="b-page b-page5a">
  <div class="b-page5a-head">
    <div class="b-page5a-tag">PHILOSOPHY · 我们的信条（上）</div>
    <div class="b-page5a-title">3 个我们<span class="accent">相信</span>的事</div>
    <div class="b-page5a-sub">不是方法论，是判断标准 · 下页是 4 个我们拒绝的事</div>
  </div>

  <div class="b-page5a-believe">
    <div class="b-believe-head">
      <div class="b-believe-head-mark">✓</div>
      <div class="b-believe-head-title">我们相信的 3 件事</div>
      <div class="b-believe-head-en">WHAT WE BELIEVE</div>
    </div>
    <div class="b-belief-row">
      <div class="b-belief">
        <div class="b-belief-icon">🌀</div>
        <div class="b-belief-num">NO. 01</div>
        <div class="b-belief-title">飞轮之上</div>
        <div class="b-belief-en">THE FLYWHEEL</div>
        <div class="b-belief-text">
          <strong>每一轮比上一轮更厚</strong>，时间越长、复利越大。
        </div>
        <div class="b-belief-text-detail">
          我们不接受"一次赚够"的项目——那是赌博，不是飞轮。<br>
          <strong>实操：</strong>每一轮融资→投资的闭环都让<strong>信用资产</strong>增值，下一轮融资更便宜、更大。
          <span class="quote">"业绩 → 信用 → 再融资，每一轮都是下一轮的杠杆。"</span>
        </div>
      </div>
      <div class="b-belief">
        <div class="b-belief-icon">⏳</div>
        <div class="b-belief-num">NO. 02</div>
        <div class="b-belief-title">长期主义</div>
        <div class="b-belief-en">LONG-TERM</div>
        <div class="b-belief-text">
          <strong>5-8 年起步 · 30 年视角</strong>。
        </div>
        <div class="b-belief-text-detail">
          拒绝短期暴利诱惑。<br>
          <strong>实操：</strong>所有项目周期 &gt; 5 年；所有投资至少持有 3 年；<strong>复利曲线</strong>在前 3 年平缓，第 5 年开始陡峭。
          <span class="quote">"慢就是快，厚就是大，30 年磨一件事的人，最终会有重量。"</span>
        </div>
      </div>
      <div class="b-belief">
        <div class="b-belief-icon">🤝</div>
        <div class="b-belief-num">NO. 03</div>
        <div class="b-belief-title">共生共建</div>
        <div class="b-belief-en">CO-SHARING</div>
        <div class="b-belief-text">
          <strong>客户不是被服务者，是共建者</strong>。
        </div>
        <div class="b-belief-text-detail">
          业绩公开、信用互认、合作长期。<br>
          <strong>实操：</strong>每月业绩公开、季度客户回访、所有数据共享；<strong>每一方都得到真实回报</strong>，不是单边抽佣。
          <span class="quote">"长期复利不是一个人赚的钱，是一群人一起赚的。"</span>
        </div>
      </div>
    </div>
  </div>

  <div class="b-page5a-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 05 / 12</span>
  </div>
</div>

<!-- ========== Page 5b: 我们的信条-4拒绝（独立深蓝页） ========== -->
<div class="b-page b-page5b">
  <div class="b-page5b-head">
    <div class="tag">PHILOSOPHY · 我们的信条（下）</div>
    <h2>4 个我们<span class="accent">拒绝</span>的事</h2>
    <div class="sub">不是挑剔，是对长期复利的尊重</div>
  </div>
  <div class="b-page5b-body">
    <div class="b-page5b-intro">
      所以我们 <span class="accent">拒绝</span> 4 类项目 ——<br>
      不是挑剔，是<strong>对长期复利的尊重</strong>
    </div>
    <div class="b-reject-grid-2x2">
      <div class="b-reject-card">
        <div class="b-reject-num">01</div>
        <div class="b-reject-body">
          <div class="b-reject-title">承诺保本</div>
          <div class="b-reject-text">
            <strong>保本是幻觉</strong>。<br>
            真正稳的资产靠<strong>分散 + 长期 + 信用</strong>，不靠承诺。<br>
            <span class="note">→ 2018 年 P2P / 2020 年银行理财亏损都是例子</span>
          </div>
        </div>
      </div>
      <div class="b-reject-card">
        <div class="b-reject-num">02</div>
        <div class="b-reject-body">
          <div class="b-reject-title">一年翻倍</div>
          <div class="b-reject-text">
            <strong>一年翻倍是赌博</strong>。<br>
            真正赚的是<strong>慢慢变厚</strong>，不是<strong>一年暴富</strong>。<br>
            <span class="note">→ 巴菲特年化 20%，50 年复利 → 8000 倍。赌翻倍的人第 3 年就没了</span>
          </div>
        </div>
      </div>
      <div class="b-reject-card">
        <div class="b-reject-num">03</div>
        <div class="b-reject-body">
          <div class="b-reject-title">闷声发大财</div>
          <div class="b-reject-text">
            <strong>闷声的项目不可持续</strong>。<br>
            <strong>业绩公开</strong>才是真业绩。<br>
            <span class="note">→ 我们承诺：所有业绩月度公开、季度复盘，所有合作方都能看到</span>
          </div>
        </div>
      </div>
      <div class="b-reject-card">
        <div class="b-reject-num">04</div>
        <div class="b-reject-body">
          <div class="b-reject-title">短期暴利诱惑</div>
          <div class="b-reject-text">
            <strong>短期暴利必有陷阱</strong>。<br>
            我们要的是<strong>5-8 年慢钱</strong>，不是 3 个月快钱。<br>
            <span class="note">→ 历史上所有"短期暴利"产品 5 年后都归零，没有例外</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="b-page5b-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 06 / 12</span>
  </div>
</div>'''

if old_p5_html in html:
    html = html.replace(old_p5_html, new_p5_html)
    print('3.1 P5 HTML 拆分为 P5a + P5b ✓')
else:
    print('⚠️  P5 HTML 块未找到，需要手动检查')
    # 调试：找近似串
    idx = html.find('<!-- ========== Page 5:')
    if idx >= 0:
        print(f'  P5 注释在 index {idx}')
        print(f'  附近 100 字符: {html[idx:idx+100]!r}')
    sys.exit(1)

# ============================================================
# 第 4 步：HTML 重命名 .b-page6/7/8/9 → 对应正确页码
# ============================================================
# 当前 HTML 中：
# - "我们的承诺" → .b-page6（用了案例样式 .b-page6-head 等）→ 改为承诺样式 .b-page6-head 等（已经在 CSS 重命名时改过了）
#   但 .b-page6-foot 等内部类名也要改

# 4.1 "我们的承诺"页 HTML（line 893-998）：当前用 .b-page6 + 内部 .b-page6-head 等
# 当前 HTML 中的"承诺页"：
old_promise_html_head = '''<!-- ========== Page 6: 我们的承诺（新）========== -->
<div class="b-page b-page6">
  <div class="b-page6-head">
    <div class="tag">PROMISE · 我们的承诺</div>'''
new_promise_html_head = '''<!-- ========== Page 6: 我们的承诺 ========== -->
<div class="b-page b-page6">
  <div class="b-page6-head">
    <div class="tag">PROMISE · 我们的承诺</div>'''
html = html.replace(old_promise_html_head, new_promise_html_head)
print('4.1 承诺页 HTML head 注释 ✓')

# 4.2 "我们的客户"页 HTML（line 1000-1092）：当前用 .b-page7 + 内部 .b-page7-head → 但 CSS 改成 .b-page6 头部等
# 实际上 line 1001 是 <div class="b-page b-page7">，需要保留 .b-page7，但内部子元素需要从 .b-page7-head 改成 .b-page7-head
# 等等，我之前 CSS 改了：line 312-382 整块 .b-page7 系列 → .b-page6 系列（承诺页）
# 但 line 1001 客户的 HTML 用的是 .b-page7，所以现在 CSS 里没有 .b-page7-head 样式（被删了）
# 需要把客户的 HTML 改为 .b-page7，但内部子元素改名：.b-page7-head, .b-page7-foot 是没有的
# 正确做法：把客户的 .b-page7 系列 CSS 子类名都已改为 .b-page7（因为 line 384-460 的 .b-page8 改成了 .b-page7）

# 等等，我看错了。让我重新捋一下：
# CSS line 312-382 → 改了：.b-page7 → .b-page6（这是承诺样式）
# CSS line 384-460 → 改了：.b-page8 → .b-page7（这是客户样式）
# CSS line 482-495 → 改了：.b-page7 → .b-page9（这是擅长样式）
# CSS line 498-516 → 改了：.b-page8 → .b-page10（这是生态样式）

# 所以现在 CSS 是：
# .b-page6 = 承诺样式 ✓
# .b-page7 = 客户样式 ✓
# .b-page8 = 案例样式 ✓
# .b-page9 = 擅长样式 ✓
# .b-page10 = 生态样式 ✓
# .b-page11 = 邀请样式 ✓

# 现在 HTML 中哪些页面用了错误的 class？
# HTML line 894（承诺页）: <div class="b-page b-page6"> ✓ 正确
#   但内部 .b-page6-head, .b-page6-body, .b-page6-foot → 已 CSS 改名，应该正常
# HTML line 1001（客户页）: <div class="b-page b-page7"> ✓ 正确
#   但内部 .b-page7-head → CSS 里有 .b-page7-head（来自 line 384-460 重命名）✓
#   .b-page7-foot → CSS 里有 .b-page7-foot ✓
# HTML line 1095（案例页）: <div class="b-page b-page6"> ❌ 错！应该是 .b-page8
#   内部 .b-page6-head, .b-page6-tag, .b-page6-title, .b-page6-sub, .b-page6-foot → 应该改为 .b-page8 系列
# HTML line 1148（擅长页）: <div class="b-page b-page7"> ❌ 错！应该是 .b-page9
#   内部 .b-page7-head, .b-page7-tag, .b-page7-title, .b-page7-sub, .b-page7-foot → 应该改为 .b-page9 系列
# HTML line 1190（生态页）: <div class="b-page b-page8"> ❌ 错！应该是 .b-page10
#   内部 .b-page8-head, .b-page8-tag, .b-page8-title, .b-page8-sub, .b-page8-foot → 应该改为 .b-page10 系列
# HTML line 1264（邀请页）: <div class="b-page b-page9"> ❌ 错！应该是 .b-page11
#   内部 .b-page9-top, .b-page9-tag, .b-page9-title, .b-page9-sub, .b-page9-foot → 应该改为 .b-page11 系列

# 4.3 案例页 .b-page6 → .b-page8（line 1095 段）
# 整段替换
old_case_html = '''<!-- ========== Page 6: 3 个真实案例 ========== -->
<div class="b-page b-page6">
  <div class="b-page6-head">
    <div class="b-page6-tag">CASES · 真实案例</div>
    <div class="b-page6-title">3 个飞轮转起来的故事</div>
    <div class="b-page6-sub">不是数据，是故事</div>
  </div>'''
new_case_html = '''<!-- ========== Page 8: 3 个真实案例 ========== -->
<div class="b-page b-page8">
  <div class="b-page8-head">
    <div class="b-page8-tag">CASES · 真实案例</div>
    <div class="b-page8-title">3 个飞轮转起来的故事</div>
    <div class="b-page8-sub">不是数据，是故事</div>
  </div>'''
html = html.replace(old_case_html, new_case_html)

# 案例页 footer .b-page6-foot → .b-page8-foot
old_case_foot = '''  <div class="b-page6-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 08 / 11</span>
  </div>
</div>

<!-- ========== Page 7: 我们擅长的 3 件事 ========== -->'''
new_case_foot = '''  <div class="b-page8-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 08 / 12</span>
  </div>
</div>

<!-- ========== Page 9: 我们擅长的 3 件事 ========== -->'''
html = html.replace(old_case_foot, new_case_foot)
print('4.3 案例页 .b-page6 → .b-page8 ✓')

# 4.4 擅长页 .b-page7 → .b-page9
old_skill_html = '''<!-- ========== Page 7: 我们擅长的 3 件事 ========== -->
<div class="b-page b-page7">
  <div class="b-page7-head">
    <div class="b-page7-tag">WHAT WE DO · 我们擅长的</div>
    <div class="b-page7-title">3 件事，让我们不同</div>
    <div class="b-page7-sub">不只是融资中介 · 不只是财务投资 · 我们是闭环设计者</div>
  </div>'''
new_skill_html = '''<!-- ========== Page 9: 我们擅长的 3 件事 ========== -->
<div class="b-page b-page9">
  <div class="b-page9-head">
    <div class="b-page9-tag">WHAT WE DO · 我们擅长的</div>
    <div class="b-page9-title">3 件事，让我们不同</div>
    <div class="b-page9-sub">不只是融资中介 · 不只是财务投资 · 我们是闭环设计者</div>
  </div>'''
html = html.replace(old_skill_html, new_skill_html)

old_skill_foot = '''  <div class="b-page7-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 09 / 11</span>
  </div>
</div>

<!-- ========== Page 8: 乾元生态 ========== -->'''
new_skill_foot = '''  <div class="b-page9-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 09 / 12</span>
  </div>
</div>

<!-- ========== Page 10: 乾元生态 ========== -->'''
html = html.replace(old_skill_foot, new_skill_foot)
print('4.4 擅长页 .b-page7 → .b-page9 ✓')

# 4.5 生态页 .b-page8 → .b-page10
old_eco_html = '''<!-- ========== Page 8: 乾元生态 ========== -->
<div class="b-page b-page8">
  <div class="b-page8-head">
    <div class="b-page8-tag">ECOSYSTEM · 乾元生态</div>
    <div class="b-page8-title">我们不是一个人在战斗</div>
    <div class="b-page8-sub">乾元系 4 大协同业务 · 共同支撑投融资飞轮</div>
  </div>'''
new_eco_html = '''<!-- ========== Page 10: 乾元生态 ========== -->
<div class="b-page b-page10">
  <div class="b-page10-head">
    <div class="b-page10-tag">ECOSYSTEM · 乾元生态</div>
    <div class="b-page10-title">我们不是一个人在战斗</div>
    <div class="b-page10-sub">乾元系 4 大协同业务 · 共同支撑投融资飞轮</div>
  </div>'''
html = html.replace(old_eco_html, new_eco_html)

old_eco_foot_html = '''  <div class="b-page8-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 10 / 11</span>
  </div>
</div>

<!-- ========== Page 9: 邀请 + CTA ========== -->'''
new_eco_foot_html = '''  <div class="b-page10-foot">
    <span><strong>乾元投融资规划和管理</strong> · 品牌宣传册 v1.0</span>
    <span>P. 10 / 12</span>
  </div>
</div>

<!-- ========== Page 11: 邀请 + CTA ========== -->'''
html = html.replace(old_eco_foot_html, new_eco_foot_html)
print('4.5 生态页 .b-page8 → .b-page10 ✓')

# 4.6 邀请页 .b-page9 → .b-page11
old_inv_html = '''<!-- ========== Page 9: 邀请 + CTA ========== -->
<div class="b-page b-page9">
  <div class="b-page9-top">
    <div class="b-page9-tag">INVITATION · 邀请</div>
    <div class="b-page9-title">如果你也是<br><span class="accent">这样的人</span></div>
    <div class="b-page9-sub">'''
new_inv_html = '''<!-- ========== Page 11: 邀请 + CTA ========== -->
<div class="b-page b-page11">
  <div class="b-page11-top">
    <div class="b-page11-tag">INVITATION · 邀请</div>
    <div class="b-page11-title">如果你也是<br><span class="accent">这样的人</span></div>
    <div class="b-page11-sub">'''
html = html.replace(old_inv_html, new_inv_html)

old_inv_foot = '''  <div class="b-page9-foot">
    <div class="disclaimer">'''
new_inv_foot = '''  <div class="b-page11-foot">
    <div class="disclaimer">'''
html = html.replace(old_inv_foot, new_inv_foot)
print('4.6 邀请页 .b-page9 → .b-page11 ✓')

# ============================================================
# 第 5 步：更新页码总页数 11 → 12
# ============================================================
# 找到所有 P. xx / 11 改为 P. xx / 12
html = re.sub(r'P\. (\d{2}) / 11\b', r'P. \1 / 12', html)
print('5.1 所有页脚 P. xx / 11 → P. xx / 12 ✓')

# ============================================================
# 第 6 步：保存
# ============================================================
with open(DST, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'\n✅ 已写入 {DST}')
print(f'   文件大小：{len(html)} 字符')
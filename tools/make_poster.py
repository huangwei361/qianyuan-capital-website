"""乾元资本带二维码宣传海报 V6 - 大字+亮色+酷炫版"""
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys, math
sys.stdout.reconfigure(encoding='utf-8')

# ============ 配色（更亮更现代）============
BG_TOP = (253, 250, 240)        # 浅暖白
BG_BOTTOM = (235, 240, 252)     # 浅冷蓝
GOLD = (218, 165, 32)           # 高饱和金
GOLD_BRIGHT = (255, 200, 60)    # 亮金
GOLD_DARK = (184, 134, 11)
NAVY = (10, 37, 64)
NAVY_DEEP = (6, 24, 42)
INK = (40, 50, 70)
GRAY = (140, 150, 165)
WHITE = (255, 255, 255)

# 装饰色（彩虹渐变）
RAINBOW = [
    (255, 200, 60),   # 金
    (255, 160, 80),   # 橙
    (220, 120, 160),  # 粉
    (160, 130, 220),  # 紫
    (100, 160, 230),  # 蓝
]

FONT_BOLD = r'C:\Windows\Fonts\msyhbd.ttc'
FONT_REG = r'C:\Windows\Fonts\msyh.ttc'
FONT_SERIF = r'C:\Windows\Fonts\STXINGKA.TTF'
FONT_KAI = r'C:\Windows\Fonts\STKAITI.TTF'

URL = 'https://huangwei361.github.io/qianyuan-capital-website/'
OUT = r'C:\Users\64549\.minimax\金融财富公司成立\乾元资本·集团海报·带二维码.png'


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


# ============ 二维码 ============
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=2)
qr.add_data(URL)
qr.make(fit=True)
qr_img = qr.make_image(fill_color='#0A2540', back_color='#FFFFFF').convert('RGB')
qr_size = 460
qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

# ============ 画布 ============
WIDTH = 1200
HEIGHT = 2000
img = Image.new('RGB', (WIDTH, HEIGHT), BG_TOP)

# ============ 径向光晕（左上 + 右下双光晕）============
glow_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)

# 巨型光晕 1（左上角暖色光晕）
for r in range(700, 100, -20):
    alpha = int(8 * (700 - r) / 600)
    color = (255, 220, 130, alpha)
    glow_draw.ellipse([(-r, -r), (r, r)], fill=color)

# 巨型光晕 2（右下角冷色光晕）
for r in range(700, 100, -20):
    alpha = int(6 * (700 - r) / 600)
    color = (140, 180, 240, alpha)
    glow_draw.ellipse([(WIDTH - r, HEIGHT - r), (WIDTH + r, HEIGHT + r)], fill=color)

img = Image.alpha_composite(img.convert('RGBA'), glow_layer).convert('RGB')

# 渐变背景
for y in range(HEIGHT):
    ratio = y / HEIGHT
    r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * ratio)
    g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * ratio)
    b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * ratio)
    for x in range(WIDTH):
        # 叠加光晕（每个像素加左上暖色光晕 + 右下冷色光晕）
        lx, ly = x, y
        dist1 = math.sqrt((lx - 200) ** 2 + (ly - 200) ** 2)
        glow1 = max(0, 1 - dist1 / 800) * 30
        dist2 = math.sqrt((lx - (WIDTH - 200)) ** 2 + (ly - (HEIGHT - 200)) ** 2)
        glow2 = max(0, 1 - dist2 / 800) * 20
        r = min(255, int(r + glow1 + glow2 * 0.7))
        g = min(255, int(g + glow1 * 0.7 + glow2 * 0.7))
        b = min(255, int(b + glow2))
        img.putpixel((x, y), (r, g, b))

draw = ImageDraw.Draw(img)
center_x = WIDTH // 2

# ============ 顶部金色装饰条 ============
draw.rectangle([(0, 0), (WIDTH, 12)], fill=GOLD)
draw.rectangle([(0, 16), (WIDTH, 22)], fill=GOLD_DARK)
# 三角齿
for i in range(0, WIDTH, 36):
    draw.polygon([(i, 0), (i + 18, 12), (i + 36, 0)], fill=GOLD_DARK)

# ============ 巨型"元"字水印（右上）============
watermark_font = load_font(FONT_BOLD, 620)
wm_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
wm_draw = ImageDraw.Draw(wm_layer)
# 金色描边 + 内部半透明
wm_draw.text((WIDTH - 480, -60), '元', font=watermark_font,
             fill=(218, 165, 32, 28))
img = Image.alpha_composite(img.convert('RGBA'), wm_layer).convert('RGB')
draw = ImageDraw.Draw(img)

# ============ 主标题区 ============
# Logo 圆
logo_x, logo_y = 160, 180
# 外层光晕圆（更大、金色更亮）
for r in range(120, 60, -10):
    alpha = int(20 * (120 - r) / 60)
    halo_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo_layer).ellipse(
        [(logo_x - r, logo_y - r), (logo_x + r, logo_y + r)],
        fill=(255, 200, 60, alpha))
    img = Image.alpha_composite(img.convert('RGBA'), halo_layer).convert('RGB')
draw = ImageDraw.Draw(img)

# 主 logo 圆
draw.ellipse([(logo_x - 80, logo_y - 80), (logo_x + 80, logo_y + 80)],
             fill=NAVY_DEEP, outline=GOLD, width=8)
draw.ellipse([(logo_x - 64, logo_y - 64), (logo_x + 64, logo_y + 64)],
             outline=GOLD_BRIGHT, width=2)
draw.text((logo_x, logo_y + 12), '元', font=load_font(FONT_BOLD, 100), fill=GOLD_BRIGHT, anchor='mm')

# 主标题"乾元资本"（超大）
title_x = 290
title_y = 110
draw.text((title_x, title_y), '乾元资本',
         font=load_font(FONT_SERIF, 170), fill=NAVY_DEEP, anchor='lm')
draw.text((title_x, title_y + 120), 'QIANYUAN  CAPITAL',
         font=load_font(FONT_BOLD, 40), fill=NAVY, anchor='lm', spacing=14)
draw.text((title_x, title_y + 180), '集  团  ·  筹  备  中',
         font=load_font(FONT_BOLD, 34), fill=GOLD_DARK, anchor='lm')

# ============ 印章（右上角，倾斜）============
seal_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
seal_draw = ImageDraw.Draw(seal_layer)
seal_cx, seal_cy = WIDTH - 260, 240
seal_r = 90
seal_draw.ellipse([(seal_cx - seal_r, seal_cy - seal_r), (seal_cx + seal_r, seal_cy + seal_r)],
                  outline=(184, 134, 11, 220), width=5)
seal_draw.ellipse([(seal_cx - seal_r + 10, seal_cy - seal_r + 10),
                   (seal_cx + seal_r - 10, seal_cy + seal_r - 10)],
                  outline=(184, 134, 11, 180), width=3)
seal_draw.text((seal_cx, seal_cy - 10), '乾', font=load_font(FONT_BOLD, 32),
                fill=(184, 134, 11, 220), anchor='mm')
seal_draw.text((seal_cx, seal_cy + 24), '元', font=load_font(FONT_BOLD, 32),
                fill=(184, 134, 11, 220), anchor='mm')
seal_draw.text((seal_cx, seal_cy + 56), 'CAPITAL',
                font=load_font(FONT_BOLD, 11),
                fill=(184, 134, 11, 220), anchor='mm')

# 印章旋转
seal_rotated = seal_layer.rotate(-15, resample=Image.BICUBIC)
img = Image.alpha_composite(img.convert('RGBA'), seal_rotated).convert('RGB')
draw = ImageDraw.Draw(img)

# 主标题下双线
draw.line([(70, 340), (WIDTH - 70, 340)], fill=GOLD, width=4)
draw.line([(70, 350), (WIDTH - 70, 350)], fill=GOLD_DARK, width=2)
draw.polygon([(center_x, 332), (center_x + 14, 345),
              (center_x, 358), (center_x - 14, 345)], fill=GOLD_DARK)

# ============ 大标语（巨字）============
slogan_y = 470
# slogan 阴影效果（柔和）
shadow_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
ImageDraw.Draw(shadow_layer).text((center_x + 4, slogan_y + 4), '5-8 年 长期主义',
         font=load_font(FONT_BOLD, 140), fill=(0, 0, 0, 30), anchor='mm')
img = Image.alpha_composite(img.convert('RGBA'), shadow_layer).convert('RGB')
draw = ImageDraw.Draw(img)
# slogan 主字（超粗深蓝 + 金边）
draw.text((center_x, slogan_y), '5-8 年 长期主义',
         font=load_font(FONT_BOLD, 140), fill=NAVY_DEEP, anchor='mm')

# 副标语
sub_y = slogan_y + 90
draw.text((center_x, sub_y), '个 人 研 究 方 向  ·   5 年 内 不 开 公 司',
         font=load_font(FONT_BOLD, 38), fill=INK, anchor='mm')

# ============ 1+5 架构（更大卡片）============
arch_label_y = sub_y + 90
draw.text((center_x, arch_label_y), '—  集  团  架 构  —',
         font=load_font(FONT_BOLD, 36), fill=GOLD_DARK, anchor='mm')

cluster_y = arch_label_y + 50
card_w = 215
card_h = 130
card_gap = 14
total_w = card_w * 5 + card_gap * 4
start_x = (WIDTH - total_w) // 2

clusters = [('投融资', '飞轮闭环'), ('黄金', '客户入口'),
            ('出海', 'AI外贸'), ('量化', '双事业部'),
            ('租赁', '稳定现金流')]

for i, (name, sub) in enumerate(clusters):
    x = start_x + i * (card_w + card_gap)
    # 卡片底（深蓝实底 + 金边 + 金色顶部条）
    draw.rounded_rectangle(
        [(x, cluster_y), (x + card_w, cluster_y + card_h)],
        radius=15, fill=NAVY_DEEP, outline=GOLD, width=4
    )
    # 顶部金色装饰条
    draw.rectangle([(x + 16, cluster_y + 10), (x + card_w - 16, cluster_y + 16)],
                   fill=GOLD)
    draw.rectangle([(x + 16, cluster_y + 18), (x + card_w - 16, cluster_y + 22)],
                   fill=GOLD_BRIGHT)
    # 主名
    draw.text((x + card_w // 2, cluster_y + 55), name,
             font=load_font(FONT_BOLD, 42), fill=GOLD_BRIGHT, anchor='mm')
    # 副标
    draw.text((x + card_w // 2, cluster_y + 100), sub,
             font=load_font(FONT_REG, 22), fill=WHITE, anchor='mm')

# ============ 飞轮核心（巨型几何版）============
flywheel_cy = cluster_y + card_h + 240
flywheel_cx = center_x
flywheel_r = 140

# 飞轮外层渐变光晕（大圆环）
halo_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
for r in range(flywheel_r + 120, flywheel_r, -8):
    alpha = int(15 * (flywheel_r + 120 - r) / 120)
    ImageDraw.Draw(halo_layer).ellipse(
        [(flywheel_cx - r, flywheel_cy - r), (flywheel_cx + r, flywheel_cy + r)],
        fill=(255, 200, 60, alpha))
img = Image.alpha_composite(img.convert('RGBA'), halo_layer).convert('RGB')
draw = ImageDraw.Draw(img)

# 5 条彩色径向光晕（背景辐射）
import math
ray_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
ray_draw = ImageDraw.Draw(ray_layer)
for i in range(5):
    a1 = math.radians(-90 + i * 72 - 12)
    a2 = math.radians(-90 + i * 72 + 12)
    # 三角辐射
    ray_draw.polygon([
        (flywheel_cx + 30 * math.cos(a1), flywheel_cy + 30 * math.sin(a1)),
        (flywheel_cx + (flywheel_r + 80) * math.cos((a1 + a2) / 2),
         flywheel_cy + (flywheel_r + 80) * math.sin((a1 + a2) / 2)),
        (flywheel_cx + 30 * math.cos(a2), flywheel_cy + 30 * math.sin(a2))
    ], fill=RAINBOW[i] + (60,))
img = Image.alpha_composite(img.convert('RGBA'), ray_layer).convert('RGB')
draw = ImageDraw.Draw(img)

# 外圈大圆环（金色描边）
draw.ellipse(
    [(flywheel_cx - flywheel_r - 30, flywheel_cy - flywheel_r - 30),
     (flywheel_cx + flywheel_r + 30, flywheel_cy + flywheel_r + 30)],
    outline=GOLD, width=4
)
# 内圈（虚线感）
for ang in range(0, 360, 8):
    a_rad = math.radians(ang)
    x1 = flywheel_cx + (flywheel_r - 10) * math.cos(a_rad)
    y1 = flywheel_cy + (flywheel_r - 10) * math.sin(a_rad)
    x2 = flywheel_cx + (flywheel_r - 4) * math.cos(a_rad)
    y2 = flywheel_cy + (flywheel_r - 4) * math.sin(a_rad)
    draw.line([(x1, y1), (x2, y2)], fill=GOLD_BRIGHT, width=2)

# 中心圆（巨型渐变）
center_r = 70
for r in range(center_r, 30, -2):
    alpha = int(255 * (center_r - r) / center_r * 0.3)
    grad_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(grad_layer).ellipse(
        [(flywheel_cx - r, flywheel_cy - r), (flywheel_cx + r, flywheel_cy + r)],
        fill=(10, 37, 64, alpha))
    img = Image.alpha_composite(img.convert('RGBA'), grad_layer).convert('RGB')
draw = ImageDraw.Draw(img)
draw.ellipse([(flywheel_cx - center_r, flywheel_cy - center_r),
              (flywheel_cx + center_r, flywheel_cy + center_r)],
             fill=NAVY_DEEP, outline=GOLD_BRIGHT, width=5)
draw.text((flywheel_cx, flywheel_cy - 8), '飞轮',
         font=load_font(FONT_BOLD, 38), fill=GOLD_BRIGHT, anchor='mm')
draw.text((flywheel_cx, flywheel_cy + 28), 'FLYWHEEL',
         font=load_font(FONT_BOLD, 12), fill=GOLD, anchor='mm')

# 5 个外圈节点（更大 + 彩色填充）
stages = [('融资', RAINBOW[0]), ('投资', RAINBOW[1]), ('业绩', RAINBOW[2]),
          ('信用', RAINBOW[3]), ('再融资', RAINBOW[4])]

for i, (name, color) in enumerate(stages):
    angle = math.radians(-90 + i * 72)
    node_x = flywheel_cx + flywheel_r * math.cos(angle)
    node_y = flywheel_cy + flywheel_r * math.sin(angle)
    # 节点圆（彩色填充 + 白边 + 阴影）
    shadow_l = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow_l).ellipse(
        [(node_x - 46, node_y - 42), (node_x + 46, node_y + 50)],
        fill=(0, 0, 0, 50))
    img = Image.alpha_composite(img.convert('RGBA'), shadow_l).convert('RGB')
    draw = ImageDraw.Draw(img)
    # 节点外层
    draw.ellipse([(node_x - 42, node_y - 42), (node_x + 42, node_y + 42)],
                 fill=color, outline=WHITE, width=3)
    # 节点文字（深蓝）
    draw.text((node_x, node_y), name, font=load_font(FONT_BOLD, 22),
              fill=NAVY_DEEP, anchor='mm')

# 5 个大箭头（环上，动感）
for i in range(5):
    a_mid = math.radians(-90 + (i + 0.5) * 72)
    a_next = math.radians(-90 + (i + 1) * 72)
    # 弧形箭头
    p1_x = flywheel_cx + (flywheel_r + 30) * math.cos(a_mid)
    p1_y = flywheel_cy + (flywheel_r + 30) * math.sin(a_mid)
    p2_x = flywheel_cx + (flywheel_r + 30) * math.cos(a_next - 0.15)
    p2_y = flywheel_cy + (flywheel_r + 30) * math.sin(a_next - 0.15)
    draw.line([(p1_x, p1_y), (p2_x, p2_y)], fill=GOLD_DARK, width=5)
    # 箭头三角
    tip_x = flywheel_cx + (flywheel_r + 38) * math.cos(a_next - 0.15)
    tip_y = flywheel_cy + (flywheel_r + 38) * math.sin(a_next - 0.15)
    draw.polygon([(tip_x, tip_y),
                  (tip_x - 18 * math.cos(a_next - 0.4), tip_y - 18 * math.sin(a_next - 0.4)),
                  (tip_x - 18 * math.cos(a_next + 0.1), tip_y - 18 * math.sin(a_next + 0.1))],
                 fill=GOLD_DARK)

# 飞轮下方标语
draw.text((flywheel_cx, flywheel_cy + flywheel_r + 120),
         '每  一  轮   比   上  一  轮   更  厚',
         font=load_font(FONT_BOLD, 38), fill=GOLD_DARK, anchor='mm')

# ============ 二维码区域 ============
contact_y = HEIGHT - 600
draw.line([(70, contact_y), (WIDTH - 70, contact_y)], fill=GOLD, width=4)
draw.line([(70, contact_y + 8), (WIDTH - 70, contact_y + 8)], fill=GOLD_DARK, width=2)
draw.polygon([(center_x, contact_y - 10), (center_x + 14, contact_y + 4),
              (center_x, contact_y + 18), (center_x - 14, contact_y + 4)], fill=GOLD_DARK)

draw.text((center_x, contact_y + 50), '—  扫 码 访 问 网 站  —',
         font=load_font(FONT_BOLD, 42), fill=NAVY_DEEP, anchor='mm')

# 二维码（左）+ 信息（右）布局
qr_x_pos = 130
qr_y_pos = contact_y + 100

# 双层边框（深蓝外 + 金边 + 白底）
draw.rectangle(
    [(qr_x_pos - 24, qr_y_pos - 24),
     (qr_x_pos + qr_size + 24, qr_y_pos + qr_size + 24)],
    fill=NAVY_DEEP
)
draw.rectangle(
    [(qr_x_pos - 18, qr_y_pos - 18),
     (qr_x_pos + qr_size + 18, qr_y_pos + qr_size + 18)],
    fill=GOLD_BRIGHT
)
draw.rectangle(
    [(qr_x_pos - 14, qr_y_pos - 14),
     (qr_x_pos + qr_size + 14, qr_y_pos + qr_size + 14)],
    fill=WHITE
)
img.paste(qr_img, (qr_x_pos, qr_y_pos))
img = img.convert('RGB')
draw = ImageDraw.Draw(img)

# 右侧信息（缩短 URL，拆成两行）
info_x = qr_x_pos + qr_size + 60
info_y = qr_y_pos + 60
draw.text((info_x, info_y), '集 团 官 网',
         font=load_font(FONT_BOLD, 38), fill=NAVY_DEEP, anchor='lm')
draw.text((info_x, info_y + 60), 'huangwei361',
         font=load_font(FONT_BOLD, 30), fill=NAVY, anchor='lm')
draw.text((info_x, info_y + 100), '.github.io/qianyuan',
         font=load_font(FONT_BOLD, 24), fill=GOLD_DARK, anchor='lm')
draw.text((info_x, info_y + 140), '-capital-website/',
         font=load_font(FONT_BOLD, 24), fill=GOLD_DARK, anchor='lm')

# 分隔线
draw.line([(info_x, info_y + 200), (info_x + 460, info_y + 200)], fill=GOLD, width=2)

draw.text((info_x, info_y + 240), '联 系 方 式',
         font=load_font(FONT_BOLD, 38), fill=NAVY_DEEP, anchor='lm')
draw.text((info_x, info_y + 310), '邮  箱：',
         font=load_font(FONT_REG, 24), fill=INK, anchor='lm')
draw.text((info_x + 110, info_y + 310), 'qygc@163.com',
         font=load_font(FONT_BOLD, 24), fill=GOLD_DARK, anchor='lm')
draw.text((info_x, info_y + 360), '欢迎合作 / 交流 / 建议',
         font=load_font(FONT_REG, 20), fill=GRAY, anchor='lm')

# ============ 底部 ============
draw.text((center_x, HEIGHT - 40),
         '本 海 报 为 个 人 博 客 性 质  ·  不 构 成 投 资 建 议     © 2026 乾 元 资 本  ·  5-8 年 长 期 主 义',
         font=load_font(FONT_REG, 18), fill=GRAY, anchor='mm')

img.save(OUT, 'PNG', quality=95)
print(f'OK: {OUT}')
print(f'Size: {os.path.getsize(OUT)} bytes')
# 乾元资本集团官网

> 1 集团 + 5 大业务集群（筹备中）· 5-8 年长期主义规划

乾元资本集团筹备期个人网站，记录集团母体的 5-8 年战略规划。包含集团架构、5 大业务集群的子网页、乾元出海的外贸商城等。

## 项目结构

```
website/
├── index.html                       # 集团主站
│
├── invest/                          # 投融资规划和管理（顶级集群）
│   ├── index.html                   # 集群入口
│   ├── plan.html                    # 投融资方案
│   ├── brochure.html                # 品牌故事宣传册
│   ├── qifu/
│   │   └── index.html               # 乾元企服（下挂）
│   └── asset/
│       └── index.html               # 乾元资产处理（下挂）
│
├── gold/                            # 乾元黄金
│   ├── index.html
│   └── dashboard.html               # 金价看板
│
├── global/                          # 乾元出海
│   ├── index.html                   # 介绍页
│   └── shop.html                    # 外贸商城
│
├── quant/                           # 乾元量化（1 公司 2 事业部）
│   ├── index.html                   # 总览
│   ├── trading.html                 # 交易事业部
│   ├── rd.html                      # 研发事业部
│   ├── rd.css                       # 研发子站独立样式
│   └── trading.css                  # 交易子站独立样式
│
├── rental/                          # 乾元租赁
│   └── index.html
│
├── style.css                        # 主站样式
├── main.js                          # 主站交互
├── _sub.css                         # 子站共享样式
│
├── tools/                           # 工具脚本（开发用，不入库）
│   ├── gen.py                       # 子站批量生成
│   ├── clean.py                     # 关键词清洗
│   ├── restructure.py               # 1+7→1+5 架构重构
│   ├── make_poster.py               # 海报生成
│   ├── md2docx.py                   # Markdown → Word 转换
│   ├── gen_pdf.py                   # 宣传册 PDF 生成
│   ├── publish.py                   # 文件发布（处理锁文件）
│   ├── verify_links.py              # 链接验证
│   └── ...                          # 其他辅助脚本
│
└── assets/
    └── img/                         # 8 个 Logo + icon
```

## 部署

所有业务子站按集群分目录组织。任何静态 web server 即可托管：

```bash
# 本地预览
python -m http.server 8000

# 部署
# GitHub Pages 自动从 main 分支部署
# URL：https://huangwei361.github.io/qianyuan-capital-website/

# 备用：hoshin.xin（个人 ICP 备案）
# 把整个 website/ 目录上传到服务器
```

## URL 结构（GitHub Pages 部署后）

| 集群 | URL |
|---|---|
| 集团主站 | `/` |
| 投融资规划和管理 | `/invest/` |
| └─ 乾元企服 | `/invest/qifu/` |
| └─ 乾元资产处理 | `/invest/asset/` |
| └─ 投融资方案 | `/invest/plan.html` |
| └─ 品牌故事册 | `/invest/brochure.html` |
| 乾元黄金 | `/gold/` |
| └─ 金价看板 | `/gold/dashboard.html` |
| 乾元出海 | `/global/` |
| └─ 外贸商城 | `/global/shop.html` |
| 乾元量化 | `/quant/` |
| └─ 交易事业部 | `/quant/trading.html` |
| └─ 研发事业部 | `/quant/rd.html` |
| 乾元租赁 | `/rental/` |

## 1+5 业务架构

### 1 集团（顶层）
- **乾元资本集团**：母体，5-8 年长期主义

### 5 大业务集群

| # | 集群 | 业务方向 | 5 年内状态 |
|---|---|---|---|
| 1 | 乾元投融资规划和管理 | 找钱 + 用钱 + 循环（飞轮闭环）· 下挂企服、资产处理 | ⚪ 长期规划 |
| 2 | 乾元黄金 | 实物黄金购销 / 积存金 / 旧金回收 | 🟢 试水 |
| 3 | 乾元出海 | AI 外贸 / Dropshipping 跨境 | 🟢 主力 |
| 4 | 乾元量化 | 1 家公司 · 2 个事业部（交易/研发）| 🟡 小试 5-10 万 |
| 5 | 乾元租赁 | 房产租赁 / 代运营 | ⚪ 自营 4 套 |

### 下挂业务（隶属于投融资规划和管理）

- **乾元企服**：集团内部资金中心 / 8 大职能
- **乾元资产处理**：法拍房 / 不良债权

## 设计风格

- 主色：深海蓝 `#0A2540` + 金色 `#D4AF37`
- 字体：微软雅黑
- 视觉：圆形徽章 + 篆刻感
- 部署类目：博客-个人空间（个人 ICP 备案）

## 开发工具

```bash
# 启动本地预览
python -m http.server 8000

# 验证所有页面链接
python tools/verify_links.py

# 生成新的子站
python tools/gen.py
```

## License

个人博客性质，不构成投资建议或商业承诺。